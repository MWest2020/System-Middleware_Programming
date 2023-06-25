# standard library to work with json
from datetime import datetime
import json
import os

class DataProcessor:

    # @staticmethod
    def read_json(self, file_path):
    # reads and returns json data
        if not os.path.isabs(file_path):
            file_path = os.path.join("../data/", file_path)
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data

    # Writing json.
    def write_json(self, file_path, json_data):
        if not os.path.isabs(file_path):
            file_path = os.path.join("../data/", file_path)
        with open(file_path, 'w') as f:
            json.dump(json_data, f, indent=4)


    # this function takes in a JSON wireshark capture (tested with flood.json)
    def get_tcp_connections(self, data) -> list:
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
            tcp_connections.append(tcp_connection)

        # Print the extracted TCP connections
        return tcp_connections

    # takes in the ouput (tcp connections from the get_tcp_connections function)
    # and processes them into a TCP ID with timestamp
    # and outputs to filepath a JSON
    def get_connection_durations(self, tcp_connections, file_path):
        connection_times = {}

        for connection in tcp_connections:
            connection_id = (
                connection["ip.src"],
                connection["tcp.srcport"],
                connection["ip.dst"],
                connection["tcp.dstport"]
            )

            # Parse the timestamp into a datetime object
            # [:23] hacky solution for cutting off beyond 6 digits (the 3 digits)
            # really prone to errors if we change the date string
            timestamp = datetime.strptime(
                connection["timestamp"][:23], '%b %d, %Y %H:%M:%S.%f')

            if connection_id not in connection_times:
                connection_times[connection_id] = [timestamp, timestamp]
            else:
                # Update the earliest and latest timestamps for this connection
                connection_times[connection_id] = [
                    min(connection_times[connection_id][0], timestamp),
                    max(connection_times[connection_id][1], timestamp)
                ]

        # Calculate the durations
        connection_durations = {
            # key =  conn_id, with value the later time - earlier time to float
            # in secs
            conn_id: (times[1] - times[0]).total_seconds()
            # for each (tuple) pair in the dict
            for conn_id, times in connection_times.items()
        }

        return connection_durations

    def get_long_connections(self, connection_durations, duration_threshold):
        long_connections = {
            conn_id: duration for conn_id,
            duration in connection_durations.items()
            if duration > duration_threshold
        }
        return long_connections

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

    def get_tcp_flag_changes(self, src_ip, src_port, dst_ip, dst_port):

        # hardcoded, because otherwise too many arguments (already) in fucntion
        # signature
        tcp_connections = self.read_json('../data/tcp_connections.json')

        # filter for specific tcp connections
        connection_packets = [
            conn for conn in tcp_connections
            if ((conn) or conn['ip.src'] == src_ip and
                (src_port is None or conn['tcp.srcport'] == src_port) and
                conn['ip.dst'] == dst_ip and
                (dst_port is None or conn['tcp.dstport'] == dst_port))
        ]

        # Make sure the packets are ordered by time (if they are not already)
        # sorting by key for advanced sorting
        connection_packets.sort(
            key=lambda packet: packet['Timestamps']['tcp.time_relative'])

        print(f"Filtered TCP connections: {len(connection_packets)}")

        printed_timestamp = False
        for packet in connection_packets:
            if not printed_timestamp:
                print(
                    f"\nConnections are captured on: {packet['timestamp']} GMT\n")
                printed_timestamp = True

            flag_value_hex = packet['tcp.flags']
            active_flags = self.decode_tcp_flags(flag_value_hex)
            attack_name = self.identify_attack_type(active_flags)

            # time relative to capture wireshark. One would need to know that.
            if attack_name is not None:
                print(f"Time: {packet['Timestamps']['tcp.time_relative']}")
                print(f"Flags: {active_flags}, Detected: {attack_name} ")

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

    def identify_attack_type(self, flags):
        flags_set = set(flags)

        attack_map = {
            frozenset(['SYN', 'FIN']): "Anomaly : SYN-FIN",
            frozenset(['SYN', 'ACK']): "Check for previous SYN.",
            frozenset(['SYN', 'RST']): "Anomaly : SYN-RST",
            frozenset(['SYN', 'URG']): "Anomaly : SYN-URG ",
            # may be needed if long streak occurs
            # frozenset(['FIN', 'ACK']): "Possible FIN-ACK attack, check for
            # previous FIN / RST",
            frozenset(['FIN', 'PSH', 'URG']): "Anomaly: FIN-PSH-URG. Possible Christmas Tree",
            frozenset(['RST', 'ACK']): "Check for previous SYN. Possible TCP RST attack.",
            frozenset(['PSH', 'URG']): "Uncommon: PSH-URG",
            frozenset(['ACK', 'PSH', 'RST', 'FIN']): "ACK-PSH-RST-FIN Flood attack detected",
            frozenset(['ACK', 'FIN', 'RST']): "Uncommon: ACK-FIN-RST, need to inspect further",
            frozenset(['ACK', 'PSH', 'FIN']): "Uncommon: ACK-PSH-FIN, need to inspect further",
        }

        detected_attacks = []

        for attack_flags, attack_name in attack_map.items():
            if attack_flags.issubset(flags_set):
                detected_attacks.append(attack_name)

        return detected_attacks if detected_attacks else None

    def scan_dataset_for_attacks(self, data, filename):
        attack_list = []
        for packet in data:
            flag_value_hex = packet['tcp.flags']
            set_flags = self.decode_tcp_flags(flag_value_hex)
            connection = (
                packet['ip.src'],
                packet['tcp.srcport'],
                packet['ip.dst'],
                packet['tcp.dstport'])

            # skip certain packets
            if set(set_flags) == {'ACK'}:
                continue

            attack_name = self.identify_attack_type(set_flags)

            if attack_name:
                # Add details of potential attack to the list
                attack_data = {
                    'time': packet['Timestamps']['tcp.time_relative'],
                    'connection': connection,
                    'flags': set_flags,
                    'attack_name': attack_name
                }
                attack_list.append(attack_data)

        self.write_json(filename, attack_list)

    # After initial review @Maarten
    # this was needed for the output of the connections

    def transform_connections(self, connections):
        transformed_connections = {}
        for i, (k, v) in enumerate(connections.items()):
            src_ip, src_port, dst_ip, dst_port = k

            new_entry = {
                "ip.src": src_ip,
                "tcp.srcport": src_port,
                "ip.dst": dst_ip,
                "tcp.dstport": dst_port,
                "duration": v
            }

            transformed_connections[f'connection_{i}'] = new_entry
        return transformed_connections

    def check_duration_and_blacklist(self, duration_data, blacklist_data):
        blacklisted_connections = {}

        # Convert blacklist_data to a set of tuples for faster checking
        blacklist_set = set(
            (item['ip.src'],
             item['tcp.srcport'],
                item['ip.dst'],
                item['tcp.dstport']) for item in blacklist_data)

        for connection_id, connection_data in duration_data.items():
            # Convert port numbers to string for comparison
            connection_data["tcp.srcport"] = str(
                connection_data["tcp.srcport"])
            connection_data["tcp.dstport"] = str(
                connection_data["tcp.dstport"])

            connection_tuple = (
                connection_data['ip.src'],
                connection_data['tcp.srcport'],
                connection_data['ip.dst'],
                connection_data['tcp.dstport'])

            if connection_tuple in blacklist_set:
                blacklisted_connections[connection_id] = connection_data
                print(
                    f"{connection_id} lasted {connection_data['duration']}",
                    "seconds long and is blacklisted.")

        return blacklisted_connections
