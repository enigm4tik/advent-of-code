# Advent of Code - 2021
## Day 11 - Part 1

from types import new_class
import numpy as np 

with open('puzzle_input', 'r') as file:
# with open('test_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

empty = np.empty([len(lines), len(lines[0])], int)
shiny_array = np.full((len(lines), len(lines[0])), False, dtype=bool)
can_shine_array = np.full((len(lines), len(lines[0])), True, dtype=bool)

for index, line in enumerate(lines): 
    for index2, letter in enumerate(line): 
        empty[index][index2] = letter

def make_one_step(array, shiny_array, count, iteration):
    if iteration == 0:
        return array, count
    increased_array = increase_energy(array)
    new_array, shiny_array = check_if_neighbors_shine(increased_array, shiny_array)
    count += len(shiny_array[shiny_array==True])
    fixed_array, fixed_shiny = fix_arrays(new_array, shiny_array)
    return make_one_step(fixed_array, fixed_shiny, count, iteration-1)

def part2(array, shiny_array, count, iteration):
    print(iteration)
    print(count)
    if count == 100:
        return array, iteration
    increased_array = increase_energy(array)
    new_array, shiny_array = check_if_neighbors_shine(increased_array, shiny_array)
    count = len(shiny_array[shiny_array==True])
    fixed_array, fixed_shiny = fix_arrays(new_array, shiny_array)
    return part2(fixed_array, fixed_shiny, count, iteration+1)

def fix_arrays(new_array, shiny_array):
    new_array = np.where(new_array > 9, 0, new_array)
    shiny_array = np.full((len(lines), len(lines[0])), False, dtype=bool)
    return new_array, shiny_array

def increase_energy(array):
    for index_i, value in enumerate(array):
        for index_j, value in enumerate(value):
            array[index_i,index_j] += 1
    return array

def find_neighbor_coordinates(x, y):
    # print(f"this is me: {(x, y)}")
    my_neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            newx = x+j
            newy = y+i
            # print(f"my new: {newx, newy}")
            if newx < 0 or newy < 0:
                continue
            elif newx == x and newy == y: # this is me again
                # print(f"this is me again!: {(newx, newy)}")
                continue
            elif newx > 9 or newy > 9:
                continue
            else: 
                my_neighbors.append((newx, newy))
    return my_neighbors

def flash_my_neighbors(array, shiny_array, myx, myy):
    new_array = array
    my_neighbors = find_neighbor_coordinates(myx, myy)
    imma_flash = []
    for x, y in my_neighbors:
        old_value = array[x, y]
        if old_value < 9:
            new_array[x, y] += 1
        else: 
            shiny = shiny_array[x, y]
            if not shiny: 
                imma_flash.append((x, y))
                array[x, y] = 10
                shiny_array[x, y] = True
                
    if len(imma_flash):
        for flx, fly in imma_flash:
            flash_my_neighbors(array, shiny_array, flx, fly)

    return new_array, shiny_array


def check_if_neighbors_shine(array, shiny_array, shiny_neighbors=1):
    new_array = array
    shining_array = shiny_array
    if shiny_neighbors == 0:
        return new_array, shiny_array
    shiny_neighbors = 0
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            shine_value = array[x, y]
            shone = shiny_array[x, y]
            if shine_value > 9 and not shone:
                shiny_neighbors += 1
                shiny_array[x, y] = True
                new_array, shining_array = flash_my_neighbors(new_array, shining_array, x, y)
    return check_if_neighbors_shine(new_array, shining_array, shiny_neighbors)

# print(make_one_step(empty, shiny_array, 0, 100))
# make_one_step(empty, shiny_array, 0, 2)

print(part2(empty, shiny_array, 0, 0))

# print(make_one_step(empty, shiny_array, 0, 36))