# Advent of Code - 2023
## Day 10

import numpy as np

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

LOOKUP_TABLE = {
    "|": {"up": "up", "down": "down"},
    "-": {"right": "right", "left": "left"},
    "F": {"up": "right", "left": "down"},
    "J": {"right": "up", "down": "left"},
    "L": {"down": "right", "left": "up"}, 
    "7": {"right": "down", "up": "left"}
}

DIRECTIONS = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
}

def setup_numpy_array(lines):
    """
    Create a numpy array from a list of strings
    :param lines: list of strings
    :return: numpy array
    """
    array = np.empty([len(lines), len(lines[0])], str)
    for index, line in enumerate(lines):
        for v_index, input in enumerate(line): 
            array[index, v_index] = input
    return array


def traverse_pipes(array):
    """
    Find the path in a numpy array based on rules:
    J, L, 7 and F turn by 90°, - and | move horizontal or vertical
    :param array: numpy array
    :return: tuple (path, furthest point in the path)
    """
    position = list(zip(*np.where(array == "S")))[0] # start behan
    pipe = 'J' 
    direction = 'right' 
    length = 0
    path = []
    while pipe != "S":
        v, h = position
        path.append((v, h))
        direction = LOOKUP_TABLE[pipe][direction]
        position = (v + DIRECTIONS[direction][0], h + (DIRECTIONS[direction][1]))
        pipe = array[position]
        length += 1
    return path, length//2


def determine_inside_values(array):
    """
    Use "ray casting" to determine whether a point is inside 
    or outside of the shape of the path. 
    :param array: numpy array:
    :return: integer, amount of elements inside the path
    """
    array[array == "S"] = "J"

    for i in range(len(lines)):
        subarray = array[i, :]
        current_direction = ""
        for idx, value in enumerate(subarray): 
            value = (i, idx)
            if value not in path:
                if array[i, idx-1] == "O":
                    array[i, idx] = "O"
                    continue
                elif array[i, idx-1] == "I":
                    array[i, idx] = "I"
                    continue
                hits = 0
                current_direction = ""
                for j in range(idx, len(subarray)):
                    if (i, j) in path: 
                        if array[i, j] == "|":
                            hits += 1
                            continue
                        elif array[i, j] == "-":
                            continue
                        else:
                            movement = [x for x in LOOKUP_TABLE[array[i, j]].values() if x in ["up", "down"]]
                            if current_direction:
                                if movement == current_direction: 
                                    hits += 2
                                else:
                                    hits += 1
                                current_direction = ""
                            else:
                                current_direction = movement
                if hits % 2 == 0:
                    array[i, idx] = "O"
                else: 
                    array[i, idx] = "I"
    return(len(array[array=="I"]))

array = setup_numpy_array(lines)
path, part1 = traverse_pipes(array)
part2 = determine_inside_values(array)

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 10':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1:^55}")
print(f"Part 2: {part2:^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")
