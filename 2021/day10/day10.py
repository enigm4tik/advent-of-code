# Advent of Code - 2021
## Day 10 - Part 1

with open('puzzle_input', 'r') as file:
# with open('test_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

syntax_error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
auto_complete_scores = {')': 1, ']': 2, '}': 3, '>': 4}
pairs = [('(', ')'), ('[', ']'), ('<', '>'), ('{', '}')]
opened = []
closed = []
dict_of_pairs = {}
for pair in pairs: 
    open, close = pair
    opened.append(open)
    closed.append(close)
    dict_of_pairs[open] = close


def find_first_closed(line):
    first_closed = []
    for close in closed:
        try:
            first_closed.append(line.index(close))
        except ValueError:
            continue
    if not first_closed:
        return False, 0
    return line[min(first_closed)], min(first_closed)

def find_last_opened(line):
    last_opened = []
    for open in opened:
        last_opened.append(line.rfind(open))
    return line[max(last_opened)]

def check_if_opened_and_closed_are_a_pair(closed, opened):
    for pair in pairs:
        if set(pair) == set([closed, opened]):
            return True
    return False

def remove_pair(line, opened, closed):
    line = line.replace(opened+closed, '', 1)
    return line

def mimic_lines_backwards(line):
    result = ''
    for character in line[::-1]:
        result += dict_of_pairs[character]
    return result

def check_line_for_syntax(line):
    first_closed, index_close = find_first_closed(line)
    if not first_closed:
        return mimic_lines_backwards(line)
    shorter_line = line[:index_close]
    last_opened = find_last_opened(shorter_line)
    if check_if_opened_and_closed_are_a_pair(first_closed, last_opened):
        new_line = remove_pair(line, last_opened, first_closed)
        return check_line_for_syntax(new_line)
    else:
        return first_closed

syntax_errors = []
for line in lines:
    syntax_error = check_line_for_syntax(line)
    syntax_errors.append(syntax_error)

def calculate_syntax_error_score(syntax_errors):
    score = 0
    for syntax_error in syntax_errors:
        if len(syntax_error) == 1:
            score += syntax_error_scores[syntax_error]
    return score

part1 = calculate_syntax_error_score(syntax_errors)

print(f"Part 1 - Result: {part1}")

## Day 10 - Part 2

def calculate_autocomplete_score(syntax_errors):
    score = 0
    list_of_scores = []
    for syntax_error in syntax_errors:
        if len(syntax_error) != 1:
            for character in syntax_error:
                score *= 5
                score += auto_complete_scores[character]
        else: 
            continue
        list_of_scores.append(score)
        score = 0
    return get_middle_result(list_of_scores)

def get_middle_result(result_list):
    result_list.sort()
    length = len(result_list)
    if length%2 == 0:
        middle_index = int(length/2)
    else:
        middle_index = int(float(length/2)-0.5)
    return result_list[middle_index]

part2 = calculate_autocomplete_score(syntax_errors)
print(f"Part 2 - Result: {part2}")
