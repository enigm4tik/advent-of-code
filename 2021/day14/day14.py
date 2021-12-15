from collections import Counter
import sys

with open('puzzle_input', 'r') as file:
# with open('test_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

polymer = ''
conditions = {}
for line in lines:
    if lines.index(line) == 0:
        polymer = line
    elif line:
        polymer_pair, polymer_element = line.split(' -> ')
        polymer_pair = (polymer_pair[0], polymer_pair[1])
        if polymer_pair not in conditions:
            conditions[polymer_pair] = polymer_element

initial_polymer = {}

for i in range(len(polymer)):
    if i == len(polymer)-1:
        break
    new_pair = (polymer[i], polymer[i+1])
    if new_pair in initial_polymer:
        initial_polymer[new_pair] += 1
    else:
        initial_polymer[new_pair] = 1


def calculate_length(used_letters):
    """ Helper function to determine if my polymer has the right length after polymerization """
    absolute_number = 0
    for letter in used_letters:
        absolute_number += used_letters[letter]
    return absolute_number


def calculate_growth(string_length, iterations):
    """  Helper function to create a polymer of length string_length after iterations iterations """
    if iterations == 0:
        return string_length
    else:
        new_x = string_length + (string_length - 1)
        return calculate_growth(new_x, iterations-1)


x = calculate_growth(2, 10)
calculated_string = "x" * x
print(sys.getsizeof(calculated_string))

def calculate_result(used_letters):
    min_value = min(used_letters.values())
    max_value = max(used_letters.values())
    return max_value - min_value


def propagate_one_round(polymer, used_letters):
    used_in_this_round = {}
    for pair, amount in polymer.items():
        new_letter = conditions[pair]
        pair_left = (new_letter, pair[1])
        pair_right = (pair[0], new_letter)

        if new_letter not in used_letters:
            used_letters[new_letter] = amount
        else:
            used_letters[new_letter] += amount
        if pair_left not in used_in_this_round:
            used_in_this_round[pair_left] = amount
        else:
            used_in_this_round[pair_left] += amount
        if pair_right not in used_in_this_round:
            used_in_this_round[pair_right] = amount
        else:
            used_in_this_round[pair_right] += amount

        if pair not in used_in_this_round:
            used_in_this_round[pair] = -amount
        else:
            used_in_this_round[pair] -= amount
    count_used_polymer = Counter(polymer)
    count_this_round = Counter(used_in_this_round)
    counter = count_used_polymer + count_this_round
    new_dict = dict(counter)
    return new_dict, used_letters


def propagate_x_rounds(polymer, rounds, used_letters):
    if rounds == 0:
        return used_letters
    new_polymer, new_letters = propagate_one_round(polymer, used_letters)
    return propagate_x_rounds(new_polymer, rounds-1, new_letters)


initially_used_elements = {}
for char in polymer:
    if char not in initially_used_elements:
        initially_used_elements[char] = 1
    else:
        initially_used_elements[char] += 1

my_polymer = propagate_x_rounds(initial_polymer, 40, initially_used_elements)
print(calculate_result(my_polymer))
