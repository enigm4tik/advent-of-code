# Advent of Code - 2016
## Day 15

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

container = []

def parse_line(line):
    split_line = line.split(' ')
    disc_number = split_line[1]
    disc_number = int(split_line[1][1:])
    positions = int(split_line[3])
    first_position = int(split_line[-1][:-1])
    offset = positions - first_position
    container.append(
        {
            'disc': disc_number,
            'positions': positions,
            'offset': offset
        }
    )

for line in lines: 
    parse_line(line)

def is_this_a_valid_slot(time, disc):
    offset_disc_value = time + disc['disc'] - disc['offset']
    if offset_disc_value % disc['positions'] == 0:
        return True
    else:
        return False

def find_correct_time_slot(container):
    time = 0
    while True:
        results = [False for i in range(len(container))]
        for i in range(len(container)):
            results[i] = is_this_a_valid_slot(time, container[1])
        if all(results):
            return time
        else:
            time += 1

part1 = find_correct_time_slot(container)
print(f"Part 1: {part1})

# Parse additional line (adding a disc)
parse_line("Disc #7 has 11 positions; at time=0, it is at positions 0."
part2 = find_correct_time_slot(container)
print(f"Part 2: {part2})