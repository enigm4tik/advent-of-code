# Advent of Code - 2015
## Day 17

import itertools

with open("puzzle_input") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

target = 150
results = []
length_of_containers = {}
for index, i in enumerate(range(len(lines))):
    for i in itertools.combinations(lines, i):
        if sum(i) == target:
            results.append(i)
            if not index in length_of_containers: 
                length_of_containers[index] = 1
            else:
                length_of_containers[index] += 1

print(f"Part 1: {len(results)}")
print(f"Part 2: {length_of_containers[min(length_of_containers)]}")
