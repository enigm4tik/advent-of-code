import numpy as np

instruction_string = "secret"

def create_instruction_list(instructions):
  instructions = instructions.split(",")
  instructions = [int(instruction.strip()) for instruction in instructions]
  return instructions

instructions = create_instruction_list(instruction_string)

# circle_length = 5
circle_length = 256
circle = [i for i in range(circle_length)]
circle_array = np.array(circle)

def move_one_step(array, current_position, length, skip_size):
  array_length = array.shape[0]  
  indices = [i%array_length for i in range(current_position, current_position + length)]
  array[indices] = np.flip(array[indices], 0)
  current_position += length + skip_size
  skip_size += 1
  return array, current_position, skip_size

current_position = skip_size = 0
for instruction in instructions:
  circle_array, current_position, skip_size = move_one_step(circle_array, current_position, instruction, skip_size)

print(f"Part 1: {circle_array[0] * circle_array[1]}")

def create_ascii_instructions(instructions):
  instructions = [ord(character) for character in instructions]
  instructions.extend([17, 31, 73, 47, 23])
  return instructions 

# instruction_string = "AoC 2017"
instructions = create_ascii_instructions(instruction_string)

current_position = skip_size = 0
circle_array = np.array(circle)
for i in range(64):
  for instruction in instructions:
    circle_array, current_position, skip_size = move_one_step(circle_array, current_position, instruction, skip_size)

def dense_hash(array):
  dense_hash = []
  sub_arrays = np.split(array, 16)
  for sub_array in sub_arrays:
    calculated_xor = 0
    for number in sub_array:
      calculated_xor ^= number
    dense_hash.append(calculated_xor)
  return dense_hash
  
dense_hash = dense_hash(circle_array)
return_string = ""
for item in dense_hash:
  return_string += hex(item)

print(f"Part 2: {return_string.replace('0x', '')}")