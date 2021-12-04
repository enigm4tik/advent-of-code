# Advent of Code - 2021
## Day 4 - Part 1

import numpy as np

with open('day04_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

bingo_numbers = lines[0].split(',')
bingo_numbers = [int(bingo_number) for bingo_number in lines[0].split(',')]


class BingoField:
    bingo_field = None   

    def __init__(self, bingo_rows):
        self.bingo_field = np.array(bingo_rows, np.int32)


def create_bingo_fields_out_of_lines(lines): 
    bingo_rows = []
    for line in lines: 
        if not lines.index(line) == 0:
            if line == '':
                continue
            else: 
                line = line.split(' ')
                line = list(filter(lambda c: c != '', line))
                bingo_rows.append(line)

    indices = []
    bingofields = []
    for i in range(len(bingo_rows) + 1):
        if i % 5 == 0:
            indices.append(i)
        
    for i in range(len(indices)+1): 
        try: 
            bingo_field = BingoField(bingo_rows[indices[i]: indices[i+1]])
            bingofields.append(bingo_field)
        except IndexError:
            break
    return bingofields


def check_for_bingo_number_in_grid(bingo_number, bingo_field):
    result = list(zip(*np.where(bingo_field == int(bingo_number))))

    try: 
        x = result[0][0]
        y = result[0][1]
        bingo_field[x, y] = -1
    except IndexError:
        pass
    return bingo_field


def check_if_bingo(bingo_field):
    bingo_winning_row = np.array([-1, -1, -1, -1, -1], int)
    for i in range(5):
        row = bingo_field[i]
        column = bingo_field[:,i]
        if np.all(np.equal(bingo_winning_row, row)) or np.all(np.equal(bingo_winning_row, column)):
            return True
        continue
    return False


def calculate_remaining_fields(bingofield):
    amount_of_minus_ones = len(bingofield[bingofield==-1])
    sum_plus_minus_ones = np.sum(bingofield)
    sum_of_remaining_fields = sum_plus_minus_ones + amount_of_minus_ones
    return sum_of_remaining_fields

bingofields = create_bingo_fields_out_of_lines(lines)

bingo = False

for bingo_number in bingo_numbers:
    for index, bingo_field in enumerate(bingofields):
        bingo_field_array = bingo_field.bingo_field
        check_for_bingo_number_in_grid(bingo_number, bingo_field_array)
        bingo = check_if_bingo(bingo_field_array)
        if bingo:
            remaining_fields_sum = calculate_remaining_fields(bingo_field_array)
            print(f"Part 1 - Result: {remaining_fields_sum * bingo_number}")
            break
    if bingo: 
        break

## Day 4 - Part 2

def remove_winning_field(bingo_fields, winning_bingo_field):
    bingo_fields.remove(winning_bingo_field)


def figure_out_who_wins(bingofields):
    bingo = False
    for bingo_field in bingofields:
        bingo_field_array = bingo_field.bingo_field
        check_for_bingo_number_in_grid(bingo_number, bingo_field_array)
        bingo = check_if_bingo(bingo_field_array)
        if bingo:
            if not len(bingofields) == 1:
                remove_winning_field(bingofields, bingo_field)
                figure_out_who_wins(bingofields)
            else: 
                remaining_fields_sum = calculate_remaining_fields(bingo_field_array)
                print(f"Part 2 - Result: {remaining_fields_sum * bingo_number}")
                return False
    return True
                        

for bingo_number in bingo_numbers:
    if not figure_out_who_wins(bingofields):
        break