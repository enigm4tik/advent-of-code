# Advent of Code - 2015
## Day 12

import json

with open('puzzle_input.json', 'r') as file:
    myjson = json.load(file)

dict_from_json = myjson[0]

NUMBERS = []
NUMBERS2 = []


def get_number_from_values(value, part2=False):
    try:
        new_number = float(value)
        if part2:
            NUMBERS2.append(new_number)
        else:
            NUMBERS.append(new_number)
    except ValueError:
        pass
    except TypeError:
        if isinstance(value, list):
            for i in value:
                get_number_from_values(i, part2)
        elif isinstance(value, dict):
            if part2:
                if not "red" in value.values(): 
                    calc_numbers(value, part2)
            else: 
                calc_numbers(value, part2)


def calc_numbers(dictionary, part2=False):
    if isinstance(dictionary, list):
        get_number_from_values(dictionary, part2)
    else:
        for value in dictionary.values():
            if isinstance(value, dict):
                if part2 and "red" in value.values():
                    continue
                else: 
                    calc_numbers(value, part2)
            else:
                get_number_from_values(value, part2)
        

for dictionary in myjson:
    calc_numbers(dictionary)
    calc_numbers(dictionary, True)

print(f"Part 1: {int(sum(NUMBERS))}")
print(f"Part 2: {int(sum(NUMBERS2))}")