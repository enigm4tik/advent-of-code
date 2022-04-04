# Advent of Code - 2016
## Day 1

from shutil import move
import numpy as np

with open('puzzle_input') as file:
    lines = file.readlines()
    directions = lines[0].split(',')
    directions = [direction.strip() for direction in directions]

vertical = 0
horizontal = 0

# directions = ['L2', 'R2', 'L2', 'L3', 'L3', 'R2', 'R4', 'R4', 'R10']
# directions = ['R8', 'R4', 'R4', 'R8']
location_storage = [vertical, horizontal]

compass_multipliers = {
    'north': {'L': -1, 'R': 1}, #vertical
    'east': {'L': 1, 'R': -1}, #horizonatl
    'south': {'L': 1, 'R': -1}, #vertical
    'west': {'L': -1, 'R': 1} #horizontal
}

direction_to_turn_to = {
    'north': {'L': 'west', 'R': 'east'},
    'east': {'L': 'north', 'R': 'south'},
    'south': {'L': 'east', 'R': 'west'},
    'west': {'L': 'south', 'R': 'north'},
}

visited_locations = []

def part1(direction, directions, iteration = 0):
    if iteration == len(directions):
        return False
    eler = directions[iteration][0]
    multiplier = compass_multipliers[direction][eler]
    movement = int(directions[iteration][1:])
    location_storage[0] += multiplier * movement
    direction = direction_to_turn_to[direction][eler]
    location_storage.reverse()
    return part1(direction, directions, iteration+1)

def part2(direction, directions, iteration = 0):
    if iteration == len(directions):
        return False
    eler = directions[iteration][0]
    multiplier = compass_multipliers[direction][eler]
    movement = int(directions[iteration][1:])
    for i in range(movement):    
        if direction in ['east', 'west']:
            visited_location = (location_storage[1], location_storage[0]+i*multiplier)
        else:
            visited_location = (location_storage[0]+i*multiplier, location_storage[1])
        if visited_location in visited_locations:
            visited_location = [abs(location) for location in visited_location]
            return sum(visited_location)
        else: 
            visited_locations.append(visited_location)
    location_storage[0] += multiplier * movement
    direction = direction_to_turn_to[direction][eler]
    location_storage.reverse()
    return part2(direction, directions, iteration+1)

part1 = part1('north', directions)
part1 = [abs(location) for location in location_storage]
print(f"Part 1: {sum(part1)}")

location_storage = [0, 0]
part2 = part2('north', directions)
print(f"Part 2: {part2}")