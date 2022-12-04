# Advent of Code - 2022
## Day 4


def create_set_out_of_sections(section):
    """
    Helper function to create a set based on the input string
    :param section: input string in format "number-number"
    :return: set ranging from first number to last number
    """
    start, end = [int(i) for i in section.split('-')]
    created_set = set(i for i in range(start, end + 1))
    return created_set


def find_complete_overlaps(list_of_all_sections):
    """
    Iterate over all pair of sections and compare if one
    completely overlaps with the second one
    Set difference should be empty for one side
    :param list_of_all_sections: list of all sections (2 elves make up one pair)
    :return: amount of section_pairs with complete overlap
    """
    result = 0
    for section_pair in list_of_all_sections:
        first, second = section_pair
        first = create_set_out_of_sections(first)
        second = create_set_out_of_sections(second)
        if not first - second or not second - first:
            result += 1
    return result


def find_partial_overlap(list_of_all_sections):
    """
    Iterate over all pair of sections and compare if one
    partially overlaps with the second one
    Set intersection should not be empty
    :param list_of_all_sections: list of all sections (2 elves make up one pair)
    :return: amount of section_pairs with partial overlap
    """
    result = 0
    for section_pair in list_of_all_sections:
        first, second = section_pair
        first = create_set_out_of_sections(first)
        second = create_set_out_of_sections(second)
        if first & second:
            result += 1
    return result


with open("puzzle_input") as file:
    lines = file.readlines()
    lines = [line.strip().split(",") for line in lines]

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2022 - Day 4':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {find_complete_overlaps(lines)}")
print(f"Part 2: {find_partial_overlap(lines)}")
