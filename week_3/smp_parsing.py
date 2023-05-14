#!/usr/bin/env python3

import re
import csv

csv_file= 'output.csv'

def content_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)
    
def copy_csv_to_txt(csv_file_path, txt_file_path):
    with open(csv_file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        
        with open(txt_file_path, 'w') as txt_file:
            for row in reader:
                txt_file.write('\t'.join(row) + '\n')

copy_csv_to_txt('output.csv', 'output.txt')

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def get_commands(pattern, text):
    return re.findall(pattern, text)

command_list = get_commands(r'\$ cd \w+', read_file('output.txt'))


def get_command_dicts(list):
    return [dict(command=command) for command in list]

command_list = get_command_dicts(command_list)




def process_text(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # process lines with both integer and strip string
    processed_lines = []
    for line in lines:
        if re.search(r'\d', line) and re.search(r'[a-zA-Z]', line):
            numbers = re.findall(r'\d+', line)
            line = '\n'.join(numbers) + '\n'
        processed_lines.append(line)

    # overwrite output text file
    with open(file_name, 'w') as file:
        file.writelines(processed_lines)

def strip_text(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    processed_lines = []

    for line in lines:
        if re.search(r'\$ cd \w+', line):
            processed_lines.append(line)
        if re.search(r'\d+', line):
            processed_lines.append(line)
        

    # overwrite output text file
    with open(file_name, 'w') as file:
        file.writelines(processed_lines)



# Example usage:
file_name = 'output.txt'
process_text(file_name)
strip_text(file_name)
read_file(file_name)






# print(command_list)

