#!/usr/bin/env python3

import csv

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




# def write_csv_to_list(filename):
#     result = []
    
#     with open(filename, 'r') as f:
#         reader = csv.DictReader(f)
        
#         for row in reader:
            
#             result.append(row)
    
#     return result


# new_list = write_csv_to_list('output.csv')

# print(new_list)