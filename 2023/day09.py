# Advent of Code - 2023
## Day 9

def create_new_row(row, collected_numbers=[], first=False):
    """
    Determine the distance between two integers in a list
    Collect the last or first value (if first is True)
    If all integers are the same, return the list of all collected values.

    :param row: list of integers
    :param collected_numbers: list of integers (either first or last values)
    :param first: boolean, whether to collect first values instead of last
    :return list of collected integers
    """
    if first: 
        collected_numbers.append(row[0])
    else: 
        collected_numbers.append(row[-1])
    if len(set(row)) == 1:
        return collected_numbers
    new_row = []
    for val in range(0, len(row)-1):
        new_row.append(row[val+1] - row[val])
    return create_new_row(new_row, collected_numbers[:], first=first)


def sum_of_minuses(row):
    """
    Function to iterate over list and always subtract the difference 
    of all numbers before it from the next number (starting from the end).
    :param row: list of integers
    :return integer
    """
    current_difference = row[-1]
    for i in range(1, len(row)):
        current_difference = row[-1-i] - current_difference
    return current_difference

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

readings = []
for line in lines: 
    readings.append([int(x) for x in line.split(' ')])

part1 = 0
for reading in readings:
    res = create_new_row(reading, [])
    part1 += sum(res)

part2 = 0
for reading in readings:
    res = create_new_row(reading, [], first=True)
    part2 += sum_of_minuses(res)

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 8':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1:^55}")
print(f"Part 2: {part2:^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")
