# Advent of Code - 2015
## Day 2 - Part 1

with open('puzzle_input', 'r') as file:
# with open('test_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def calculate_paper_needed(dimensions):
    length, width, height = dimensions.strip().split('x')
    length, width, height = intify_a_string(length), intify_a_string(width), intify_a_string(height)
    sides= [length*width, width*height, length*height]
    paper_needed = 2*(sum(sides)) + min(sides)
    return paper_needed

def intify_a_string(string):
    return int(string)

sum_of_paper = 0
for line in lines: 
    sum_of_paper += calculate_paper_needed(line)

print(f"Part 1 - Result: {sum_of_paper}")

## Day 2 - Part 2

def calculate_ribbon_needed(dimensions):
    return get_perimeter(dimensions) + get_volume(dimensions)

def turn_dimensions_into_list(dimensions):
    dimension_list = dimensions.strip().split('x')
    dimension_list = [intify_a_string(value) for value in dimension_list]
    return dimension_list

def get_perimeter(dimensions):
    dimension_list = turn_dimensions_into_list(dimensions)
    dimension_list.sort()
    perimeter = 2*(dimension_list[0] + dimension_list[1])
    return perimeter

def get_volume(dimensions):
    dimension_list = turn_dimensions_into_list(dimensions)
    volume = 1
    for dimension in dimension_list:
        volume *= dimension
    return volume

ribbon_needed = 0
for line in lines: 
    ribbon_needed += calculate_ribbon_needed(line)

print(f"Part 2 - Result: {ribbon_needed}")
