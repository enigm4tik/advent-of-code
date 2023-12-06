# Advent of Code - 2023
## Day 6

def parse_lines(lines):
    """
    Parse the input into a list of integer tuples
    :param lines: string
    :return: list tuples (int, int)
    """
    time = [int(time) for time in lines[0].split(' ') if not time == '' and not time == 'Time:']
    distance = [int(time) for time in lines[1].split(' ') if not time == '' and not time == 'Distance:']

    time_distance_pairs = []
    for i in range(len(time)):
        time_distance_pairs.append((time[i], distance[i]))
    return time_distance_pairs


def part1():
    """
    Solve Part 1
    Determine amount of runs for each pair.
    Multiply all amounts
    :return: integer
    """
    time_distance_pairs = parse_lines(lines)
    best_results = {}
    for pair in time_distance_pairs:
        time, distance = pair 
        best_results[time] = 0
        for speed in range(time + 1):
            travel_distance = speed * (time - speed)
            if travel_distance > distance:
                best_results[time] += 1

    result = 1
    for value in best_results.values():
        result *= value 
    return result

def part2():
    """
    Solve Part 2
    Determine earliest and latest candidate. 
    Return amount of runs that would lead to a win.
    :return: integer
    """
    time = int(lines[0].replace(" ", "").split(":")[1])
    distance = int(lines[1].replace(" ", "").split(":")[1])

    times = 0
    for speed in range(time + 1):
        travel_distance = speed * (time - speed)
        if travel_distance > distance:
            times -= speed
            break

    for speed in range(time, 0, -1):
        travel_distance = speed * (time - speed)
        if travel_distance > distance:
            times += speed + 1
            break
    return times 

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 6':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1():^55}")
print(f"Part 2: {part2():^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")