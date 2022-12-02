# Advent of Code - 2022
## Day 2

moves = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

win = {
    "win": 6,
    "lose": 0,
    "draw": 3
}

resolutions_for_opponent = {
    "X": win["win"],
    "Y": win["draw"],
    "Z": win["lose"]
}

conditions = {
    1: {
        1: win["draw"],
        2: win["lose"],
        3: win["win"]
    },
    2: {
        1: win["win"],
        2: win["draw"],
        3: win["lose"]
    },
    3: {
        1: win["lose"],
        2: win["win"],
        3: win["draw"]
    }
}


def determine_my_move(opponent, me):
    key_list = list(conditions[moves[opponent]].keys())
    val_list = list(conditions[moves[opponent]].values())
    my_move = key_list[val_list.index(resolutions_for_opponent[me])]
    my_letter = list(moves.keys())[list(moves.values()).index(my_move)]
    return my_letter


def calculate_my_score(input, with_conditions=False):
    total_points = 0
    for line in input:
        first, second = line
        if with_conditions:
            second = determine_my_move(first, second)
        total_points += moves[second]
        total_points += conditions[moves[second]][moves[first]]
    return total_points


with open("puzzle_input") as file:
    lines = file.readlines()
    lines = [line.strip().split(" ") for line in lines]

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2022 - Day 2':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {calculate_my_score(lines, False)}")
print(f"Part 2: {calculate_my_score(lines, True)}")
