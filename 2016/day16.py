# Advent of Code - 2016
## Day 16

#puzzle_input = "110010110100"
puzzle_input = "01111001100111011"

def create_dragon_curve(input):
    a = input
    b = input[::-1]
    b = b.replace('0', '2')
    b = b.replace('1', '0')
    b = b.replace('2', '1')
    result = a + '0' + b
    return result 

def create_check_sum(input):
    check_pairs = [input[i: i + 2] for i in range(0, len(input), 2)]
    result = ''
    for pair in check_pairs:
        if pair[0] == pair[1]:
            result += "1"
        else:
            result += "0"
    return result 

def find_valid_checksum(input):
    check_sum = create_check_sum(input)
    if len(check_sum) % 2:
        return check_sum
    else:
        return find_valid_checksum(check_sum)

required_length = 272
while len(puzzle_input) < required_length:
    puzzle_input = create_dragon_curve(puzzle_input)
part1 = find_valid_checksum(puzzle_input[:required_length])
print(f"Part 1: {part1}")

required_length = 35651584
while len(puzzle_input) < required_length:
    puzzle_input = create_dragon_curve(puzzle_input)
part2 = find_valid_checksum(puzzle_input[:required_length])
print(f"Part 2: {part2}")
