# Advent of Code - 2021
## Day 1 - Part 1

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

previous = 0
count = 0

for line in lines:
    if lines.index(line) == 0:
        continue
    else:
        if line > previous:
            count += 1
    previous = line

print(f"Part 1 - Result: {count}")

## Day 1 - Part 2

previous_sum = 0
count2 = 0

for index, line in enumerate(lines):
    if index >= len(lines) - 2:
        continue
    else:
        current_sum = lines[index] + lines[index + 1] + lines[index + 2]
        if current_sum > previous_sum:
            count2 += 1
        previous_sum = current_sum

print(f"Part 2 - Result: {count2 - 1}")  # because the first comparison is comparing against 0