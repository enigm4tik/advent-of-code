# Advent of Code - 2016
## Day 8
import numpy as np

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

display = np.full([6, 50], '.')
# display = np.full([3, 7], '.') # for test data

def create_a_rectangle(screen, dimensions):
    column, row = dimensions.split('x')
    column = int(column)
    row = int(row)
    screen[0:row, 0:column] = '#'


def rotate_row(screen, x_value, rotate_value):
    slice = screen[x_value:x_value+1,:]
    slice = np.roll(slice, rotate_value)
    screen[x_value:x_value+1,:] = slice


def rotate_column(screen, y_value, rotate_value):
    slice = screen[:, y_value:y_value+1]
    slice = np.roll(slice, rotate_value)
    screen[:, y_value:y_value+1] = slice


def make_human_readable(screen):
    a = []
    for i in range(6):
        a.append([bla.item() for bla in np.nditer(screen[i:i+1,:])])
    for row in range(len(a)):
        print(''.join(a[row]))

for line in lines:
    if line.startswith('rect'):
        dimensions = line.split()[1]
        create_a_rectangle(display, dimensions)
    elif line.startswith('rotate'):
        command, axis, where, trash, how_much = line.split()
        if axis == 'column':
            y_value = where.split('=')[1]
            rotate_column(display, int(y_value), int(how_much))
        elif axis == 'row':
            x_value = where.split('=')[1]
            rotate_row(display, int(x_value), int(how_much))

print(f"Part 1: {len(display[display=='#'])}")

print(f"Part 2:")
make_human_readable(display)
