# Advent of Code - 2021
## Day 1 - Part 1

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

horizontal = 0
vertical = 0

for line in lines:
    direction, amount = line.split(' ')
    if direction == 'forward':
        horizontal += int(amount)
    if direction == 'up':
        vertical -= int(amount)
    if direction == 'down':
        vertical += int(amount)

print(f"Part 1 - Result: {horizontal * vertical}")


## Day 2 - Part 2

horizontal = 0
aim = 0
depth = 0

for line in lines:
    direction, amount = line.split(' ')
    if direction == 'forward':
        horizontal += int(amount)
        depth += aim * int(amount)
    if direction == 'up':
        aim -= int(amount)
    if direction == 'down':
        aim += int(amount)

print(f"Part 2 - Result: {horizontal * depth}")