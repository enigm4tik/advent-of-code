# Advent of Code - 2016
## Day 6

import numpy as np

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

scramble = np.full((len(lines), len(lines[0])), '', dtype=str)

for index, line in enumerate(lines): 
    scramble[index] = [letter for letter in line]

part1 = ''
part2 = ''
for i in range(len(lines[0])):
    sliced_column = scramble[:, i]
    values, counts = np.unique(sliced_column, return_counts=True)
    most_frequent_value = values[counts==np.amax(counts)]
    least_frequent_value = values[counts==np.amin(counts)]
    part1 += most_frequent_value.item()
    part2 += least_frequent_value.item()

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
