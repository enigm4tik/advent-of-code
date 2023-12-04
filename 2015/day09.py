# Advent of Code - 2015
## Day 9

from itertools import permutations

distances = {}
with open('puzzle_input', 'r') as file: 
    lines = file.readlines()
    input = [str(line.rstrip()) for line in lines]

for line in input:
    destination1, to, destination2, equals, distance = line.split(" ")
    if not destination1 in distances:
        distances[destination1] = {destination2: int(distance)}
    else: 
        distances[destination1][destination2] = int(distance)
    if not destination2 in distances:
        distances[destination2] = {destination1: int(distance)}
    else: 
        distances[destination2][destination1] = int(distance)

all_cities = distances.keys()
all_possible_paths = permutations(all_cities)
cities = []
for city in all_possible_paths: 
    reverse_path = city[::-1]
    if not reverse_path in cities: 
        cities.append(city)

def calculate_distance(path):
    distance = 0
    for index, city in enumerate(path): 
        if index == 0:
            continue
        else: 
            distance += distances[path[index-1]][city]
    return distance

smallest_number = 100000000
biggest_number = 0
for path in cities: 
    distance = calculate_distance(path)
    if distance < smallest_number:
        smallest_number = distance
    if distance > biggest_number: 
        biggest_number = distance

print(f"Part 1: {smallest_number}")
print(f"Part 2: {biggest_number}")