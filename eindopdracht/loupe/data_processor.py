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
            tcp_connections.append(tcp_connection)

        # # remove duplicates from the list (set does this)
        # tcp_connections = list(set(tcp_connections))

        # Print the extracted TCP connections
        # print(tcp_connections[0])
        return tcp_connections
    
        
    def write_tcp_connections(self, connections, file_path):
        # tuples to list 
        connections = [list(connection) for connection in connections]
        
        self.write_json('../data/tcp_connections.json', connections )
        
    def analyze_tcp_connections(self, file_path):
        connections = self.read_json(file_path)
        print("Total num. of TCP connections: {}", len(connections) )        

    def compare_blacklist(self, connections, blacklist):
        blacklisted_connections = []

        for connection in connections:
            # checks for blacklisted tcp connections and appends to list
            connection_tuple = (connection.get('ip.src'), connection.get('tcp.srcport'), connection.get('ip.dst'), connection.get('tcp.dstport'))
                # If the 'blacklist' is a list of dictionaries
            if isinstance(blacklist, list) and isinstance(blacklist[0], dict):
                for blacklisted in blacklist:
                    blacklisted_tuple = (blacklisted.get('ip.src'), blacklisted.get('tcp.srcport'), blacklisted.get('ip.dst'), blacklisted.get('tcp.dstport'))
                    if connection_tuple == blacklisted_tuple:
                        blacklisted_connections.append(connection)

            # If the 'blacklist' is a tuple
            elif isinstance(blacklist, tuple):
                if connection_tuple == blacklist:
                    print(connections)
                    blacklisted_connections.append(connection)

        return blacklisted_connections

