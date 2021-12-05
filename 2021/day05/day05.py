# Advent of Code - 2021
## Day 5 - Part 1

import numpy as np

with open('day05_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# Size of array should be computed, hard-coded because I got frustrated :D
array = np.zeros([1000, 1000], int)

def fill_array_row_or_column(beginning, end, part2=False):
    y1 = beginning[0]
    y2 = end[0]
    x1 = beginning[1]
    x2 = end[1]

    if x1 == x2:
        if y1 > y2: 
            y1, y2 = y2, y1
        array[x1, y1:y2+1] += 1
        
    elif y1 == y2: 
        if x1 > x2:
            x1, x2 = x2, x1
        array[x1:x2+1, y1] += 1    
    else: 
        if part2:
            fill_diagonal(beginning, end)

## Day 5 - Part 2

def fill_diagonal(beginning, end):
    y1 = beginning[0]
    y2 = end[0]
    x1 = beginning[1]
    x2 = end[1]
    i = 0
    while i <= abs(x1-x2):
        if x1 > x2: 
            if y1 > y2: 
                array[x1 - i, y1 - i] += 1
                pass
            else: 
                array[x1 - i, y1 + i] += 1
                pass
        else: 
            if y1 > y2: 
                array[x1 + i, y1 - i] += 1
                pass
            else: 
                array[x1 + i, y1 + i] += 1
        i += 1


for line in lines:
    val1, val2 = line.split(' -> ')
    val1 = eval(val1)
    val2 = eval(val2)
    fill_array_row_or_column(val1, val2, part2=False) # change to True for part2

print(f"Part 1 - Result: {np.count_nonzero(array>=2)}")
#print(f"Part 2 - Result: {np.count_nonzero(array>=2)}")