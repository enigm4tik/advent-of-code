# Advent of Code - 2023
## Day 13

with open('input') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

patterns = []
current_pattern = []
i = 0
while lines: 
    line = lines.pop(0)
    length = len(line)
    if not line: 
        patterns.append(current_pattern)
        current_pattern = []
        i = 0
    else: 
        for character in range(length):
            if line[character] == "#":
                current_pattern.append((i, character))
        i += 1
        
def find_values(pattern, direction):
    """
    Take a list of coordinates and sort them by either
    columns or rows into a dictionary. 
    :param pattern: list of tuples (x, y)
    :param direction: string, either 'horizontal' or 'vertical'
    :return: dictionary representation of the pattern
    """
    representation = {}
    for coord in pattern:
        if direction == 'horizontal':
            x, y = coord 
        else: 
            y, x = coord
        try: 
            representation[y].append(x)
        except KeyError:
            representation[y] = [x]
    sorted_representation = dict(sorted(representation.items()))
    return sorted_representation


def recursion_part_1(representation, index, iteration=0):
    """
    Determine if all values in 2 rows or columns are equivalent. 
    Propagate until the edge of the 2d matrix. 
    :param representation: dictionary, representation of a 2D matrix
    :param index: integer, left or upper index
    :param iteration: integer, how many times recursion was observed
    :return: tuple (boolean, integer)
    """
    maximum = max(representation.keys())
    candidate1 = index - iteration
    candidate2 = index + iteration + 1
    if (candidate1 < 0 or candidate2 > maximum) and iteration != 0:
        # Out of bounds during recursion -> This is a winner
        return True, index
    elif index == max(representation.keys()):
        # Out of bounds without recursion -> Edge of the 2d matrix
        return False, index
    if representation[candidate1] == representation[candidate2]:
        # Found a candidate -> Propagation
        return recursion_part_1(representation, index, iteration + 1)
    else: 
        # Candidate was incorrect -> Abort
        return False, index


def find_row_or_col(representation, part1=True):
    """
    Determine which row is the mirror plane
    :param representation: dictionary, representation of a 2D matrix
    :param part1: boolean
    :return: tuple (boolean, integer)
    """
    found = False
    for i in representation.keys(): 
        if not part1: 
            found, result = recursion_part_2(representation, i)
        else:
            found, result = recursion_part_1(representation, i)
        if found: 
            break 
    return found, result


def recursion_part_2(representation, index, iteration=0, found=False):
    """
    Basically part1 with one more condition to check
    :param representation: dictionary, representation of a 2D matrix
    :param index: integer, left or upper index
    :param iteration: integer, how many times recursion was observed
    :return: tuple (boolean, integer)
    """
    maximum = max(representation.keys())
    candidate1 = index - iteration
    candidate2 = index + iteration + 1
    if (candidate1 < 0 or candidate2 > maximum) and iteration != 0:
        # Out of bounds during recursion 
        if not found:
            # We found the one from part 1
            return False, index
        else:
            # We found the one from part 2!
            return True, index
    elif index == max(representation.keys()):
        # Out of bounds without recursion -> Edge of the 2d matrix
        return False, index
    if representation[candidate1] == representation[candidate2]:
        # Found a candidate -> Propagation
        return recursion_part_2(representation, index, iteration + 1, found)
    elif not found: 
        # Smudge detection
        missing_element = set(representation[candidate1]) ^ set(representation[candidate2])
        if len(missing_element) == 1 and not found:
            # Found a candidate -> Propagation
            found = True
            return recursion_part_2(representation, index, iteration + 1, found)
        else: 
            # This candidate will not even work in part 2
            return False, index
    else: 
        # Candidate was incorrect -> Abort
        return False, index


def calculate_pattern_sum(patterns, part1):
    """
    Calculate the sum of the pattern by: 
    adding up all columns left of the vertical lines found and
    adding up all rows above the horizontal lines found (*100)
    :param patterns: list of list of tuples (x, y)
    :param part1: boolean 
    """
    pattern_sum = 0
    for pattern in patterns:
        horizontal = find_values(pattern, 'horizontal')
        vertical = find_values(pattern, 'vertical')
        horizontal, result = find_row_or_col(horizontal, part1)
        vertical, result1 = find_row_or_col(vertical, part1)
        if horizontal: 
            pattern_sum += result + 1
        if vertical:
            pattern_sum += (result1 + 1) * 100
    return pattern_sum

part1 = calculate_pattern_sum(patterns, True)
part2 = calculate_pattern_sum(patterns, False)

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 13':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1:^55}")
print(f"Part 2: {part2:^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")