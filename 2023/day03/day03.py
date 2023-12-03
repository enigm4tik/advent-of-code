# Advent of Code - 2023
## Day 3

import numpy as np

def prepare_numpy_array(lines):
    """
    Create a numpy array that is as big as the input. 
    One character per index and collect all special characters
    :param lines: list of strings
    :return: numpy array, list of symbols
    """
    array = np.empty([len(lines), len(lines[0])], str)
    list_of_symbols = []
    for index, line in enumerate(lines):
        for v_index, input in enumerate(line): 
            array[index, v_index] = input
            if not input in list_of_symbols:
                try: 
                    int(input)
                except ValueError:
                    list_of_symbols.append(input)

    return array, list_of_symbols


def prepare_indices_of_symbols(array, list_of_symbols):
    """
    Create a list of all indices for each symbol
    :param array: numpy array
    :param list_of_symbols: list of special characters
    :return: dictionary {special character: [list of indices]}
    """
    list_of_symbols.remove(".")
    indices_of_symbols = {}
    for symbol in list_of_symbols:
        indices = np.where(array == symbol)
        indices_of_symbols[symbol] = list(zip(*indices))
    return indices_of_symbols


def find_valid_neighbors(index, array):
    """
    Find all values that are neighboring a special character,
    remove all neighbors that have a '.'.
    :param index: tuple (horizontal, vertical)
    :param array: numpy array
    :return: list of tuples (index)
    """
    h, v = index 
    left = (h, v-1)
    right = (h, v+1)
    up = (h-1, v)
    down = (h+1, v)
    leftup = (h-1, v-1)
    rightup = (h-1, v+1)
    leftdown = (h+1, v-1)
    rightdown = (h+1, v+1)

    neighbors = [left, right, up, down, leftup, rightup, leftdown, rightdown]
    unwanted = []
    for neighbor in neighbors:
        if v == 0:
            unwanted += [left, leftup, leftdown]
        if v == len(lines[0]):
            unwanted += [right, rightup, rightdown]
        if h == 0: 
            unwanted += [up, leftup, rightup]
        if h == len(lines):
            unwanted += [down, leftdown, rightdown]
    unwanted = list(set(unwanted))
    neighbors = list(set(neighbors) - set(unwanted))

    valid_neighbors = []
    for neighbor in neighbors: 
        if array[neighbor] != ".":
            valid_neighbors.append(neighbor)

    return valid_neighbors


def find_part_number(index, array):
    """
    Determine the part number by finding the left most neighbor,
    then walking to the right until a symbol (either . or special character) is found.
    Replacing all numbers with '.' to prevent duplications.
    :param: index, tuple
    :param array: numpy array
    :return: changed array and value
    """
    h, v = index 
    while v >= 0 and array[h, v-1] != "." and array[h, v-1] not in list_of_symbols:
        v-= 1
    number = ""
    while v < len(lines[0]) and array[h, v] != "." and array[h, v] not in list_of_symbols:
        number += array[h, v]
        array[h, v] = "."
        v += 1
    try:
        return array, int(number)
    except ValueError:
        return array, 0
    

def part1(array, indices_of_symbols):
    """
    Calculating the sum of all parts touching any special character. 
    :param array: numpy array
    :param indices_of_symbols: dictionary of symbols and their indices
    :return: integer, sum of parts
    """
    list_of_valid_neighbors = []
    sum_of_parts = 0
    for indices in indices_of_symbols.values():
        for index in indices:
            list_of_valid_neighbors = find_valid_neighbors(index, array)

            for valid_neighbor in list_of_valid_neighbors: 
                array, result = find_part_number(valid_neighbor, array)
                sum_of_parts += result
    return sum_of_parts

# Part 2

def part2(array, indices_of_symbols):
    """
    Calculating the product of parts touching gears (*) only when there are exactly 2. 
    Then summing all of the products up. 
    :param array: numpy array
    :param indices_of_symbols: dictionary of symbols and their indices
    :return: integer, sum of gear_ratio
    """
    gear_ratio = 0
    for index in indices_of_symbols["*"]:
        gear_parts = []
        valid_neighbors = find_valid_neighbors(index, array)
        for valid_neighbor in valid_neighbors:
            array, result = find_part_number(valid_neighbor, array)
            if not result == 0: gear_parts.append(result)
        if len(gear_parts) == 2:
            gear_ratio += gear_parts[0] * gear_parts[1]
    return gear_ratio


with open('puzzle_input') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

array, list_of_symbols = prepare_numpy_array(lines)
indices_of_symbols = prepare_indices_of_symbols(array, list_of_symbols)
array2, list_of_symbols = prepare_numpy_array(lines)
    

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 3':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1(array, indices_of_symbols):^55}")
print(f"Part 2: {part2(array2, indices_of_symbols):^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")