# Advent of Code - 2017
## Day 7

with open('puzzle_input') as file:
# with open('test_input') as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]


def parse_lines(line):
  name, weight = line.split('(')
  name = name.strip()
  weight, rest = weight.split(')')
  weight = int(weight.strip())
  rest = rest.strip()
  programs[name] = weight
  if rest:
    rest = rest.split('-> ')[1]
    for child in rest.split(","):
      child = child.strip()
      parents[child] = name
      if not name in children: 
        children[name] = [child]
      else:  
        children[name].append(child)


def find_parents_of_programs_without_children():
  childless = {}
  for program in all_programs:
    if program not in children:
      parent = parents[program]
      if not parent in childless:
        childless[parent] = [programs[program]]
      else:
        childless[parent].append(programs[program])
  return childless


def filter_parents_with_grandchildren(grandparents):
  filtered_parents = []
  for parent in grandparents:
    my_children = []
    for child in children[parent]:
      if not child in parents.values():
        my_children.append(child)
    if set(children[parent]) - set(my_children):
      continue
    else:
      filtered_parents.append(parent)
  grandparents = {
    filtered_parent: grandparents[filtered_parent] for filtered_parent in filtered_parents
  }  
  return grandparents


def find_solution_based_on_program_weights(weights):
  calculated_weights = weights['calculated']
  original_weights = weights['original']
  most_common = max(set(calculated_weights), key = calculated_weights.count)
  least_common = min(set(calculated_weights), key = calculated_weights.count)
  value_to_change = calculated_weights.index(least_common)
  difference = most_common - least_common
  original = original_weights[value_to_change] + difference
  return original


def update_parent_weights(parent, weight, siblings):
  programs[parent] += siblings * weight
  

programs = {}
children = {}
parents = {}

for line in lines:
  parse_lines(line)

for program in programs:
  if program not in parents.keys():
    print(f"Part 1: {program}")

all_programs = [program for program in programs.keys()]
original_weights = {**programs}

culprit_found = False
while not culprit_found:
  parents_without_children = find_parents_of_programs_without_children()
  no_grandparents = filter_parents_with_grandchildren(parents_without_children)
  for parent_without_children in no_grandparents:
    if len(set(no_grandparents[parent_without_children])) == 1:
      update_parent_weights(parent_without_children, no_grandparents[parent_without_children][0], len(no_grandparents[parent_without_children]))
      all_programs = list(set(all_programs) - set(children[parent_without_children]))
      orphans = children.pop(parent_without_children)
      for orphan in orphans:
        parents.pop(orphan)
    else:
      weights = {
        "original": [],
        "calculated": []
      }
      for program in children[parent_without_children]:
        weights["original"].append(original_weights[program])
        weights["calculated"].append(programs[program])
      result = find_solution_based_on_program_weights(weights)
      culprit_found = True

print(f"Part 2: {result}")