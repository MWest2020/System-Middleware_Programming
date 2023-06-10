# standard library to work with json
import json


class DataProcessor:

    
    # @staticmethod
    def read_json(self, file_path):
        # reads and returns json data
        with open("../data/" + file_path, 'r') as f:
            data = json.load(f)
            return data

    # read text file
    def read_text(self, file_path):
        with open(file_path, 'r') as f:
            data = f.readlines(file_path)
            return data

    # write text file

    def write_text(self, file_path, data):
        with open(file_path, 'w') as f:
            f.write(data)

    # Writing json.
    def write_json(self, file_path, json_data):
        with open(file_path, 'w') as f:
            json.dump(json_data, f, indent=4)

    def get_tcp_connections(self, data):
        # Initialize an empty list to store TCP connections
        tcp_connections = []

        # Iterate through each packet in the dataset
        for packet in data:
            tcp_info = packet["_source"]["layers"]["tcp"]
            ip_info = packet["_source"]["layers"]["ip"]
            frame = packet["_source"]["layers"]["frame"]


            # Add the timestamp from the frame object
            raw_timestamp = frame['frame.time']
            timestamp_parts = raw_timestamp.split()
            cleaned_timestamp = ' '.join(timestamp_parts[:4])
            tcp_info['timestamp'] = cleaned_timestamp

            # Create a TCP connection dictionary and add it to the list
            tcp_connection = {**ip_info, **tcp_info}
            # print(f"{tcp_connection}")
            tcp_connections.append(tcp_connection)

        # Print the extracted TCP connections
        return tcp_connections

    def compare_blacklist(self, connections, blacklist):
        blacklisted_connections = []

        for connection in connections:
            # Convert each connection to a dictionary
            connection_dict = self.connection_to_dict(connection)

            # Check if the connection is blacklisted
            if self.is_blacklisted(connection_dict, blacklist):
                blacklisted_connections.append(connection)

        return blacklisted_connections

    def connection_to_dict(self, connection):
        return {
            'ip.src': connection.get('ip.src'),
            'tcp.srcport': connection.get('tcp.srcport'),
            'ip.dst': connection.get('ip.dst'),
            'tcp.dstport': connection.get('tcp.dstport')
        }

    def is_blacklisted(self, connection_dict, blacklist):
        # If the 'blacklist' is a list of dictionaries
        if isinstance(blacklist, list) and isinstance(blacklist[0], dict):
            return self.is_in_list(connection_dict, blacklist)

        # If the 'blacklist' is a dictionary
        elif isinstance(blacklist, dict):
            return connection_dict == blacklist

        return False

    def is_in_list(self, connection_dict, blacklist):
        for blacklisted in blacklist:
            blacklisted_dict = self.connection_to_dict(blacklisted)
            if connection_dict == blacklisted_dict:
                return True

        return False

    def check_blacklisted_ips(self, blacklisted, blacklist_file):
        # Read the blacklist file and make a list of ips 
        blacklist = self.read_json(blacklist_file)

        blacklisted_ips = [
            item['ip.src'] for item in blacklist if 'ip.src' in item] + [
            item['ip.dst'] for item in blacklist if 'ip.dst' in item]

        # Create a set to store printed IP addresses
        printed_ips = set()

        # Iterate over the blacklisted connections and check each source and
        # destination IP
        for connection in blacklisted:
            src_ip = connection['ip.src']
            dst_ip = connection['ip.dst']
            if src_ip in blacklisted_ips and src_ip not in printed_ips:
                print(f"The source IP address {src_ip} is blacklisted.")
                printed_ips.add(src_ip)
            if dst_ip in blacklisted_ips and dst_ip not in printed_ips:
                print(f"The destination IP address {dst_ip} is blacklisted.")
                printed_ips.add(dst_ip)
                
                
    ## BEYOND BLACK
        
    def get_tcp_flag_changes(self, src_ip, src_port, dst_ip, dst_port):
        
        # hardcoded, because otherwise too many arguments (already) in fucntion signature
        tcp_connections = self.read_json('../data/tcp_connections.json')
        
        # filter for specific tcp connections
        connection_packets = [
            conn for conn in tcp_connections
            if (conn['ip.src'] == src_ip
                and conn['tcp.srcport'] == src_port
                and conn['ip.dst'] == dst_ip
                and conn['tcp.dstport'] == dst_port)
        ]

        printed_timestamp = False
        for packet in connection_packets:
            if not printed_timestamp:
                print(f"Connections are captured on: {packet['timestamp']} GMT")
                printed_timestamp = True
            
            flag_value_hex = packet['tcp.flags']
            active_flags = self.decode_tcp_flags(flag_value_hex)
            attack_name = self.detect_attack(active_flags)
            
            # time relative to capture wireshark. One would need to know that.
            print(f"Time: {packet['Timestamps']['tcp.time_relative']}, Flags: {active_flags}, Detected: {attack_name} ")

    def decode_tcp_flags(self, flag_value):
        
        # hex to latin letters
        flags = {
        'FIN': 0x01,
        'SYN': 0x02,
        'RST': 0x04,
        'PSH': 0x08,
        'ACK': 0x10,
        'URG': 0x20,
        'ECE': 0x40,
        'CWR': 0x80
        }
        
        # hex to integer
        flag_value = int(flag_value, 16)
        
        active_flags = [
            
            flag for flag, 
            item in flags.items() if flag_value & item
        ]
        
        return active_flags
    
    
    def detect_attack(self, flags):
        
        attack_map = {
        frozenset(['SYN', 'FIN']): "SYN-FIN attack",
        frozenset(['SYN', 'RST']): "SYN-RST attack",
        frozenset(['SYN', 'URG']): "SYN-URG attack",
        frozenset(['FIN', 'ACK']): "FIN-ACK attack",
        frozenset(['FIN', 'PSH', 'URG']): "FIN-PSH-URG attack",
        frozenset(['PSH', 'URG']): "PSH-URG attack",
        frozenset(['RST', 'PSH']): "RST-PSH attack",
        frozenset(['ACK', 'FIN', 'RST']): "ACK-FIN-RST attack",
        }
        
        #  check if key is in attack_map
        attack_name = attack_map.get(frozenset(flags))
                                     
        return attack_name