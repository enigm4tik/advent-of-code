# Advent of Code - 2023
## Day 1

import re

# Part 1

def find_digit_part1(line):
    """
    Find a digit by checking if it is int()able.
    :param line: string containing numbers and letetrs
    :return: found digit as string
    """
    for character in line: 
        try:
            digit = int(character)
            return character
        except ValueError:
            continue

def part1(lines):
    """
    Executing the finding of digits for a list of strings from the start, 
    then from the end.
    Adding both digits together to create a 2-digit number 
    and then add them up for all lines.
    :param lines: a list of strings
    :return: sum of all numbers found
    """
    sum = 0

    for line in lines: 
        first_digit = find_digit_part1(line)
        second_digit = find_digit_part1(line[::-1])
        number = first_digit + second_digit
        sum += int(number)
    return sum

# Part 2

# Preparation of containers
conversion = {
    'one': 1, 
    'two': 2, 
    'three': 3, 
    'four': 4,
    'five': 5,
    'six': 6, 
    'seven': 7, 
    'eight': 8,
    'nine': 9
}
    
written_digits = [digit for digit, number in conversion.items()]
actual_digits = [str(x+1) for x in range(9)]

def find_substring(line):
    """
    Find all digits that are written out in a string.
    :param line: string containing letters and numbers
    :return: list of tuples (position of match, match)
    """
    found_digits = []
    for written_digit in written_digits:
        if written_digit in line:
            for match in re.finditer(written_digit, line):
                found_digits.append((match.start(), written_digit))
    return found_digits

def find_digit_part2(line):
    """
    Find all digits in a string.
    :param line: string containing letters and numbers
    :return: list of tuples (position of match, match)
    """
    found_numbers=[]
    for actual_digit in actual_digits:
        if actual_digit in line:
            for match in re.finditer(actual_digit, line):
                found_numbers.append((match.start(), actual_digit))
    return found_numbers


def find_most_left_and_most_right_digit(line):
    """
    Find the most left and most right digit found in a string.
    :param line: string
    :return: return tuple of two digits (either word or number)
    """
    substrings = find_substring(line)
    numbers = find_digit_part2(line)
    digits = substrings + numbers
    sorted_digits = sorted(digits)
    return sorted_digits[0][1], sorted_digits[-1][1]

def convert_word_to_digit(digit):
    """
    Converts strings that represent a digit to a digit.
    :param digit: a digit representation either word or number
    :return: string
    """
    try: 
        result = int(digit)
    except ValueError:
        result = conversion[digit]
    return str(result)


def part2(lines):
    """
    Execute part two: find digits and convert them to numbers.
    Then add the numbers up - digits can be words or numbers.
    :param: list of strings
    :return: sum of found numbers
    """
    sum = 0
    for line in lines:
        first, last = find_most_left_and_most_right_digit(line)
        first_digit = convert_word_to_digit(first)
        second_digit = convert_word_to_digit(last)
        number = first_digit + second_digit
        sum += int(number)
    return sum


# with open('puzzle_input') as file:
with open('test_input', 'r') as file:
    lines = file.readlines()

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 1':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1(lines):^55}")
print(f"Part 2: {part2(lines):^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")