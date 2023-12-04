# Advent of Code - 2016
## Day 12

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

registers = {letter: 0 for letter in ['a', 'b', 'c', 'd']}
registers_part_2 = {letter: 0 for letter in ['a', 'b', 'c', 'd']}
registers_part_2['c'] = 1

def parse_line(loop_index, used_dictionary=registers):
    line = lines[loop_index]
    instruction, *values = line.split()
    if not instruction == 'jnz':
        loop_index += 1
    if instruction == 'cpy':
        execute_cpy(values, used_dictionary)
    elif instruction == 'inc':
        execute_inc(values, used_dictionary)
    elif instruction == 'dec':
        execute_dec(values, used_dictionary)
    elif instruction == 'jnz':
        loop_index = execute_jnz(values, loop_index, used_dictionary)
    return loop_index


def execute_cpy(values, used_dictionary=registers):
    try:
        assign_value = int(values[0])
    except ValueError:
        assign_value = used_dictionary[values[0]]
    used_dictionary[values[1]] = assign_value


def execute_inc(register, used_dictionary=registers):
    used_dictionary[register[0]] += 1


def execute_dec(register, used_dictionary=registers):
    used_dictionary[register[0]] -= 1


def execute_jnz(values, loop_index, used_dictionary=registers):
    try: 
        register_value = int(values[0])
    except ValueError:
        register_value = used_dictionary[values[0]]
    if not register_value == 0:
        loop_index += int(values[1])
    else:
        loop_index += 1
    return loop_index

loop_index = 0
while loop_index < len(lines):
    loop_index = parse_line(loop_index)

loop_index = 0
while loop_index < len(lines):
    loop_index = parse_line(loop_index, used_dictionary=registers_part_2)

print(f"Part 1: {registers['a']}")
print(f"Part 2: {registers_part_2['a']}")
