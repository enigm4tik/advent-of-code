# Advent of Code - 2017
## Day 1

with open('2017/puzzle_input') as file:
    lines = file.readlines()

def check_digit_at(digits, digit_pos, other_digit):
    if digits[digit_pos] == digits[other_digit]:
        return int(digits[digit_pos])
    return 0
    
def part1(line):
    sum = 0
    for index, digit in enumerate(line):
        second_index = index+1
        if index == len(line)-1:
            second_index = 0
        sum += check_digit_at(line, index, second_index)
    return sum

def part2(line):
    sum = 0
    half = len(line)//2
    for index, digit in enumerate(line):
        second_index = index + half
        if second_index >= len(line):
            second_index -= len(line)
        sum += check_digit_at(line, index, second_index)

    return sum

print(f"Part 1: {part1(lines[0])}")
print(f"Part 2: {part2(lines[0])}")
