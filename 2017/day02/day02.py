# Advent of Code - 2017
## Day 2

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.split() for line in lines]
    spreadsheet = []
    for line in lines: 
        line = [int(value) for value in line]
        spreadsheet.append(line)
    
def calculate_checksum(line):
    result = max(line) - min(line)
    return result 

result = 0
for line in spreadsheet:
    result += calculate_checksum(line)

print(f"Part 1: {result}")

def calculate_evenly_divided_checksum(line):
    result = 0
    for dividend in line:
        candidates = [divisor for divisor in line if divisor < dividend]
        for candidate in candidates: 
            if dividend % candidate == 0: 
                result += dividend / candidate
    return result

result = 0
for line in spreadsheet:
    result += calculate_evenly_divided_checksum(line)

print(f"Part 2: {int(result)}")