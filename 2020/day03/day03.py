# Advent of Code - 2020
## Day 3 - Part 1

import numpy as np 

with open('day03_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

array = np.empty([len(lines), len(lines[0])], str)

for index, line in enumerate(lines):
    for v_index, input in enumerate(line): 
        array[index, v_index] = input

def move_x_and_y_down_matrix(matrix, x, y, result):
    y_dim, x_dim = array.shape
    x = adjust_x_to_matrix_width(x, x_dim)
    try: 
        result.append(matrix[y, x])
    except:
        pass # end of the matrix

def adjust_x_to_matrix_width(x, width):
    while x >= width:
        x = x-width
    return x

def traverse_with_slope(matrix, x, y):
    result = []
    for i in range(len(lines)):
            move_x_and_y_down_matrix(array, x+i*x, y+y*i, result)
    return(result.count('#'))

part1 = traverse_with_slope(array, 3, 1)
print(f"Part 1 - Result: {part1}")

## Day 3 - Part 2

list_of_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

list_of_slope_results = []
for slope in list_of_slopes:
    list_of_slope_results.append(traverse_with_slope(array, *slope))

product = 1
for item in list_of_slope_results:
    product = product * item 

print(f"Part 2 - Result: {product}")
