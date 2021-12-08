# Advent of Code - 2020
## Day 6 - Part 1

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

## Code to split the list on the '' value.
size = len(lines)
idx_list = [idx + 1 for idx, val in
            enumerate(lines) if val == '']
  
res = [lines[i: j] for i, j in
        zip([0] + idx_list, idx_list + 
        ([size] if idx_list[-1] != size else []))]

answer_list = []
count = 0
for group in res:
    for person in group: 
        for answer in person: 
            if not answer in answer_list and answer != '':
                answer_list.append(answer)
    count += len(answer_list)
    answer_list = []

print(f"Part 1 - Result: {count}")

## Day 6 - Part 2

answer_dict = {}
answers_in_common = 0
group_size = 0
for group in res:
    for person in group: 
        if person:
            group_size += 1
            for answer in person: 
                try: 
                    answer_dict[answer] += 1
                except:
                    answer_dict[answer] = 1
    
    answers_in_common_for_group = [k for k, v in answer_dict.items() if v == group_size]
    group_size = 0
    answers_in_common += len(answers_in_common_for_group)
    answer_dict = {}

print(f"Part 2 - Result: {answers_in_common}")