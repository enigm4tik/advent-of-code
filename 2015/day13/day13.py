# Advent of Code - 2015
## Day 13

from itertools import permutations

with open('puzzle_input') as file:
    lines = file.readlines()
    lines = [line.rstrip().split(" ") for line in lines]
    
happiness = {}

for line in lines: 
    if 'gain' in line: 
        if not line[0] in happiness:
            happiness[line[0]] = {line[-1][:-1]: int(line[3])}
        else: 
            happiness[line[0]].update({line[-1][:-1]: int(line[3])})
    else: 
        if not line[0] in happiness:
            happiness[line[0]] = {line[-1][:-1]: int(line[3])*-1}
        else: 
            happiness[line[0]].update({line[-1][:-1]: int(line[3])*-1})


def find_unique_possibilities(all_permutations):
    list_of_permutations = list(all_permutations)
    unique_permutations = [x for x in list_of_permutations if x[0] == 'Alice'] # Any name would work. 
    return unique_permutations

def calculate_happiness(seating, happiness_dictionary):
    current_happiness = 0
    for index, person in enumerate(seating): 
        current_happiness += happiness_dictionary[person][seating[index-1]]
        if not index == len(seating)-1:
            current_happiness += happiness_dictionary[person][seating[index+1]]
        else:
            current_happiness += happiness_dictionary[person][seating[0]]
    return current_happiness

all_people = happiness.keys()
all_possible_seating_arrangements = permutations(all_people)
unique_seating_arrangements = find_unique_possibilities(all_possible_seating_arrangements)

maximal_happiness_part_1 = 0
for seating in unique_seating_arrangements:
    change_in_happiness = calculate_happiness(seating, happiness)
    if change_in_happiness > maximal_happiness_part_1:
        maximal_happiness_part_1 = change_in_happiness
print(f"Part 1: {maximal_happiness_part_1}")

# Part 2

happiness_part_2 = happiness.copy()
for person in happiness_part_2:
    happiness_part_2[person].update({'Enigm4tik': 0})

me = {person: 0 for person in happiness_part_2.keys()}
happiness_part_2['Enigm4tik'] = me

all_people = happiness_part_2.keys()
all_possible_seating_arrangements = permutations(all_people)
unique_seating_arrangements = find_unique_possibilities(all_possible_seating_arrangements)

maximal_happiness_part_2 = 0
for seating in unique_seating_arrangements:
    change_in_happiness = calculate_happiness(seating, happiness_part_2)
    if change_in_happiness > maximal_happiness_part_2:
        maximal_happiness_part_2 = change_in_happiness

print(f"Part 2: {maximal_happiness_part_2}")