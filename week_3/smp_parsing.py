#!/usr/bin/env python3

import re
import csv

csv_file = 'output.csv'


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


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def get_commands(pattern, text):
    return re.findall(pattern, text)


command_list = get_commands(r'\$ cd \w+', read_file('output.txt'))


def get_command_dicts(list):
    return [dict(command=command) for command in list]


command_list = get_command_dicts(command_list)


def process_integers_text(file_name):
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


def sum_integers(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    numbers = []
    for line in lines:
        if re.search(r'\d+', line):
            numbers.append(int(line))
    return sum(numbers)


# Example usage:
file_name = 'output.txt'
copy_csv_to_txt('output.csv', 'output.txt')
process_integers_text(file_name)
strip_text(file_name)
read_file(file_name)


def accumulate_size(file_name, commands_list):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    processed_lines = []
    numbers_sum = 0

    # Flatten the list of dictionaries into a set of command strings
    commands = set()
    for command_dict in commands_list:
        commands.update(command_dict.values())

    for line in lines:
        line = line.strip()

        # Check for a command from the flattened set
        if line in commands:
            # Append buffered numbers to the previous line if it's not empty
            if numbers_sum > 0:

                processed_lines.append(str(numbers_sum))
                numbers_sum = 0

            processed_lines.append(line)
        elif re.search(r'\d', line):
            # Add numbers to buffer
            numbers_sum += int(line)
        else:
            # Empty the numbers buffer if a non-integer line is encountered
            numbers_sum = 0

    # Append buffered numbers if any remain at the end
    if numbers_sum > 0:
        processed_lines.append(''.join(str(processed_lines)))

    with open(file_name, 'w') as file:
        file.writelines('\n'.join(processed_lines))


accumulate_size(file_name, command_list)


def get_largest_directory(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    largest_number = None
    largest_number_index = None

    for i, line in enumerate(lines):
        line = line.strip()

        if re.match(r'^\d+$', line):
            number = int(line)

            if largest_number is None or number > largest_number:
                largest_number = number
                largest_number_index = i

    if largest_number_index is not None:
        command = lines[largest_number_index - 1].strip()
        print(
            f"The largest number is {largest_number}, and the command above it is '{command}'")


get_largest_directory(file_name)
