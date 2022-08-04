# Advent of Code - 2017
## Day 8

with open('puzzle_input') as file:
#with open('test_input') as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]

def initialize_registers(list_of_registers):
  registers = {letter: 0 for letter in list_of_registers}
  return registers

register_list = []

for line in lines:
  register, *rest = line.split(" ")
  if not register in register_list:
    register_list.append(register)
    
registers = initialize_registers(register_list)

def execute_inc(register, by, register_list):
  register_list[register] += int(by)
  return register_list


def execute_dec(register, by, register_list):
  register_list[register] -= int(by)
  return register_list
  

def check_condition_on_current_registers(condition, registers):
  compare_first, using, compare_second = condition[1:]
  if using == '>=': 
    return registers[compare_first] >= int(compare_second)
  if using == '==':
    return registers[compare_first] == int(compare_second)
  if using == "<=":
    return registers[compare_first] <= int(compare_second)
  if using == "<":
    return registers[compare_first] < int(compare_second)
  if using == ">":
    return registers[compare_first] > int(compare_second)
  if using == '!=':
    return registers[compare_first] != int(compare_second)


def find_biggest_register(registers):
  return max(registers.values())

biggest_register = 0

for line in lines:
  register, instruction, by, *condition = line.split(" ")
  execute = check_condition_on_current_registers(condition, registers)
  if execute:
    if instruction == "inc":
      registers = execute_inc(register, by, registers)
    else:
      registers = execute_dec(register, by, registers)
    current_biggest_register = find_biggest_register(registers)
    if current_biggest_register > biggest_register:
      biggest_register = current_biggest_register
  
print(f"Part 1: {find_biggest_register(registers)}")
print(f"Part 2: {biggest_register}")
