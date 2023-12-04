# Advent of Code - 2017
## Day 6

with open('puzzle_input') as file:
#with open('test_input') as file:
  lines = file.readlines()
  lines = lines[0].split('\t')
  lines = [int(line) for line in lines]

def find_bank_with_most_blocks(banks):
  return banks.index(max(banks))

def redistribute_blocks(banks):
  bank_with_most_blocks = find_bank_with_most_blocks(banks)
  blocks_to_distribute = banks[bank_with_most_blocks]
  banks[bank_with_most_blocks] = 0
  for i in range(blocks_to_distribute):
    banks[(i+bank_with_most_blocks+1) % len(banks)] += 1
  return banks
    
known_configurations = [lines[::]]
not_in_loop = True
loop_index = 0

while not_in_loop:
  loop_index += 1
  lines = redistribute_blocks(lines)
  if not lines in known_configurations:
    known_configurations.append(lines[::])
  else:
    known_configurations.append(lines[::])
    not_in_loop = False

print(f"Part 1: {loop_index}")

def find_loop_length(loop):
  last_config = loop[-1]
  complete_length = len(loop) - 1
  first_config = loop.index(last_config)
  loop_length = complete_length - first_config 
  return loop_length

print(f"Part 2: {find_loop_length(known_configurations)}")
