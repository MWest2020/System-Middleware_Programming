# standard library to work with json
import json


class DataProcessor:

    # No need for self as argument
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
            # Extract the TCP information from the packet
            tcp_info = packet["_source"]["layers"]["tcp"]

            # Extract the source and destination IP addresses and ports
            src_ip = packet["_source"]["layers"]["ip"]["ip.src"]
            dst_ip = packet["_source"]["layers"]["ip"]["ip.dst"]
            src_port = tcp_info["tcp.srcport"]
            dst_port = tcp_info["tcp.dstport"]

            # Create a TCP connection tuple and add it to the list
            tcp_connection = (src_ip, src_port, dst_ip, dst_port)
            tcp_connections.append(tcp_connection)

        # remove duplicates from the list (set does this)
        tcp_connections = list(set(tcp_connections))

        # Print the extracted TCP connections
        return tcp_connections

    def compare_blacklist(self, connections, blacklist):
        blacklisted_connections = []

        for connection in connections:
            # Split the connection into src IP and dst IP
            src_ip, src_port, dst_ip, dst_port = connection
            for blacklisted in blacklist:
                # If the blacklisted item is a complete connection
                if len(blacklisted) == 4:
                    # checks for blacklisted tcp connections and appends to list
                    if connection == tuple(blacklisted):
                        blacklisted_connections.append(connection)
                else:
                    # If the blacklisted item is just an IP address
                    if dst_ip == blacklisted[0] or src_ip == blacklisted[0]:
                        blacklisted_connections.append(connection)

        return blacklisted_connections


