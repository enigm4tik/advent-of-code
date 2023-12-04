# Advent of Code - 2016
## Day 3
import numpy as np
from itertools import permutations

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.split() for line in lines]

alleged_triangle_list = []
for line in lines:
    alleged_triangle_list.append([int(side) for side in line])


def is_it_a_triangle(triangle_sides):
    a = triangle_sides[0]
    b = triangle_sides[1]
    c = triangle_sides[2]

    if any((x + y <= z for x, y, z in permutations((a, b, c)))):
        return 0
    else:
        return 1
    
    # The above statement is equivalent to this but without consecutive ors.
    # if a + b <= c or a + c <= b or c + b <= a:
    #     return 0
    # else:
    #     return 1
    

def find_legit_triangles(triangle_list):
    triangles = 0
    for triangle in triangle_list:
        triangles += is_it_a_triangle(triangle)
    return triangles

#Part 2

for index, row in enumerate(alleged_triangle_list):
    if index == 0:
        triangle_array = np.array(row)
    else:
        triangle_array = np.vstack((triangle_array, row))

vertical_alleged_triangles = []

while triangle_array.shape[0]:
    for i in range(3):
        vertical_alleged_triangles.append([side for side in triangle_array[0:3, i]])
    triangle_array = triangle_array[3:, :]


print(f"Part 1: {find_legit_triangles(alleged_triangle_list)}")
print(f"Part 2: {find_legit_triangles(vertical_alleged_triangles)}")