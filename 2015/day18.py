# Advent of Code - 2015
## Day 18
from hashlib import new
import numpy as np 
np.set_printoptions(threshold=np.inf, linewidth=200)

with open("puzzle_input") as file:
# with open("test_input") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


GRID = np.empty([100, 100], int)
# GRID = np.empty([6, 6], int)


for index, line in enumerate(lines): 
    for index2, letter in enumerate(line): 
        if letter == '#':
            value = 1
        else:
            value = 0
        GRID[index][index2] = value

GRID_FOR_PART_2 = np.copy(GRID)

list_length = len(lines) - 1
SKIP_COORDINATES = [(0, 0), (0, list_length), (list_length, 0), (list_length, list_length)]

for always_on in SKIP_COORDINATES:
    GRID_FOR_PART_2[always_on] = 1

NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), 
             (1, 1), (1, -1), (1, 0), 
             (0, -1), (0, 1)]


def find_neighbors(coordinates):
    x, y = coordinates
    neighbor_coordinates = []
    for neighbor_x, neighbor_y in NEIGHBORS:
        neighbor_x += x
        neighbor_y += y 
        if any(coordinate < 0 or coordinate > len(lines)-1 for coordinate in [neighbor_x, neighbor_y]):
            continue
        neighbor_coordinates.append((neighbor_x, neighbor_y))
    return neighbor_coordinates


def calculate_amount_of_on_neighbors(neighbors, grid):
    amount_of_on = 0
    for neighbor in neighbors:
        x, y = neighbor
        amount_of_on += grid[x][y]
    return amount_of_on

def turn_lights_on_off(grid, round=100, part2=False):
    if round == 0:
        return grid
    new_grid = np.copy(grid)
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            coordinates = (i, j)
            if part2 and coordinates in SKIP_COORDINATES:
                continue
            else:
                me = grid[i][j]
                neighbors = find_neighbors((i, j))
                amount_of_on = calculate_amount_of_on_neighbors(neighbors, grid)
                if me:
                    if amount_of_on in [2, 3]:
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 0
                else:
                    if amount_of_on == 3:
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 0   
    return turn_lights_on_off(new_grid, round - 1, part2)

resulting_grid_part1 = turn_lights_on_off(GRID)
resulting_grid_part2 = turn_lights_on_off(GRID_FOR_PART_2, part2=True)

part_1 = len(resulting_grid_part1[resulting_grid_part1 == 1])
part_2 = len(resulting_grid_part2[resulting_grid_part2 == 1])

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")