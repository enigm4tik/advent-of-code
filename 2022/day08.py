# Advent of Code - 2022
## Day 8

import numpy as np


def part1(grid):
    """
    Solve part 1 of day 08 2022
    How many trees are visible in the given grid
    :param grid: numpy array, based on input grid
    :return: int, amount of total_visible_trees
    """
    result_grid = visible_trees(grid)
    total_visible_trees = len(result_grid[result_grid > 0])
    return total_visible_trees


def visible_trees(grid):
    """
    Calculate the visibility for each tree.
    Maximum visibility is 4, anytime a tree cannot be seen from one direction
    visibility is decreased by 1.
    :param grid: numpy array, based on input file
    :return: numpy array, containing visibility per tree
    """
    result_grid = grid.copy()
    x, y = grid.shape
    for i in range(x):
        for j in range(y):
            if i == 0 or i == x - 1:
                visibility = 4
            elif j == 0 or j == y - 1:
                visibility = 4
            else:
                visibility = calculate_visibility(grid, (i, j))
            result_grid[i][j] = visibility
    return result_grid


def calculate_visibility(grid, tree):
    """
    Calculate visibility for one tree in a grid
    :param grid: numpy array, based on input file
    :param tree: tuple, coordinates of a tree
    :return: int, calculated visibility (0-4)
    """
    visibility = 4
    list_of_views = get_view_of_tree(grid, tree)
    tree = grid[tree]
    for view in list_of_views:
        if any((tree - view) < 1):
            visibility -= 1
    return visibility


def get_view_of_tree(grid, tree):
    """
    Find all 4 sub arrays for a tree
    :param grid: numpy array, based on input
    :param tree: tuple, coordinates of tree
    :return list, list of 4 sub arrays
    """
    x, y = tree
    view_left = grid[x, 0:y]
    view_right = grid[x, y + 1:]
    view_top = grid[:x, y]
    view_bottom = grid[x + 1:, y]
    list_of_views = [view_left, view_right, view_top, view_bottom]
    return list_of_views


def part2(grid):
    """
    Solve part 2 of day 08 2022
    Calculate the best visibility score (product of all visibilities)
    :param grid: numpy array, based on input
    :return: int, best calculated visibility score
    """
    result = update_grid_with_visibility_scores(grid)
    best_visibility_score = np.max(result)
    return best_visibility_score


def update_grid_with_visibility_scores(grid):
    """
    Calculate the visibility score for each tree
    :param grid: numpy array, based on input
    :return: numpy array, with visibility score
    """
    result_grid = grid.copy()
    x, y = grid.shape
    for i in range(x):
        for j in range(y):
            visibility_score_for_tree = calculate_visibility_score(grid, (i, j))
            result_grid[i, j] = visibility_score_for_tree
    return result_grid


def calculate_visibility_score(grid, tree):
    """
    Calculate the visibility score for each tree
    :param grid: numpy array, based on input
    :param tree: tuple, coordinates for a tree
    :return: int, visibility score = product of distances
    """
    list_of_views = get_view_of_tree(grid, tree)
    list_of_views = [list(list_of_views[0])[::-1], list(list_of_views[1]), list(list_of_views[2])[::-1],
                     list(list_of_views[3])]
    tree = grid[tree]
    distances = []
    for index, view in enumerate(list_of_views):
        current_distance = 0
        for tree_in_sight in view:
            current_distance += 1
            if tree_in_sight >= tree:
                break
        distances.append(current_distance)
        visibility_score = np.product(distances)
    return visibility_score


with open("puzzle_input") as file:
    lines = file.readlines()
    lines = [[int(line[i]) for i in range(len(line.strip()))] for line in lines]

array = np.array(lines)

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2022 - Day 8':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1(array)}")
print(f"Part 2: {part2(array)}")
