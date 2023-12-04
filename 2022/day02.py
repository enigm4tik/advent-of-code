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


def determine_my_move(opponent, outcome):
    """
    Determine the move based on the opponent's move and their win condition (win, lose, draw)
    :param opponent: letter describing their move (A, B, C)
    :param win_condition: letter describing the outcome (X, Y, Z)
    :return: letter describing desired move (A, B, C)
    """
    key_list = list(conditions[moves[opponent]].keys())
    val_list = list(conditions[moves[opponent]].values())
    my_move = key_list[val_list.index(resolutions_for_opponent[outcome])]
    my_letter = list(moves.keys())[list(moves.values()).index(my_move)]
    return my_letter


def calculate_my_score(input, with_conditions=False):
    """
    Calculate player's score based on their move.
    :param input: list of moves by opponent and player
    :param with_conditions: boolean, if True consider outcome
    :return: calculated total points of player
    """
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
