# Advent of Code - 2021
## Day 11 - Part 1

import numpy as np 

with open('puzzle_input', 'r') as file:
# with open('test_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

octopi = np.empty([len(lines), len(lines[0])], int)
flashed = np.full((len(lines), len(lines[0])), False, dtype=bool)

for index, line in enumerate(lines): 
    for index2, character in enumerate(line): 
        octopi[index][index2] = character


def iterate_one_step(array, shiny_array, count, iteration):
    if iteration == 0:
        return count
    increased_array = increase_energy(array)
    new_array, shiny_array = check_if_neighbors_shine(increased_array, shiny_array)
    count += len(shiny_array[shiny_array==True])
    fixed_array, fixed_shiny = fix_arrays(new_array, shiny_array)
    return iterate_one_step(fixed_array, fixed_shiny, count, iteration-1)


def fix_arrays(new_array, shiny_array):
    new_array = np.where(new_array > 9, 0, new_array) # replace all 10s with 0 for next step
    shiny_array = np.full((len(lines), len(lines[0])), False, dtype=bool) # reset all shining octopi to False
    return new_array, shiny_array


def increase_energy(array):
    for index_i, value in enumerate(array):
        for index_j, value in enumerate(value):
            array[index_i,index_j] += 1
    return array


def find_neighbor_coordinates(x, y):
    my_neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            newx = x+j
            newy = y+i
            if newx < 0 or newy < 0: # neighbor doesn't exist
                continue
            elif newx == x and newy == y: # this is me
                continue
            elif newx > len(lines)-1 or newy > len(lines[0])-1: # index out of range
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

## Day 11 - Part 2

def when_do_all_octopi_light_up(array, shiny_array, count, iteration):
    if count == 100:
        return iteration
    increased_array = increase_energy(array)
    new_array, shiny_array = check_if_neighbors_shine(increased_array, shiny_array)
    count = len(shiny_array[shiny_array==True])
    fixed_array, fixed_shiny = fix_arrays(new_array, shiny_array)
    return when_do_all_octopi_light_up(fixed_array, fixed_shiny, count, iteration+1)

part1 = iterate_one_step(octopi, flashed, 0, 100)

print(f"Part 1 - Result: {part1}")

part2 = when_do_all_octopi_light_up(octopi, flashed, 0, 1)

print(f"Part 2 - Result: {part2}")