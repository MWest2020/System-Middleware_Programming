#! /usr/bin/env python3

import json


# 1. open json
def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# 2 standardise json


def process_json(json_data):
    processed_data = []
    for data in json_data:
        if 'source' in data and 'destination' in data:
            src_ip, src_port = data['source'].split(':')
            dest_ip, dest_port = data['destination'].split(':')

            data['src_ip'] = src_ip
            data['src_port'] = int(src_port)
            data['dest_ip'] = dest_ip
            data['dest_port'] = int(dest_port)

            del data['source']
            del data['destination']
        processed_data.append(data)

    # kill the comma bug
    replace_commas_in_ips(processed_data)

    clean_white_spaces(processed_data)

    return processed_data


def replace_commas_in_ips(json_data):
    for data in json_data:
        if 'src_ip' in data:
            data['src_ip'] = '.'.join(data['src_ip'].split(','))
        if 'dest_ip' in data:
            data['dest_ip'] = '.'.join(data['dest_ip'].split(','))

    return json_data


def clean_white_spaces(json_data):
    for data in json_data:
        if 'src_ip' in data:
            data['src_ip'] = data['src_ip'].strip()
        if 'dest_ip' in data:
            data['dest_ip'] = data['dest_ip'].strip()
        if 'timestamp' in data:
            data['timestamp'] = data['timestamp'].strip()

    return json_data


json_data = read_json('networkdata.json')
processed_data = process_json(json_data)


# 3  write to networkdataclean.json
def write_json(json_data, output_file):

    with open(output_file, 'w') as f:
        json.dump(json_data, f, indent=2)


write_json(processed_data, 'networkdataclean.json')
