# Advent of Code - 2015
## Day 1 - Part 1

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

directions = {
    '(': 1,
    ')': -1
}

amount_of_plus = lines[0].count('(')
amount_of_minus = lines[0].count(')')

print(f"Part 1 - Result: {amount_of_plus-amount_of_minus}")

## Day 1 - Part 2
floor = 0
for index, character in enumerate(lines[0]):
    floor += directions[character]
    if floor == -1:
        print(f"Part 2 - Result: {index + 1}")
        break
