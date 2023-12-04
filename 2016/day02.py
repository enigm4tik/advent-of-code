# Advent of Code - 2016
## Day 2

import numpy as np

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def decipher_digit(code, starting_digit='5', keypad=None, length=0):
    returning_coordinate = [0, 0]
    starting_coordinate = np.where(keypad==starting_digit)
    starting_coordinate = list(*tuple(zip(*starting_coordinate)))
    for index, letter in enumerate(code):
        if index == 0:
            returning_coordinate = starting_coordinate
        row = returning_coordinate[0] + directions[letter][0]
        column = returning_coordinate[1] + directions[letter][1]
        if row <= length and row >= 0 and column <= length and column >= 0 and keypad[(row, column)] != '0':
            returning_coordinate[0] = row
            returning_coordinate[1] = column
    return keypad[tuple(returning_coordinate)]


def decipher_code(iteration=0, digit='5', returning_code='', keypad=None):
    length = keypad.shape[0] - 1
    if iteration == len(lines):
        return returning_code
    to_decipher = lines[iteration]
    deciphered_digit = decipher_digit(to_decipher, digit, keypad, length)
    return decipher_code(iteration + 1, deciphered_digit, returning_code + str(deciphered_digit), keypad)


keypad = np.array([
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
    ])

print(f"Part 1: {decipher_code(keypad=keypad)}")

altered_keypad = np.array([
    ['0', '0', '1', '0', '0'], 
    ['0', '2', '3', '4', '0'], 
    ['5', '6', '7', '8', '9'], 
    ['0', 'A', 'B', 'C', '0'], 
    ['0', '0', 'D', '0', '0']
    ])

print(f"Part 2: {decipher_code(keypad=altered_keypad)}")
