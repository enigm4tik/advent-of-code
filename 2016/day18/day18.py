# Advent of Code - 2016
## Day 18

import numpy as np
np.set_printoptions(threshold=np.inf)

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

rows = 40

trap_room = np.full([rows, len(lines[0])], 0, dtype=str)

def parse_row_into_room():
    for index, character in enumerate(lines[0]):
        trap_room[0][index] = character

parse_row_into_room()

def plan_trap_room():
    for i in range(1, rows):
        for j in range(len(lines[0])):
            neighbors = find_neighbors((i, j))
            if is_this_a_trap(neighbors):
                trap_room[i][j] = '^'
            else:
                trap_room[i][j] = '.'

def find_neighbors(position):
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

plan_trap_room()
print(trap_room)
print(len(trap_room[trap_room=='.']))