# Advent of Code - 2016
## Day 5

import hashlib

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()

string_to_hash = lines[0]

i = 0

password = ''
second_password = ['#' for i in range(8)]

while len(password) < 8 or any((i == '#' for i in second_password)):
    string_i = str(i)
    string_to_hash += string_i
    result = hashlib.md5(string_to_hash.encode())
    hex_result = result.hexdigest()
    string_to_hash = string_to_hash[:-len(string_i)]
    if hex_result.startswith('00000'):
        if not len(password) >= 8:
            password += str(hex_result)[5]
        position = hex_result[5]
        try:
            position = int(position)
            character = str(hex_result)[6]
            if position <= 7 and second_password[position] == '#':
                second_password[int(position)] = character
        except ValueError:
            pass # Invalid position
    i += 1

print(f"Part 1: {password}")
print(f"Part 2: {''.join(second_password)}")
