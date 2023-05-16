# standard library to work with json
import json

class DataProcessor:
   
    # No need for self as argument
    @staticmethod
    def read_json(file_path):
        with open() as f:
            data = json.load(f)
            return data
        
    # Voor het geval. 
    def write_json(self, file_path, json_data):
        with open(file_path, 'w') as f:
            json.dump(json_data, f)