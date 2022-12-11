# Advent of Code - 2022
## Day 9

def change_input_to_one_per_row(instructions):
    """
    Parse input and split it in single instruction per line.
    eg. R 4 -> 4 lines of: R 1
    :param instructions: list, lines read from input file
    :return: list, one instruction per line
    """
    updated_instruction_list = []
    for instruction in instructions:
        direction, steps = instruction
        for i in range(int(steps)):
            updated_instruction_list.append((direction, 1))
    return updated_instruction_list


def check_if_attached(head, tail):
    """
    Check if the head is withing range (max distance of 1) and adjust position if not.
    If diagonal move diagonally towards the head, otherwise in x or y direction.
    :param head: tuple, coordinates for head
    :param tail: tuple, coordinates for tail
    :return: tuple, coordinates of updated tail
    """
    distance_x = head[0] - tail[0]
    distance_y = head[1] - tail[1]
    tail_x, tail_y = tail
    if abs(distance_x) + abs(distance_y) == 3:
        tail = tail_x + distance_x // abs(distance_x), tail_y + distance_y // abs(distance_y)
    elif abs(distance_x) > 1 or abs(distance_y) > 1:
        if distance_x:
            tail_x += distance_x // abs(distance_x)
        if distance_y:
            tail_y += distance_y // abs(distance_y)
        tail = tail_x, tail_y
    return tail


def move_head_of_rope(instruction, visited_nodes):
    """
    Move only the first element of the rope which leads to a chain reaction.
    :param visited_nodes: list, all visited nodes per element of rope
    :param instruction: str, instruction in the form of eg "R 1", direction, step
    :return: list, updated list of visited nodes
    """
    direction, _ = instruction
    tail_to_check = visited_nodes[0]["tail"][-1]
    head_x, head_y = visited_nodes[0]["head"][-1]
    head_x += movement_dict[direction][0]
    head_y += movement_dict[direction][1]
    head = (head_x, head_y)
    tail = check_if_attached(head, tail_to_check)
    visited_nodes[0]["head"].append(head)
    visited_nodes[0]["tail"].append(tail)
    return visited_nodes


def set_previous_tail_as_current_head(current_element, visited_nodes):
    """
    Set the previous element's tail as the current element's head.
    :param current_element: int, index of current element
    :param visited_nodes: list, all visited nodes per element of rope
    :return: list, updated list of visited nodes
    """
    previous_tail = visited_nodes[current_element - 1]["tail"][-1]
    visited_nodes[current_element]["head"].append(previous_tail)
    return visited_nodes


def compare_previous_tail_with_new_head(current_element, visited_nodes):
    """
    Update previous tail according to new head
    :param current_element: int, index of current element
    :param visited_nodes: list, all visited nodes per element of rope
    :return: list, updated list of visited nodes
    """
    previous_tail = visited_nodes[current_element]["tail"][-1]
    my_head = visited_nodes[current_element]["head"][-1]
    updated_tail = check_if_attached(my_head, previous_tail)
    visited_nodes[current_element]["tail"].append(updated_tail)
    return visited_nodes


def day09(instruction_list, tail_length):
    """
    Solve day 09 2022: Find the amount of visited nodes by last element of rope.
    :param instruction_list: list, read lines from input file
    :param tail_length: int, length of tail (rope consists of head and tail of length <tail_length>
    :return: int, amount of visited nodes by last element of rope
    """
    instruction_list = change_input_to_one_per_row(instruction_list)
    visible_rope_elements = []
    visited_nodes_per_rope_element = [{"head": [(250, 250)], "tail": [(250, 250)]} for i in range(tail_length)]
    i = 0
    while instruction_list:
        current_instruction = instruction_list.pop(0)
        visited_nodes_per_rope_element = move_head_of_rope(current_instruction, visited_nodes_per_rope_element)
        if 0 < i < tail_length:
            visible_rope_elements.append(i)
        for node in visible_rope_elements:
            visited_nodes_per_rope_element = set_previous_tail_as_current_head(node, visited_nodes_per_rope_element)
            visited_nodes_per_rope_element = compare_previous_tail_with_new_head(node, visited_nodes_per_rope_element)
        i += 1
    number_of_spots_visited_by_tail = len(set(visited_nodes_per_rope_element[-1]["tail"]))
    return number_of_spots_visited_by_tail


with open("puzzle_input") as file:
    lines = file.readlines()
    lines = [[line.strip() for line in line.split(" ")] for line in lines]

movement_dict = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 0),
    "D": (-1, 0)
}

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2022 - Day 9':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {day09(lines, 1)}")
print(f"Part 2: {day09(lines, 9)}")
