# Advent of Code - 2016
## Day 18

import numpy as np
np.set_printoptions(threshold=np.inf)

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]


def setup_matrix():
    trap_room = np.full([2, len(lines[0])], 0, dtype=str)
    parse_row_into_room(trap_room)
    amount_of_safe_rooms = len(trap_room[trap_room=='.'])
    return trap_room, amount_of_safe_rooms


def parse_row_into_room(trap_room):
    for index, character in enumerate(lines[0]):
        trap_room[0][index] = character


def plan_trap_room(trap_room, amount_of_safe_rooms):
    for j in range(len(lines[0])):
        neighbors = find_neighbors((1, j), trap_room)
        if is_this_a_trap(neighbors):
            trap_room[1][j] = '^'
        else: 
            trap_room[1][j] = '.'
    blabla = list(trap_room[1])
    amount_of_safe_rooms += blabla.count('.')
    trap_room = np.roll(trap_room, 1, axis=0)
    return trap_room, amount_of_safe_rooms


def find_neighbors(position, trap_room):
    row, column = position
    left = column - 1 
    right = column + 1
    
    if right < len(lines[0]):
        right_neighbor = trap_room[row-1][right]
    else:
        right_neighbor = '.'

    if left >= 0:
        left_neighbor = trap_room[row-1][left]
    else:
        left_neighbor = '.'

    center_neighbor = trap_room[row-1][column]

    neighbors = [left_neighbor, center_neighbor, right_neighbor]
    return neighbors


def is_this_a_trap(neighbors):
    """Returns True if it is a trap."""
    
    is_a_trap = False

    left, center, right = neighbors

    if left == center == '^' and right != '^':
        is_a_trap = True
    elif right == center == '^' and left != '^':
        is_a_trap = True
    elif left == '^' and right == center == '.':
        is_a_trap = True
    elif right == '^' and left == center == '-':
        is_a_trap = True
    return is_a_trap


def calculate_day_18(rows):
    trap_room, amount_of_safe_rooms = setup_matrix()
    for i in range(rows-1):
        trap_room, amount_of_safe_rooms = plan_trap_room(trap_room, amount_of_safe_rooms)
    return amount_of_safe_rooms

part1 = calculate_day_18(40)
print(f"Part 1: {part1}")

part2 = calculate_day_18(400000)
print(f"Part 2: {part2}")
