# Advent of Code - 2021
## Day 9 - Part 1

import numpy as np

with open('puzzle_input', 'r') as file:
# with open('test_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

empty = np.empty([len(lines), len(lines[0])], int)

for index, line in enumerate(lines): 
    for index2, letter in enumerate(line): 
        empty[index][index2] = letter

def find_neighbor(array, x, y, values=True):
    upper_neighbor = lower_neighbor = left_neighbor = right_neighbor = 0
    max_x, max_y = array.shape

    if x == 0:
        upper_neighbor = None
    if x == max_x-1:
        lower_neighbor = None
    if y == 0:
        left_neighbor = None
    if y == max_y-1:
        right_neighbor = None

    if not upper_neighbor is None:
        upper_neighbor = array[x-1][y]
    if not lower_neighbor is None: 
        lower_neighbor = array[x+1][y]
    if not left_neighbor is None:
        left_neighbor = array[x][y-1]
    if not right_neighbor is None:
        right_neighbor = array[x][y+1]

    if values: 
        return left_neighbor, right_neighbor, lower_neighbor, upper_neighbor
    else:
        left = (x, y-1)
        right = (x, y+1)
        lower = (x+1, y)
        upper = (x-1, y)
        invalid = [9, None]
        if left_neighbor in invalid:
            left = False
        if right_neighbor in invalid:
            right = False
        if lower_neighbor in invalid:
            lower = False
        if upper_neighbor in invalid:
            upper = False
        
        return left, right, lower, upper

def is_this_a_local_minimum(array, x, y):
    
    me = array[x][y]
    if me == 9: # a 9 cannot be a low value
        return False
    if me == 0: # a 0 has to be a high value
        return True

    left_neighbor, right_neighbor, lower_neighbor, upper_neighbor = find_neighbor(array, x, y)
    
    my_neighbors = list(set([left_neighbor, right_neighbor, lower_neighbor, upper_neighbor]))
    my_not_none_neighbors = list(filter(None.__ne__, my_neighbors))
    
    for neighbor in my_not_none_neighbors:
        if neighbor < me:
            return False
    return True

list_of_local_min_values = []
list_of_local_min_locations = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        local_min = is_this_a_local_minimum(empty, i, j)
        if local_min:
            list_of_local_min_values.append(empty[i][j])
            list_of_local_min_locations.append((i, j))

print(f"Part 1 - Result: {sum(list_of_local_min_values)+len(list_of_local_min_values)}")

## Day 9 - Part 2

def find_neighbor_until_9(array, x, y, result=[]):
    res = find_neighbor(array, x, y, False)
    for r in res:
        if r:
            a, b = r
            if not r in result:
                result.append(r)
                find_neighbor_until_9(array, a, b, result)
    return result

list_of_basins = []
list_of_basin_locations = []
for local_min in list_of_local_min_locations:
    x, y = local_min
    basin = find_neighbor_until_9(empty, x, y, [])
    list_of_basins.append(len(basin))
    list_of_basin_locations.append(basin)

list_of_basins.sort()
three_largest_basins = list_of_basins[-3:]

print(f"Part 2 - Result: {three_largest_basins[0]*three_largest_basins[1]*three_largest_basins[2]}")