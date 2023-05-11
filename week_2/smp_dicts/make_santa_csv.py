#!/usr/bin/env python3

import csv
import random
from faker import Faker

fake = Faker()

def generate_people_csv(num_people, filename):
    # Generate `num_people` random people with random names, birth dates, and postal codes
    people = []
    for i in range(num_people):
        name = fake.name()
        birth_date = fake.date_of_birth(minimum_age=1, maximum_age=18)
        postal_code = fake.postcode()
        house_number = random.randint(1, 100)
        gift_given = random.choice([True, False])
        behavior = random.choice(["goed", "slecht"])
        people.append((name, birth_date, f"{postal_code} {house_number}", gift_given, behavior))

    # Write the data to a CSV file with the given `filename`
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['naam', 'geboortedata', 'Postcode', 'gift_given', 'gedrag'])
        for person in people:
            writer.writerow(person)

# Example usage: generate a CSV file with x random people and name the file "my_people.csv"
generate_people_csv(1250, 'kids_US.csv')
generate_people_csv(1250, 'kids_EU.csv')
generate_people_csv(1250, 'kids_UK.csv')
generate_people_csv(1250, 'kids_RUS.csv')