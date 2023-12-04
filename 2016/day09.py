# Advent of Code - 2016
## Day 9

import numpy as np
import re

# with open('puzzle_input') as file:
with open('test_input') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

def find_marker(code):
    match = re.findall(r"(\(\w+\))", code)
    if match:
        return match[0]
    else:
        return False

def execute_marker(code, match):
    returning_string = ''
    start = code.index(match)
    resume = start + len(match)
    characters, multiplicator = match[1:-1].split('x')
    returning_string = code[0:start]
    duplicated_string = code[resume:resume + int(characters)]
    for i in range(int(multiplicator)):
        returning_string += duplicated_string
    execute_code = code[resume + int(characters):]
    return execute_code, returning_string

all_deciphered_codes = []
for line in lines: 
    execute_code = line
    returning_code = ''
    while find_marker(execute_code):
        match = find_marker(execute_code)
        execute_code, returned_code = execute_marker(execute_code, match)
        returning_code += returned_code
    else:
        returning_code += execute_code
    all_deciphered_codes.append(returning_code)

string_of_all_codes = ''.join(all_deciphered_codes)
print(len(string_of_all_codes))
