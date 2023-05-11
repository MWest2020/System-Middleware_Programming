#!/usr/bin/env python3

import csv
import random

# Read all data and store in dictionary (key = name, value = data(?))
# General function for any csv to dict
def csv_to_dict(filename):
    # list to store dicts
    result = []

    with open('kids_EU.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 
            result.append(dict(row))
    
    return result;

eu = csv_to_dict('kids_EU.csv')
print(eu)

def gift_randomizer() -> str:
    dice_roll = random.randint(1, 6)

    if dice_roll == 1:  
        return ""
    elif dice_roll == 2:
        return "pony"
    elif dice_roll == 3:
        return "ps5"
    elif dice_roll == 4:
        return "nintendo switch"
    elif dice_roll == 5:
        return "lego"
    elif dice_roll == 6:
        return "barbie"



# # Assign each kid a present or charcoal
# # only one parameter, the dictionary, because this function is only for one type of dict. 
def assign_kid_present(list):
    key = "gift_given"
    for dict in list:
        if dict[key] == "False":
           dict["cadeau"] = gift_randomizer() 
           dict[key] == "True"
           string_goed_of_slecht = "goed" if dict.get('gedrag', 'goed') else "stout"
           
           print(f"{dict.get('naam')} was {string_goed_of_slecht}. We hebben een {dict['cadeau']} onder de boom gelegd")             
        else:
            print(f"oh, nee, {dict.get('naam')} heeft al een cadeau gekregen")

assign_kid_present(eu)


# def main():
#     csv_to_dict('kids_EU.csv')
#     assign_kid_present(dict, "gift_given")

# Assign each kid a present or charcoal

# Track if kid has been given a gift in the dictionary (key gift_given, value a bool)

# Write a function that automatically assigns a gift to a kid
#  - use complete dictionary as parameter
#  - Change assign gift from false to true
#  - print a string: "{Kidname} was {good / bad} has been assigned a gift. {giftname} delivered under tree" 
# - if kid has been assigned a gift, print a string: "{Kidname} has already been assigned a gift. Hopefully {giftname} is desireably"