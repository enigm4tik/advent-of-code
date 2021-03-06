# Advent of Code - 2016
## Day 21

import numpy as np
import re

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

password = 'abcde' # test value
password = 'abcdefgh'
password2 = 'decab' # test value
# password2 = 'dbfgaehc' # test value
password2 = 'fbgdceah'
password = [letter for letter in password]
password2 = [letter for letter in password2]

def calculate_ultimate_position(index):
    """Calculate the ultimate position when rotating based on index"""

    if index < 4:
        index += index + 1
    else:
        index += index + 2
    index = index % len(password)
    return index

rotation_dictionary = {index: calculate_ultimate_position(index) for index in range(len(password))}
reversed_dictionary = {key: value for value, key in rotation_dictionary.items()}

def calculate_rotation(index, reversed=False):
    """Calculate the rotation based on the calculated ultimate position"""

    calculated_index = rotation_dictionary[index]
    if reversed:
        calculated_index = reversed_dictionary[index]
    rotation = calculated_index - index 
    if calculated_index == 0:
        rotation = 1
    if reversed and calculated_index == 0:
        rotation *= -1 
    return rotation


def parse_instructions(line, password, reversed=False):
    """Call appropriate function based on line"""

    if line.startswith('swap position'):
        index_x, index_y = re.findall('[0-9]+', line)
        password = swap_positions(password, int(index_x), int(index_y))
    elif line.startswith('swap letter'):
        a, b, letter1, c, d, letter2 = line.split(' ')
        password = swap_letters(password, letter1, letter2)
    elif line.startswith('reverse'):
        position1, position2 = re.findall('[0-9]+', line)
        password = reverse_string(password, int(position1), int(position2))
    elif line.startswith('rotate left') or line.startswith('rotate right'):
        a, direction, steps, b = line.split(' ')
        if direction == 'left':
            steps = (-1) * int(steps)
        else:
            steps = int(steps)
        if reversed:
            steps = (-1) * steps
        password = roll_by_steps(password, steps)
    elif line.startswith('rotate based'):
        if reversed:
            password = rotate_backwards(password, line[-1])
        else:
            password = rotate_based_on_position(password, line[-1])
    elif line.startswith('move'):
        index_x, index_y = re.findall('[0-9]+', line)
        if reversed:
            index_x, index_y = index_y, index_x
        password = move_letter_to_position(password, int(index_x), int(index_y))
    return password


def swap_positions(password, index_x, index_y):
    """Swap letters at the two given indexes"""

    password[index_x], password[index_y] = password[index_y], password[index_x]
    return password


def swap_letters(password, letter1, letter2):
    """Swap the two given letters in the string"""

    index_1 = password.index(letter1)
    index_2 = password.index(letter2)
    password[index_1], password[index_2] = password[index_2], password[index_1]
    return password


def roll_by_steps(password, steps):
    """Rotate all letters by the given amounts of steps"""

    password = list(np.roll(password, steps))
    return password


def rotate_based_on_position(password, letter):
    """Rotate letters to the right once, then index of letter, then once more if index > 4"""

    index = password.index(letter)
    if index >= 4:
        index +=1
    password = np.roll(password, 1+index)
    password = list(password)
    return password


def rotate_backwards(password, letter):
    """Additional function to reverse the rotation based on position"""

    index = password.index(letter)
    rollindex = calculate_rotation(index, True)
    password = list(np.roll(password, rollindex))
    return password


def reverse_string(password, index_x, index_y):
    """Reverse the letters between the given indexes"""

    sublist = password[index_x: index_y + 1]
    sublist.reverse()
    password[index_x: index_y + 1] = sublist
    return password


def move_letter_to_position(password, index_x, index_y):
    """Move letter from index x to index y"""
    
    letter_to_move = password.pop(index_x)
    password.insert(index_y, letter_to_move)
    return password


for line in lines: 
    password = parse_instructions(line, password)

print(f"Part 1: {''.join(password)}")

lines.reverse()

for line in lines: 
    password2 = parse_instructions(line, password2, True)

print(f"Part 2: {''.join(password2)}")