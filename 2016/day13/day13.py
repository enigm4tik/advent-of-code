# Advent of Code - 2016
## Day 13

from math import floor
import numpy as np 
np.set_printoptions(threshold=np.inf, linewidth=200)

# with open('puzzle_input') as file:
with open('test_input') as file:
    lines = file.readlines()

favorite_number = 10 
favorite_number = 1352
size = 10
size = 40

floor_plan = np.full([size+10,size],'.', str)

def fill_floor_plan():
    for i in range(size+10):
        for j in range(size):
            floor_plan[i][j] = determine_wall_or_room(j, i)

def determine_wall_or_room(x, y):
    formula = x*x + 3*x + 2*x*y + y + y*y + favorite_number
    binary_representation = str(format(formula, 'b'))
    ones = binary_representation.count('1')
    if ones%2:
        return '#'
    else:
        return '.'
    
fill_floor_plan()
destination = (7,4)

movements = {
    'down': (0, 1),
    'right': (1, 0)
}

def move_to_destination(coordinates):
    
    pass

paths = {}

def move_one_step(my_coordinates, step=0):
    print(step)
    my_x, my_y = my_coordinates
    downx = my_x
    downy = my_y +1
    rightx = my_x +1
    righty = my_y
    down = floor_plan[downx, downy]
    right = floor_plan[rightx, righty]

# floor_plan[4][7] = 'X'
floor_plan[39][31] = 'X'
print(floor_plan)