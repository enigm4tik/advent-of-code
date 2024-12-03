def get_exclamations(string, id):
    count = 0
    for s in reversed(string[:id]):
        if s == "!":
            count += 1
        else: break
    if count%2 == 0:
        return True


def get_opener(opener_list, value):
    for index, opener in enumerate(opener_list):
        if opener > value:
            return index


def garbage_collector(a):
    garbage = []
    garbage_open = [i for i, x in enumerate(a) if x == "<"]
    garbage_close = [j for j, y in enumerate(a) if y == ">" and get_exclamations(a, j)]
    newstring = ""
    opened = 0
    ns = -1
    for g in range(len(garbage_close)):

        garbage.append(a[garbage_open[opened]:garbage_close[g]+1])
        newstring += a[ns+1:garbage_open[opened]] + a[garbage_close[g]+1]
        ns = garbage_close[g]+1
        opened = get_opener(garbage_open, garbage_close[g])
    
    newstring += a[ns+1:]
    return (newstring, garbage)


def calculate_score(clean_string):
    group = 0
    score = 0
    for s in clean_string:
        if s == "{":
            group += 1
            score += group
        elif s == ',':
            continue
        else:
            group -= 1
    return score


def garbage_counter(garbage):
    skip = False
    overall_trash = 0
    for trash in garbage:
        trash_characters = 0
        for char in trash:
            if char == "!" and not skip:
                skip = True
                continue
            if skip:
                skip = False
                continue
            trash_characters += 1
        overall_trash += trash_characters-2
    return overall_trash

with open("puzzle_input", 'r') as file:
    string = file.readline()
clean, garbage = garbage_collector(string)
get_exclamations(string, 5)
print(f'Part 1: {calculate_score(clean)}')
print(f'Part 2: {garbage_counter(garbage)}')
