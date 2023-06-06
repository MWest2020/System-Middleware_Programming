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


    # getting ugly with the 3 parameters
    def group_TCP(self, connection,  data ) -> dict:
        
        # dictionary to store TCP connections
        TCP_connections = {}

        for packet in data:
            nested = packet["_source"]["layers"]
            # tuple for TCP connection (src ip, src port, dst ip, dst port) 
            
            # Working here on specific connection
            # all connections
            # connection = (nested["ip"]["ip.src"], nested["tcp"]["tcp.srcport"], nested["ip"]["ip.dst"], nested["tcp"]["tcp.dstport"])
            
            # specific connection
            # connection =  ('192.168.1.9', '80', '10.128.0.26', '60755')

            


            # when connection is not found
            if connection not in TCP_connections:
                TCP_connections[connection] = []
                print('TCP connection not found')

            # if TCP connection is found, add to dictionary.
            TCP_connections[connection].append(packet)

        for key, value in TCP_connections.items():
            # print(key, value)
            print(list(dict.fromkeys(TCP_connections)))
            print(f"\n \n \n \n \n ****************************** \n {len(TCP_connections)} packets grouped \n ****************************** \n \n")
