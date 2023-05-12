#!/usr/bin/env python3

import csv
import random
import ast

# Read all data and store in dictionary (key = name, value = data(?))
# General function for any csv to dict


def csv_to_dict(filename):
    # list to store dicts
    result = []

    with open('kids_EU.csv', 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            value = row['gift_given']
            boolean_value = convert_to_bool(value)
            row["gift_given"] = boolean_value
            
            result.append(row)

    return result


def convert_to_bool(value):
    try:
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return None



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




# Write a function that automatically assigns a gift to a kid
#  - use complete dictionary as parameter
#  - Change assign gift from false to true
#  - print a string: "{Kidname} was {good / bad} has been assigned a gift. {giftname} delivered under tree"
# - if kid has been assigned a gift, print a string: "{Kidname} has already been assigned a gift. Hopefully {giftname} is desireably"

def assign_kid_present(kids_list):
    key = "gift_given"
    for child in kids_list:
        if not child[key]:
            child["cadeau"] = gift_randomizer()
            string_goed_of_slecht = "goed" if child.get('gedrag', 'goed') else "stout"
            print(f"{child.get('naam')} was {string_goed_of_slecht}. We hebben een {child['cadeau']} onder de boom gelegd")
            # not setting to True -- csv read only
            child[key] = True
        else:
            print(f"Oh nee, {child.get('naam')} heeft al een cadeau gekregen")
       

kids_list = csv_to_dict('kids_EU.csv')


assign_kid_present(kids_list)



# def main():
#     csv_to_dict('kids_EU.csv')
#     assign_kid_present(dict, "gift_given")



