# Advent of Code - 2017
## Day 5

with open('puzzle_input') as file:
#with open('test_input') as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]
  lines = [int(line) for line in lines]

part1_input = lines[::]
part2_input = lines[::]
  
def adjust_offset(offset, part2=False):
  if part2: 
    if offset >= 3:
      offset -= 1
    else:
      offset += 1
  else:
      offset += 1
  return offset

def jump_according_to_offset(current_position, offset):
  new_position = current_position + offset
  return new_position

def check_for_exit(new_position, check_list):
  if new_position < 0 or new_position > len(check_list) -1:
    return False
  else:
    return True

def move_one_step_according_to_instructions(instructions, current_position, part2=False):
  current_offset = instructions[current_position]
  new_position = jump_according_to_offset(current_position, current_offset)
  instructions[current_position] = adjust_offset(instructions[current_position], part2)
  return new_position, instructions

def day_05(check_value, part2=False):
  valid_jumps = 0
  while check_for_exit(check_value[0], check_value[1]):
    check_value[0], check_value[1] = move_one_step_according_to_instructions(check_value[1], check_value[0], part2)
    valid_jumps += 1

  return valid_jumps

print(f"Part 1: {day_05([0, part1_input])}")
print(f"Part 2: {day_05([0, part2_input], True)}")