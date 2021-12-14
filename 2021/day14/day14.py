from collections import Counter

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
        if polymer_pair not in conditions:
            conditions[polymer_pair] = polymer_element

# used_polymer = {}
# # print(polymer)
# for i in range(len(polymer)):
#     if i == len(polymer)-1:
#         break
#     new_pair = polymer[i] + polymer[i+1]
#     if new_pair in used_polymer:
#         used_polymer[new_pair] += 1
#     else:
#         used_polymer[new_pair] = 1

# print(used_polymer)
# for pair in conditions:
#     print(pair, conditions[pair])


# def update_used_polymer(pair, last=False):
#     print(pair, last)
#     print(used_polymer)
#     if not last:
#         used_polymer[pair] -= 1
#         new_pair = pair[0] + conditions[pair]
#         if new_pair in used_polymer:
#             used_polymer[new_pair] += 1
#         else:
#             used_polymer[new_pair] = 1
#     else:
#         if pair in used_polymer:
#             used_polymer[pair] += 1
#         else:
#             used_polymer[pair] = 1


# def grow_one_step(polymer):
#     new_polymer = ''
#     last_character = ''
#     for index in range(len(polymer)):
#         if index == len(polymer) -1:
#             new_polymer += polymer[index]
#             return new_polymer
#         else:
#             found_pair = polymer[index] + polymer[index + 1]
#             new_polymer += polymer[index]
#             new_polymer += conditions[found_pair]
#     return polymer
#
#
# def grow_by_steps(polymer, steps):
#     if steps == 0:
#         return polymer
#     else:
#         new_polymer = grow_one_step(polymer)
#         return grow_by_steps(new_polymer, steps-1)

# polymer = 'NNCB'
# after1step = 'NBBBCNCCNBBNBNBBCHBHHBCHB'
# part3 = 'NBBBCNCCNBB'
# part4 = 'BNBNBBCHBHHBCHB'

# def calculate_element_occurence(polymer):
#     element_count = {}
#     for element in polymer:
#         if element not in element_count:
#             element_count[element] = 1
#         else:
#             element_count[element] += 1
#     return element_count
#
# new_polymer = grow_by_steps(polymer, 10)
# element_count = calculate_element_occurence(new_polymer)
# print(element_count)
#
# def calculate_most_common_minus_least_common(element_count):
#     most_common = 0
#     least_common = 10000000
#     for element_count in element_count.values():
#         if element_count > most_common:
#             most_common = element_count
#         if element_count < least_common:
#             least_common = element_count
#     return most_common - least_common

# print(calculate_most_common_minus_least_common(element_count))


# element_count = {}
#
# import re
#
# def split_polymer_in_list_of_x_length(polymer, x):
#     polymer_list = re.findall('.'*x, polymer)
#     return polymer_list
#
# polymerlist = split_polymer_in_list_of_x_length(new_polymer, len(polymer))
#
# element_occurence = {}
# element_occurence_for_chunk = {}

# def blabla(iteration=40):
#     if iteration == 0:
#         return element_occurence_for_chunk
#     for index, polymer in enumerate(polymerlist):
#         if not index == 0:
#             polymer_overlap = polymerlist[index-1][-1]
#             polymer = polymer_overlap + polymer
#         new_polymer = grow_by_steps(polymer, 10)
#         element_occurence_for_chunk.update(calculate_element_occurence(new_polymer))
#         print(calculate_element_occurence(new_polymer))
#         return blabla(iteration-5)
#
# print(blabla())


# def calculate_growth(x, iterations, y=0):
#     if iterations == 0:
#         return x, y
#     else:
#         new_x = x + (x - 1)
#         y = new_x + x
#         return calculate_growth(new_x, iterations-1, y)
#
#
# x, y = calculate_growth(2, 10)
# stringval = "x" * x
#
# import sys
# print(sys.getsizeof(stringval))
#

conditions = {}
for line in lines:
    if lines.index(line) == 0:
        polymer = line
    elif line:
        polymer_pair, polymer_element = line.split(' -> ')
        polymer_pair = (polymer_pair[0], polymer_pair[1])
        if polymer_pair not in conditions:
            conditions[polymer_pair] = polymer_element

used_polymer = {}
# print(polymer)
for i in range(len(polymer)):
    if i == len(polymer)-1:
        break
    new_pair = (polymer[i], polymer[i+1])
    if new_pair in used_polymer:
        used_polymer[new_pair] += 1
    else:
        used_polymer[new_pair] = 1
# print(conditions)
# used_in_this_round = {}
# print(f"used polymer: {used_polymer}")
# for pair in used_polymer:
#     new_pair = (conditions[pair], pair[1])
#     new_pair2 = (pair[0], conditions[pair],)
#     print(f"pair: {pair}, new pair: {new_pair}, new pair: {new_pair2}")
#     # adding the new pairs
#     if new_pair not in used_in_this_round:
#         used_in_this_round[new_pair] = 1
#     else:
#         used_in_this_round[new_pair] += 1
#     if new_pair2 not in used_in_this_round:
#         used_in_this_round[new_pair2] = 1
#     else:
#         used_in_this_round[new_pair2] += 1
#     # removing the old pair
#     if pair not in used_in_this_round:
#         used_in_this_round[pair] = -1
#     else:
#         used_in_this_round[pair] -= 1
#     print(f"used in this round: {used_in_this_round}")

print(f"used polymer: {used_polymer}")
# print(f"used in this round: {used_in_this_round}")
#
# from collections import Counter
# new_dict = Counter(used_polymer) + Counter(used_in_this_round)
# print(dict(new_dict))

def calculate_length(used_letters):
    absolute_number = 0
    for letter in used_letters:
        absolute_number += used_letters[letter]
    return absolute_number

def calculate_result(used_letters):
    min_value = min(used_letters.values())
    max_value = max(used_letters.values())
    return max_value - min_value


def propagate_one_round(used_polymer, used_letters):
    used_in_this_round = {}
    for pair, value in used_polymer.items():
        new_letter = conditions[pair]
        new_pair = (new_letter, pair[1])
        new_pair2 = (pair[0], new_letter)
        # print(new_pair, new_pair2)
        if new_letter not in used_letters:
            used_letters[new_letter] = value
        else:
            used_letters[new_letter] += value
        if new_pair not in used_in_this_round:
            used_in_this_round[new_pair] = value
        else:
            used_in_this_round[new_pair] += value
        if new_pair2 not in used_in_this_round:
            used_in_this_round[new_pair2] = value
        else:
            used_in_this_round[new_pair2] += value
        # removing the old pair
        if pair not in used_in_this_round:
            used_in_this_round[pair] = -value
        else:
            used_in_this_round[pair] -= value
    count_used_polymer = Counter(used_polymer)
    count_this_round = Counter(used_in_this_round)
    counter = count_used_polymer + count_this_round
    new_dict = dict(counter)
    return new_dict, used_letters


def propagate_x_rounds(used_polymer, rounds, used_letters):
    if rounds == 0:
        return used_letters
    new_polymer, new_letters = propagate_one_round(used_polymer, used_letters)
    return propagate_x_rounds(new_polymer, rounds-1, new_letters)

blabla = {}
for char in polymer:
    if char not in blabla:
        blabla[char] = 1
    else:
        blabla[char] += 1

my_polymer = propagate_x_rounds(used_polymer, 40, blabla)
print(calculate_result(my_polymer))

# def count_numbers(given_polymer):
#     used_elements = {}
#     for key, value in given_polymer.items():
#         element1, element2 = key
#         if element1 not in used_elements:
#             used_elements[element1] = value
#         else:
#             used_elements[element1] += value
#         if element2 not in used_elements:
#             used_elements[element2] = value
#         else:
#             used_elements[element2] += value
#     return used_elements
#
# print(count_numbers(my_polymer))