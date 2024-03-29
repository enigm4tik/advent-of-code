# Advent of Code - 2022
## Day 3

def calculate_priority(item_type):
    """
    Calculate the priority score for each letter.
    Score[a-z] = 1-26
    Score[A-Z] = 27-52
    :param item_type: one letter string
    :return: Calculated score
    """
    adjustment = 96
    unicode_value = ord(item_type)
    if unicode_value < 97:
        adjustment = 38
    return unicode_value - adjustment


def calculate_sum_of_priorities(item_list):
    """
    Calculate sum of priorities per backpack
    Each backpack has 2 equal sized compartment (split list in half)
    :param item_list: list of all backpacks
    :return: sum of all calculated priorities
    """
    result = 0
    for item in item_list:
        compartment1, compartment2 = set(item[:len(item) // 2]), set(item[len(item) // 2:])
        found_element = list(compartment1 & compartment2)[0]
        result += calculate_priority(found_element)
    return result


def calculate_sum_of_priorties_part_2(item_list):
    """
    Calculate the sum of priorities over 3 backpacks
    :param item_list: list of all backpacks
    :return: sum of all priorities calculated for groups of 3
    """
    result = 0
    one_third_length = int(len(item_list) / 3)
    for i in range(one_third_length):
        backpack1, backpack2, backpack3 = item_list[i*3 : i*3 + 3]
        group_badge = list(set(set(backpack1) & set(backpack2)) & set(backpack3))[0]
        result += calculate_priority(group_badge)
    return result


with open("puzzle_input") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2022 - Day 3':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {calculate_sum_of_priorities(lines)}")
print(f"Part 2: {calculate_sum_of_priorties_part_2(lines)}")
