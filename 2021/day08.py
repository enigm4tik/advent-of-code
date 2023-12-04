# Advent of Code - 2021
## Day 8 - Part 1

with open('puzzle_input', 'r') as file:
# with open('test_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

signal_patterns = []
digit_lists = []
for line in lines: 
    signal_pattern, result = line.split(' | ')
    signal_patterns.append(signal_pattern)
    digit_lists.append(result)

count = 0

for digit_list in digit_lists:
    digits = digit_list.split(' ')
    for digit in digits:
        length = len(digit)
        if length in [2, 3, 4, 7]:
            count += 1

print(f"Part 1 - Result: {count}")

## Part 2

def determine_a(cf, acf):
    a = acf - cf
    return a

def determine_bd(cf, bcdf):
    bd = bcdf - cf
    return bd

def determine_f_and_g(five_list, a, bd, cf):
    fg = ''
    
    for fiver in five_list:
        fiver = set(fiver)
        temp_fg = fiver - a - bd
        if len(temp_fg) == 2:
            fg = set(temp_fg)
    
    f = fg.intersection(cf)
    g = fg - f

    return f, g

def determine_c(f, cf):
    c = cf -f
    return c

def determine_d(five_list, acf, g):
    d = ''
    for fiver in five_list:
        fiver = set(fiver)
        d = fiver - acf - g
        if len(d) == 1:
            return d

def determine_b(bd, d):
    b = bd - d
    return b

def determine_e(abcdefg, a, b, c, d, f, g):
    e = abcdefg - a - b - c - d - f - g
    return e

def get_key_from_letters(dictionary, val):
    for key, value in dictionary.items():
        if val == value:
            return key
        

def determine_code_through_letters(result, a, b, c, d, e, f, g):
    zero = a.union(b).union(c).union(e).union(f).union(g)
    two = a.union(c).union(d).union(e).union(g)
    three = a.union(c).union(d).union(f).union(g)
    five = a.union(b).union(d).union(f).union(g)
    six = a.union(b).union(d).union(e).union(f).union(g)
    nine = a.union(b).union(c).union(d).union(f).union(g)

    value_dictionary = {
        '0': zero,
        '2': two,
        '3': three,
        '5': five,
        '6': six,
        '9': nine
    }

    digit_string = ''
    for digit in result:
        digit = set(digit)
        key = get_key_from_letters(value_dictionary, digit)
        if key:
            digit_string += key
        if len(digit) == 2:
            digit_string += '1'
        if len(digit) == 3:
            digit_string += '7'
        if len(digit) == 4:
            digit_string += '4'
        if len(digit) == 7:
            digit_string += '8'
    return int(digit_string)
    
def determine_code(signal, result):
    signal = signal.split(' ')
    result = result.split(' ')
    five_list = []
    for split in signal:
        if len(split) == 2:
            cf = set(split)
        if len(split) == 3:
            acf = set(split)
        if len(split) == 4:
            bcdf = set(split)
        if len(split) == 7:
            abcdefg = set(split)
        if len(split) == 5:
            five_list.append(split)

    a = determine_a(cf, acf)
    bd = determine_bd(cf, bcdf)
    f, g = determine_f_and_g(five_list, a, bd, cf)
    c = determine_c(f, cf)
    d = determine_d(five_list, acf, g)
    b = determine_b(bd, d)
    e = determine_e(abcdefg, a, b, c, d, f, g)

    return determine_code_through_letters(result, a, b, c, d, e, f, g)

code_results = []
for line in lines: 
    signal_pattern, code = line.split(' | ')
    code_results.append(determine_code(signal_pattern, code))
print(f"Part 2 - Result: {sum(code_results)}")