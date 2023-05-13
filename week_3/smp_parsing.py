#!/usr/bin/env python3


import csv
import os 

filename = 'output.csv'

# read from csv and print line by line

def read_csv_and_print(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            print(row)

read_csv_and_print('output.csv')






# def write_csv_to_list(filename):
#     result = []
    
#     with open(filename, 'r') as f:
#         reader = csv.DictReader(f)
        
#         for row in reader:
            
#             result.append(row)
    
#     return result


# new_list = write_csv_to_list('output.csv')

# print(new_list)