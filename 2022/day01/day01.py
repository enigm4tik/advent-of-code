# Advent of Code - 2022
## Day 1

def create_elves_calories(input_list):
    """
    Calculate the sum of all calories carried by all elves.
    :param input_list: list of numbers and blank lines
    :return: dictionary of elves and sum of calories
    """
    elves = {}
    elf_index = 0
    for line in input_list:
        if not line:
            elf_index += 1
            continue
        if elf_index not in elves:
            elves[elf_index] = []
        elves[elf_index].append(int(line))
    elves = {elf: sum(calories) for elf, calories in elves.items()}
    return elves


def find_top_x_elves(elves, amount):
    """
    Calculate the sum of the top <amount> elves in <elves>.
    :param elves: {elf: sum of calories}
    :param amount: amount of elves to consider
    :return: int <sum of top x elves' calories>
    """
    _elves = elves.copy()
    sum_of_calories = 0
    for i in range(amount):
        sum_of_calories += max(_elves.values())
        elf = max(_elves, key=elves.get)
        del _elves[elf]
    return sum_of_calories


with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    elf_calories_dictionary = create_elves_calories(lines)

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code - Day 1':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {find_top_x_elves(elf_calories_dictionary, 1)}")
print(f"Part 2: {find_top_x_elves(elf_calories_dictionary, 3)}")
