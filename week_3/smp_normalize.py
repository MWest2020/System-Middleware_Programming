#! /usr/bin/env python3

import json

# 1. open json
# 2 standardise json
#  write to networkdataclean.json

# returns a dictionary
def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
# print(read_json('networkdata.json'))

def process_json(json_data):
    processed_data = []
    for data in json_data:
        if 'source' in data and 'destination' in data:
            src_ip, src_port = data['source'].split(':')
            dst_ip, dst_port = data['destination'].split(':')

            data['src_ip'] = src_ip.replace(',', '.')
            data['src_port'] = int(src_port)
            data['dst_ip'] = dst_ip.replace(',', '.')
            data['dst_port'] = int(dst_port)

            del data['source']
            del data['destination']
        processed_data.append(data)

    return processed_data


json_data = read_json('networkdata.json')
processed_data = process_json(json_data)

def write_json(json_data, output_file):
    
    with open(output_file, 'w') as f:
        json.dump(json_data, f, indent=2)
        

write_json(processed_data, 'networkdataclean.txt')




