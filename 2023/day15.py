# Advent of Code - 2023
## Day 15

with open('input') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

initialization_sequence = lines[0].split(',')

def hash_algorithm(given_string):
    """
    Implement a hash algorithm with these steps: 
    1) Determine the ASCII code of a character
    2) Add the code to the current hash value (start with 0)
    3) Multiply the current hash value by 17
    4) Hash value is the remainder of dividing by 256 (% 256)
    5) Continue with the next character at 1)
    :param given_string: string to hash 
    :return: integer, calculated hash value
    """
    hash_value = 0
    for character in given_string:
        ascii_value = ord(character)
        hash_value += ascii_value
        hash_value *= 17
        hash_value = hash_value % 256
    return hash_value


def get_focus_power(slot, lens):
    """
    Calculate the focus length by these rules: 
    Focus power = hash value of label * focal length * slot 
    :param lens: tuple (label, focal_length)
    :param slot: integer
    :return: calculated focus power for one lens
    """
    label, focal = lens
    box = 1 + hash_algorithm(label)
    slot += 1
    focus_power = box * slot * focal
    return focus_power

part1 = 0
for step in initialization_sequence: 
    part1 += hash_algorithm(step)

hashmap = {i: {} for i in range(256)}

for step in initialization_sequence:
    if "-" in step:
        # remove if exists
        label, _ = step.split("-")
        box = hash_algorithm(label)
        found_labels = set([i for i in hashmap[box].keys()])
        if label in found_labels:
            del hashmap[box][label]
    if "=" in step: 
        # add a lens or replace 
        label, focus = step.split("=")
        focus = int(focus)
        box = hash_algorithm(label)
        found_labels = set([i for i in hashmap[box].keys()])
        if label in found_labels:
            hashmap[box][label] = focus
            pass
        else: 
            hashmap[box][label] = focus

part2 = 0
for box, contents in hashmap.items():
    for slot, lens in enumerate(contents.items()):
        part2 += get_focus_power(slot, lens)

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 15':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1:^55}")
print(f"Part 2: {part2:^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")
