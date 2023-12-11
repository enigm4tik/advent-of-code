import numpy as np
import itertools

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def setup_numpy_array(lines):
    """
    Create a numpy array from a list of strings
    :param lines: list of strings
    :return: numpy array
    """
    array = np.empty([len(lines), len(lines[0])], str)
    for index, line in enumerate(lines):
        for v_index, input in enumerate(line): 
            array[index, v_index] = input
    return array

def find_empty_space(array):
    """
    Find rows and columns that have all '.' = empty space 
    :param array: numpy array
    :return: tuple (empty_rows, empty_cols)
    """
    empty_rows = list(zip(*np.where(np.all(array=='.', axis=1))))
    empty_rows = [empty[0] for empty in empty_rows]
    empty_cols = list(zip(*np.where(np.all(array==".", axis=0))))
    empty_cols = [empty[0] for empty in empty_cols]
    return empty_rows, empty_cols


def get_shortest_distance(galaxy1, galaxy2, years, empty_rows, empty_cols):
    """
    Calculate Manhattan Distance for two coordinates based on
    years of expansion 
    :param galaxy1: tuple (v, h)
    :param galaxy2: tuple (v, h)
    :param years: integer, years the galaxy aged
    :param empty_rows: list [row ids]
    :param empty_cols: list [col ids]
    :return: integer, Manhattan distance
    """
    g1_h, g1_v = galaxy1
    g2_h, g2_v = galaxy2
    shortest_h = abs(g2_h-g1_h)
    shortest_v = abs(g1_v-g2_v)

    empty_rows_traveled = len(set([i for i in range(min(g1_h, g2_h), max(g1_h, g2_h))]) & set(empty_rows))
    shortest_h += years * empty_rows_traveled
    empty_cols_traveled = len(set([i for i in range(min(g1_v, g2_v), max(g1_v, g2_v))]) & set(empty_cols))
    shortest_v += years * empty_cols_traveled

    shortest_distance = shortest_h + shortest_v
    return shortest_distance


def calculate_sum_of_shortest_paths(array, years):
    """
    Calculate the sum of all shortest paths in a galaxy.
    :param array: numpy array
    :param years: integer, years that passed
    :return: integer, sum of all shortest distances
    """
    position_of_galaxies =  list(zip(*np.where(array == "#")))
    combinations = itertools.combinations(position_of_galaxies, 2)
    empty_rows, empty_cols = find_empty_space(array)
    distance = 0
    for combination in combinations: 
        galaxy1, galaxy2 = combination
        calculated_distance = get_shortest_distance(galaxy1, galaxy2, years, empty_rows, empty_cols)
        distance += calculated_distance
    return distance

array = setup_numpy_array(lines)
part1 = calculate_sum_of_shortest_paths(array, 1)
part2 = calculate_sum_of_shortest_paths(array, 999999)

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 10':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1:^55}")
print(f"Part 2: {part2:^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")
