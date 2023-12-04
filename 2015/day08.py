# Advent of Code - 2015
## Day 8

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    counted_characters = [len(line.rstrip()) for line in lines]
    actual_characters = [len(line.rstrip().encode('latin1').decode('unicode-escape')) - 2 for line in lines]
    part2 = [len(line.rstrip()) + line.count('"') + line.count('\\') + 2 for line in lines]

result_part1 = sum(counted_characters) - sum(actual_characters)
result_part2 = sum(part2) - sum(counted_characters)

print(f"Part 1: {result_part1}")
print(f"Part 2: {result_part2}")