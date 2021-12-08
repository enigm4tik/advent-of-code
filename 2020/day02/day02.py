# Advent of Code - 2020
## Day 2 - Part 1

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

valid_passwords = 0

for line in lines: 
    times, required_letter, phrase = line.split(' ')
    min, max = times.split('-')
    min = int(min)
    max = int(max)
    required_letter = required_letter[:-1]
    
    found_times = 0
    for letter in phrase: 
        if required_letter == letter:
            found_times += 1
        else:
            continue
    if found_times <= max and found_times >= min: 
        valid_passwords += 1

print(f"Part 1 - Result: {valid_passwords}")

## Day 2 - Part 2

valid_passwords = 0

for line in lines: 
    times, required_letter, phrase = line.split(' ')
    min, max = times.split('-')
    min = int(min) - 1
    max = int(max) - 1
    required_letter = required_letter[:-1]
    try: 
        first = phrase[min]
        second = phrase[max]
    except IndexError:
        continue
    if first == second:
        continue
    if first != second:
        if first == required_letter:
            valid_passwords += 1
        if second == required_letter: 
            valid_passwords += 1

print(f"Part 2 - Result: {valid_passwords}")
