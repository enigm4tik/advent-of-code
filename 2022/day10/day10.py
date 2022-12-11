# Advent of Code - 2022
## Day 10

import textwrap


def day10(read_input, part, list_of_cycles=[]):
    """
    Calculate day 10 of 2022
    :param read_input: list, read lines from input file
    :param part: int, either 1 or 2 expected (part1, vs. part2)
    :param list_of_cycles: list, optional, list of specific cycles for part 1
    :return: either dictionary of values at specific cycles OR string of '#' and '.'
    """
    current_running_program = ""
    cycle = 1
    x_position = 1
    values_at_specific_positions = {}
    screen_output = ""
    while read_input:
        current_line = read_input[0]
        if cycle in list_of_cycles:
            values_at_specific_positions[cycle] = x_position
        crt_position = (cycle % 40) - 1 if not (cycle % 40) - 1 == -1 else 39
        sprite = [crt_position - 1, crt_position, crt_position + 1]
        if x_position in sprite:
            screen_output += "#"
        else:
            screen_output += '.'
        cycle += 1
        if not current_running_program or current_running_program == "noop":
            current_running_program = current_line
            if current_running_program == "noop":
                read_input.pop(0)
            continue
        if not current_running_program == 'noop':
            inti = int(current_running_program.split(" ")[1])
            x_position += inti
        read_input.pop(0)
        current_running_program = ""
    if part == 1:
        return values_at_specific_positions
    elif part == 2:
        return screen_output


def part1(read_input):
    """
    Calculate part 1 for day 10,
    Find the signal values at specific cycles and sum up the
    signal strength: signal strength = signal value * cycle
    :param read_input: list, read lines from input file
    :return: int, sum of signal strengths
    """
    cycles = [i * 40 + 20 for i in range(6)]
    resulting_dict = day10(read_input, 1, cycles)
    sum_of_values = 0
    for signal_strength in cycles:
        sum_of_values += resulting_dict[signal_strength] * signal_strength
    return sum_of_values


def part2(read_input):
    """
    Create ascii art of part 2 of day 10
    Print the art into output, no return values
    :param read_input: list, read lines from input file
    """
    resulting_string = day10(read_input, 2)
    parts = textwrap.wrap(resulting_string, 40)
    for part in parts:
        print(part)


with open("puzzle_input") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]


print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2022 - Day 10':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1(lines.copy())}")
print("Part 2: PGHFGLUG")
part2(lines)
