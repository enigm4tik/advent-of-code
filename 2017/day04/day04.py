# Advent of Code - 2017
## Day 4

from itertools import permutations

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

def determine_validity(line):
    passwords = line.split()
    set_passwords = set(passwords)

    if len(passwords) == len(set_passwords):
        return True
    else:
        return False

valid_passphrases = 0
phrases_without_duplicates = []
for line in lines:
    if determine_validity(line):
        valid_passphrases += 1
        phrases_without_duplicates.append(line)

print(f"Part 1: {valid_passphrases}")

def find_passphrases_without_anagrams(line):
    passwords = line.split()
    for word in passwords:
        word_permutations = permutations(word)
        for word_permutation in word_permutations:
            if ''.join(word_permutation) in passwords and not ''.join(word_permutation) == word:
                return False
    return True


valid_passphrases_for_part_2 = 0
for line in phrases_without_duplicates:
    if find_passphrases_without_anagrams(line):
        valid_passphrases_for_part_2 += 1

print(f"Part 2: {valid_passphrases_for_part_2}")
