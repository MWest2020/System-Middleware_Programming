# standard library to work with json
import json


class DataProcessor:

    # TODO : No need for self as argument?
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

