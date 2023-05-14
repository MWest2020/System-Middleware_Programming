#!/usr/bin/env python3

import csv
import re


# read from csv and print line by line

def read_csv_and_print(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            print(row)

# read_csv_and_print('output.csv')

# from dict to list. -- why? 
def from_dict_make_list(filename):
    result = []
    
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
    
        for row in reader:
            result.append([value for value in row.values()])
    
    return result

# list = from_dict_make_list('output.csv')
# print(list)

def write_csv_to_list(filename):
    result = []
    
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            
            result.append(row)
    
    return result


new_list = write_csv_to_list('output.csv')







# write a fuction that returns the name and size of the biggest folder
def find_largest_directory(csv_file):
    directories = {}
    largest_size = 0
    largest_directory = ""

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        current_directory = "/"
        current_size = 0

        for row in csv_reader:
            command = row[0].strip()

            if command.startswith("$ cd"):


                pattern = r'\$ cd [a-z]+'

                command = command
                match = re.match(pattern, command)

                if match:
                    print(match.group())
                

                







            # elif command.startswith("ls") or command.startswith("dir"):
            #     parts = command.split(" ")
            #     if len(parts) >= 2:
            #         try:
            #             size = int(parts[1])
            #             filename = " ".join(parts[2:])
            #         except ValueError:
            #             continue
            #         current_size += size

            #         if current_size > largest_size:
            #             largest_size = current_size
            #             largest_directory = current_directory

    return largest_size, largest_directory


largest_size, largest_directory = find_largest_directory('output.csv')
print("Largest Size:", largest_size)
print("Largest Directory:", largest_directory)