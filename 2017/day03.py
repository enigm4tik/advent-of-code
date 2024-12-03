# Advent of Code - 2017
## Day 3

import numpy as np
import math

puzzle_input = 265149
grid_dimensions = math.ceil(math.sqrt(puzzle_input))

if grid_dimensions % 2:
    grid_dimensions += 21  # add a buffer around the value
half_point = int(grid_dimensions / 2)

grid = np.full([grid_dimensions, grid_dimensions], 0, int)
grid[half_point, half_point] = 1  # center position
new_position = (half_point, half_point + 1)
number = 2
grid[new_position] = number

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

directions_with_diagonals = {
    **directions, 'nw': (-1, -1),
    'ne': (-1, 1),
    'sw': (1, -1),
    'se': (1, 1)
}


def check_four_neighbors(array, me, get_values=False):
    neighbors = {direction: False for direction in directions.keys()}
    neighbor_values = {direction: 0 for direction in directions.keys()}
    for neighbor in directions:
        new = me[0] + directions[neighbor][0], me[1] + directions[neighbor][1]
        if array[new] != 0:
            neighbors[neighbor] = True
            neighbor_values[neighbor] = int(array[new])

    if get_values:
        return neighbor_values

    return neighbors


def find_direction_of_next_value(neighbors):
    if (neighbors['up'] == neighbors['down'] == neighbors['right'] == False
            and neighbors['left']
            == True) or (neighbors['down'] == neighbors['left'] == True
                         and neighbors['right'] == neighbors['up'] == False):
        direction = 'up'
    elif (neighbors['up'] == neighbors['left'] == neighbors['right'] == False
          and neighbors['down']
          == True) or (neighbors['down'] == neighbors['right'] == True
                       and neighbors['left'] == neighbors['up'] == False):
        direction = 'left'
    elif (neighbors['right'] == neighbors['left'] == neighbors['down'] == False
          and neighbors['up']
          == True) or (neighbors['left'] == neighbors['up'] == True
                       and neighbors['right'] == neighbors['down'] == False):
        direction = 'right'
    elif (neighbors['up'] == neighbors['left'] == neighbors['down'] == False
          and neighbors['right']
          == True) or (neighbors['up'] == neighbors['right'] == True
                       and neighbors['left'] == neighbors['down'] == False):
        direction = 'down'
    return direction


def fill_array_in_spiral(array, position, number):
    neighbors = check_four_neighbors(array, position)
    direction = find_direction_of_next_value(neighbors)
    new_position = position[0] + directions[direction][0], position[
        1] + directions[direction][1]
    array[new_position] = number + 1
    return array, number + 1, new_position


while number < puzzle_input:
    grid, number, new_position = fill_array_in_spiral(grid, new_position,
                                                      number)


def find_smallest_neighbor(value):
    my_position = np.where(grid == value)
    neighbor_values = check_four_neighbors(grid, my_position, True)
    values = []
    for value in neighbor_values.values():
        if value != 0:
            values.append(value)
    new_value = min(values)
    return new_value


value = puzzle_input
steps = 0
while value > 1:
    value = find_smallest_neighbor(value)
    steps += 1

print(f"Part 1: {steps}")


def check_eight_neighbors(array, me):
    neighbor_values = {
        direction: 0
        for direction in directions_with_diagonals.keys()
    }
    for neighbor in directions_with_diagonals:
        new = me[0] + directions_with_diagonals[neighbor][0], me[
            1] + directions_with_diagonals[neighbor][1]
        neighbor_values[neighbor] = int(array[new])

    return sum(neighbor_values.values())


def fill_array_in_spiral_with_sums(array, position):
    calculation_running = True
    neighbors = check_four_neighbors(array, position)
    direction = find_direction_of_next_value(neighbors)
    new_position = position[0] + directions[direction][0], position[
        1] + directions[direction][1]
    sum_of_neighbors = check_eight_neighbors(array, new_position)
    array[new_position] = sum_of_neighbors
    if sum_of_neighbors > puzzle_input:
        calculation_running = False
    return array, new_position, calculation_running


part2_grid = np.full([grid_dimensions, grid_dimensions], 0, int)
new_position = (half_point, half_point + 1)
part2_grid[half_point, half_point] = 1
part2_grid[new_position] = 1

calculation_running = True
while calculation_running:
    my_empty_array, new_position, calculation_running = fill_array_in_spiral_with_sums(
        part2_grid, new_position)

print(f"Part 2: {np.amax(part2_grid)}")
