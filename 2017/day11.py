# Advent of Code - 2017
## Day 11

with open('puzzle_input') as file:
    lines = file.readlines()
    lines = lines[0].split(',')


def count_directions(input):
    directions = ['se', 'sw', 's', 'ne', 'nw', 'n']
    amounts = {direction: input.count(direction) for direction in directions}
    return amounts


def remove_non_movement(amounts):
    opposites = {'n': 's', 'nw': 'se', 'sw': 'ne'}
    calculated_amounts = {}
    for direction_1, direction_2 in opposites.items():
        calculated_amounts[direction_1] = amounts[direction_1] - amounts[
            direction_2] if amounts[direction_1] - amounts[
                direction_2] > 0 else 0
        calculated_amounts[direction_2] = amounts[direction_2] - amounts[
            direction_1] if amounts[direction_2] - amounts[
                direction_1] > 0 else 0
    return calculated_amounts


def switch_movements(amounts):
    combined_movements = {
        'se': ['ne', 's'],
        's': ['sw', 'se'],
        'sw': ['nw', 's'],
        'nw': ['n', 'sw'],
        'n': ['ne', 'nw'],
        'ne': ['n', 'se']
    }
    non_zero_directions = [
        direction for direction in amounts if amounts[direction] != 0
    ]
    for direction, movement in combined_movements.items():
        new_list = non_zero_directions + movement
        if len(set(new_list)) == 3:
            combined_movement = min(amounts[movement[0]], amounts[movement[1]])
            amounts[direction] += combined_movement
            amounts[movement[0]] -= combined_movement
            amounts[movement[1]] -= combined_movement

    return sum([value for value in amounts.values()])

def solution(input):
  amounts = count_directions(input)
  amounts = remove_non_movement(amounts)
  amounts = switch_movements(amounts)
  return amounts

print(f"Part 1: {solution(lines)}")

max_witnessed = 0
for i in range(len(lines)):
  result = solution(lines[0:i])
  if result > max_witnessed:
    max_witnessed = result

print(f"Part 2: {max_witnessed}")