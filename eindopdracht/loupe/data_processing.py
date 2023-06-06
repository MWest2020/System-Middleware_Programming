# standard library to work with json
import json

class DataProcessor:
    
    # No need for self as argument
    # @staticmethod
    def read_json(self, file_path):
        # reads and returns json data
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data
        
    # Writing json. 
    def write_json(self, file_path, json_data):
        with open(file_path, 'w') as f:
            json.dump(json_data, f)

    def group_TCP(key, data ) -> dict:
        
        # dictionary to store TCP connections
        TCP_connections = {}

        for packet in data:
            nested = packet["_source"]["layers"]
            # tuple for TCP connection (src ip, src port, dst ip, dst port) 
            key = (nested["ip"]["ip.src"], nested["tcp"]["tcp.srcport"], nested["ip"]["ip.dst"], nested["tcp"]["tcp.dstport"])
        
            # when key is not found
            if key not in TCP_connections:
                TCP_connections[key] = []
                print('TCP connection not found')

            # if TCP connection is found, add to dictionary.
            TCP_connections[key].append(packet)

