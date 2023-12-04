# Advent of Code - 2020
## Day 1 - Part 1

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

summand1 = 0
summand2 = 0

for x in lines: 
    for y in lines:
        if x == y: 
            continue
        else: 
            if x + y == 2020: 
                summand1 = x
                summand2 = y
                break

print(f"Part 1 - Result: {summand1 * summand2}")

## Day 1 - Part 2

summand1 = 0
summand2 = 0
summand3 = 0

for x in lines: 
    for y in lines:
        for z in lines:
            if x != y != z and x + y + z == 2020: 
                summand1 = x
                summand2 = y
                summand3 = z
                break

print(f"Part 2 - Result: {summand1 * summand2 * summand3}")