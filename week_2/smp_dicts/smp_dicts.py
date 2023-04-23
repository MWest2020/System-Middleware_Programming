import csv

with open('kids_EU.csv', 'r') as f:
    reader = csv.Dictreader(f)
    for row in reader:


# Read all data and store in dictionary (key = name, value = data(?)    )

# Assign each kid a present or charcoal

# Track if kid has been given a gift in the dictionary (key gift_given, value a bool)

# Write a function that automatically assigns a gift to a kid
#  - use complete dictionary as parameter
#  - Change assign gift from false to true
#  - print a string: "{Kidname} was {good / bad} has been assigned a gift. {giftname} delivered under tree" 
# - if kid has been assigned a gift, print a string: "{Kidname} has already been assigned a gift. Hopefully {giftname} is desireably"