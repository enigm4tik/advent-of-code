# Advent of Code - 2015
## Day 6

import numpy as np

# with open('test_input', 'r') as file:
with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

instructions = {}

for index, line in enumerate(lines):
    all_instructions = line.split(" ")
    if all_instructions[0] == 'turn':
        instructions[index] = [all_instructions[1], all_instructions[2], all_instructions[4]]
    else: 
        instructions[index] = [all_instructions[0], all_instructions[1], all_instructions[3]]

grid = np.full([1000, 1000], 0, int)
full_ones = np.full([1000, 1000], 1, int)

# grid = np.full([10, 10], 0, int) # for debug purposes of test data

def day06(part1=True):
    for instruction in instructions.values():
        todo, start, end = instruction
        start_1, start_2 = start.split(',')
        start_1, start_2 = int(start_1), int(start_2)
        end_1, end_2 = end.split(',')
        end_1, end_2 = int(end_1), int(end_2)
        subarray = grid[start_1:end_1+1, start_2:end_2+1]
        if todo == 'on':
            if part1: 
                subarray.fill(1) 
            else:
                np.add.at(subarray, None, 1)
        elif todo == 'off':
            if part1:
                subarray.fill(0) 
            else:
                np.add.at(subarray, None, -1)
                subarray[subarray<1] = 0
        else:
            if part1:
                full_ones = np.full(subarray.shape, 1, int)
                subarray2 = np.logical_xor(subarray, full_ones).astype(int)
                np.copyto(subarray, subarray2)       
            else:
                np.add.at(subarray, None, 2)
    if part1:
        return f"Part 1: {len(grid[grid==1])}"
    else:
        return f"Part 2: {grid.sum()}"

print(day06())
print(day06(False))