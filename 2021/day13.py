# Advent of Code - 2021
## Day 13 - Part 1

import numpy as np
np.set_printoptions(threshold=np.inf, linewidth=200)

with open('puzzle_input', 'r') as file:
# with open('test_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

fold_instructions = []
coordinates = []
for line in lines: 
    if line and not line.startswith('f'):
        y, x = line.split(',')
        coordinates.append((int(x), int(y)))
    elif line and line.startswith('f'):
        instructions = line.split('fold along ')[1]
        direction, where = instructions.split('=')
        fold_instructions.append((direction, where))

def find_biggest_x_and_y(coordinates):
    biggest_x = 0
    biggest_y = 0

    for x, y in coordinates:
        if x > biggest_x:
            biggest_x = x
        if y > biggest_y:
            biggest_y = y

    # this assumes that the paper is folded in half
    # if not (sneaky fold, make sure to adjust paper (in either side!)        
    return (biggest_x + 1, biggest_y + 1)

matrix = np.full((find_biggest_x_and_y(coordinates)), 0, dtype=int)

for x, y in coordinates:
    matrix[x][y] = 1

def fold_matrix_horizontally(where, matrix):
    matrix_with_deleted_fold_line = np.delete(matrix, where, 0)
    
    half_one, half_two = np.vsplit(matrix_with_deleted_fold_line, 2)
    
    half_two_flipped_upside_down = np.flipud(half_two)

    resulting_matrix = np.add(half_one, half_two_flipped_upside_down)

    resulting_matrix[resulting_matrix>1] = 1
    
    return resulting_matrix

def fold_matrix_vertically(where, array):
    matrix_with_deleted_fold_line = np.delete(array, where, 1)
    
    half_one, half_two = np.hsplit(matrix_with_deleted_fold_line, 2)
    
    half_two_flipped_left_right = np.fliplr(half_two)

    resulting_matrix = np.add(half_one, half_two_flipped_left_right)

    resulting_matrix[resulting_matrix>1] = 1
    
    return resulting_matrix

first_fold = fold_matrix_vertically(655, matrix)

part1 = len(first_fold[first_fold==1])
print(f"Part 1 - Result: {part1}")

## Day 13 - Part 2

def fold_matrix(direction, where, matrix):
    if direction == 'x':
        folded_matrix = fold_matrix_vertically(where, matrix)
    if direction == 'y':
        folded_matrix = fold_matrix_horizontally(where, matrix)
    return folded_matrix

def fold_matrix_according_to_fold_instructions(matrix, fold_instructions, iteration=0):
    if iteration == len(fold_instructions):
        return matrix
    direction, where = fold_instructions[iteration]
    folded_matrix = fold_matrix(direction, int(where), matrix)
    return fold_matrix_according_to_fold_instructions(folded_matrix, fold_instructions, iteration+1)
    
matrix = fold_matrix_according_to_fold_instructions(matrix, fold_instructions)

print(f"Part 2 - Result: PCPHARKL")
print(matrix)
# To see the result properly I suggest grepping the 1s.
