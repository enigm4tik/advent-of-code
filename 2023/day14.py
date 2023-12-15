# Advent of Code - 2023
## Day 14

with open('input') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def move_one_column_north(values, blockers):
    """
    Move values north until they hit a blocker or the end
    :param values: list of integers
    :param blocker: list of integers
    return: list of integers
    """
    evaluated_values = []
    for value in values:
        current_blockers = [i for i in blockers if i < value]
        if not current_blockers: 
            max_blocker = 0
        else: 
            if evaluated_values: 
                max_blocker = max(evaluated_values[-1], *current_blockers)
            else: 
                max_blocker = max(current_blockers)
        start = min([value, max_blocker])
        evaluated_value = min([i for i in range(start, value + 1) 
                                    if i not in evaluated_values and i not in blockers])
        evaluated_values.append(evaluated_value)
    return evaluated_values


def rotate(coordinates, length=9):
    """
    Rotate coordinates in a 2D matrix clock-wise:
    old y values become new x values 
    new y values are calulated by length - old x values
    :param coordinates: list of tuples (x, y)
    :return: list of tuples (x, y)
    """
    coordinates = [(y, length-x) for x, y in coordinates]
    return sorted(coordinates)


def move_one_step(circles, squares, columns):
    """
    Use the coordinates of circles and squares to determine 
    the evaluated coordinates. 
    Circles move until they hit a square or the bounds of the matrix.
    :param circles: list of tuples (x, y)
    :param squares: list of tuples (x, y)
    :param columns: integer, amount of columns
    """
    new_circles = []
    for i in range(columns):
        values = [j[0] for j in circles if j[1] == i]
        blocker = [j[0] for j in squares if j[1] == i]
        north = move_one_column_north(values, blocker)
        for k in north:
            new_circles.append((k, i))
    return new_circles, squares 


def rotate_after_step(circles, squares, columns):
    """
    Rotate circles and squares for the next step.
    :param circles: list of tuples (x, y)
    :param squares: list of tuples (x, y)
    :param columns: integer, amount of columns
    :return: tuple (list of tuples, list of tuples)
    """
    adjusted_length = columns - 1
    circles = rotate(circles, adjusted_length)
    squares = rotate(squares, adjusted_length)
    return circles, squares


def get_north_support_beams(list_of_stones, rows):
    """
    Calculate the load on north support beams: 
    from top to bottom in 2D matrix decrease the value, 
    amount of circles in each row * value
    example:
    O...O < row 1 (value = rows) -> 20
    ...O. < row 2 (value = rows -1) -> 19
    -> sum up all values 
    :param list_of_stones: list of tuples (x, y)
    :param rows: amount of rows
    :return: integer sum of load for each row
    """
    list_of_stones = [i for i, j in list_of_stones]
    temporary_dictionary = {}
    for i in list_of_stones:
        try: 
            temporary_dictionary[rows-i] += 1
        except KeyError: 
            temporary_dictionary[rows-i] = 1
    result = 0
    for key, value in temporary_dictionary.items():
        result += key * value 
    return result

circles = []
squares = []
for x in range(len(lines)): 
    for y in range(len(lines[0])):
        if lines[x][y] == "O":
            circles.append((x, y))
        if lines[x][y] == "#":
            squares.append((x, y))

seen_circles = [circles]
big_number = 1000000000
loop_found = False
i = 0
while not loop_found and i < big_number: 
    for j in range(4):
        circles, squares = move_one_step(circles, squares, len(lines[0]))
        if i == 0 and j == 0:
            #part 1: move once north 
            part1 = get_north_support_beams(circles, len(lines))
        circles, squares = rotate_after_step(circles, squares, len(lines[0]))
    if not circles in seen_circles:
        seen_circles.append(circles)
    else: 
        repeater = seen_circles.index(circles)
        loop_found = True
        cycle_length = i-seen_circles.index(circles)
        first_repeat = i
        loop_found = True
    i+= 1

for i in range(1, 2000):
    bla = (big_number - i*(repeater+1)) % cycle_length
    if bla != 0:
        break
part2 = get_north_support_beams(seen_circles[bla + repeater +1], len(lines))

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 14':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1:^55}")
print(f"Part 2: {part2:^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")
