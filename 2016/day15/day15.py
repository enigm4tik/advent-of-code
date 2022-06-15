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
    first_position = int(split_line[-1][0])
    if not first_position == 0:
        offset = positions - first_position
    else:
        offset = disc_number
    container.append(
        {
            'disc': disc_number,
            'positions': positions,
            'offset': offset
        }
    )

for line in lines: 
    parse_line(line)

print(container)

def is_this_a_slot(time, disc):
    offset_disc_value = time + disc['disc'] - disc['offset']
    if offset_disc_value % disc['positions'] == 0:
        return True
    else:
        return False


time_slot_found = False
time = 0

while not time_slot_found:
    a = [False for i in range(len(container))]
    for i in range(len(container)):
        a[i] = is_this_a_slot(time, container[i])
    print(a)
    if all(a):
        time_slot_found = True
        print(time)
    else:
        time += 1
