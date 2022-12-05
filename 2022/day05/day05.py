# Advent of Code - 2022
## Day 5

import textwrap


def parse_input(read_lines):
    """
    Parse the <read_lines> containing a "visual" graph of stacks and lines of instructions.
    Convert it to a nested list of letters for the stack part
    [['A'], ['B', 'C'], ['D', 'E', 'F'], ...]
    and a list of dictionaries containing information on the movement:
    [{"move": 2, "from": 1, "to": 2}, ...]
    :param read_lines: lines read from the input file
    :return: instruction dictionary and nested list of stacks
    """
    instructions = []
    towers = []
    for line in read_lines:
        if not line.startswith("move"):
            tower = textwrap.wrap(line, 4, drop_whitespace=False)
            towers.append([stripped_tower.strip() for stripped_tower in tower])
        else:
            move, amount, before, source, after, destination = line.split(" ")
            instructions.append({move: int(amount), before: int(source), after: int(destination.strip())})

    stacks_dict = {}
    for tower in towers:
        for index, value in enumerate(tower):
            if value and value != ",":
                if index not in stacks_dict:
                    stacks_dict[index] = [value]
                else:
                    stacks_dict[index].insert(0, value)

    stacks = []
    tower_amount = int(len(read_lines[0]) / 4)
    for i in range(tower_amount):
        new_stack = [stack.strip('[').strip(']') for stack in stacks_dict[i] if stack.startswith("[")]
        stacks.append(new_stack)
    return instructions, stacks


def move_one_at_a_time(instructions, stacks):
    """
    Follow <instructions> and move the last added element in a <stack> onto another <stack>. (FIFO queue)
    :param instructions: list of dictionaries with instructions
    [{"move": 2, "from": 1, "to": 2}, ...]
    :param stacks: nested list of stacks
    [['A'], ['B', 'C'], ['D', 'E', 'F'], ...]
    :return: string, containing last element of all stacks
    """
    for instruction in instructions:
        moving = 0
        while moving < instruction["move"]:
            popped = stacks[instruction["from"] - 1].pop()
            stacks[instruction["to"] - 1].append(popped)
            moving += 1
    string_to_return = "".join([stack[-1] for stack in stacks])
    return string_to_return


def move_substack_at_a_time(instructions, stacks):
    """
    Follow <instructions> and move multiple elements in a <stack> onto another <stack>.
    :param instructions: list of dictionaries with instructions
    [{"move": 2, "from": 1, "to": 2}, ...]
    :param stacks: nested list of stacks
    [['A'], ['B', 'C'], ['D', 'E', 'F'], ...]
    :return: string, containing last element of all stacks
    """
    for instruction in instructions:
        popped_list = []
        moving = 0
        while moving < instruction["move"]:
            popped = stacks[instruction["from"] - 1].pop()
            popped_list.append(popped)
            moving += 1
        else:
            for i in range(len(popped_list)):
                stacks[instruction["to"] - 1].append(popped_list.pop())
    string_to_return = "".join([stack[-1] for stack in stacks])
    return string_to_return


with open("puzzle_input") as file:
    lines = file.readlines()
    lines = [line for line in lines]

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2022 - Day 5':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {move_one_at_a_time(*parse_input(lines))}")
print(f"Part 2: {move_substack_at_a_time(*parse_input(lines))}")
