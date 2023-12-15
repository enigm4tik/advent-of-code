# Advent of Code - 2023
## Day 14

# This was a lot of work, I'll refactor it if I feel like it.
# It works, that's all I needed after day 12 and 13 ....

with open('input') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def move_north(werte, blocker):
    seen = []
    for wert in werte:
        list_of_blockers = [i for i in blocker if i < wert]
        if not list_of_blockers: 
            max_blocker = 0
        else: 
            if seen: 
                max_blocker = max(seen[-1], *list_of_blockers)
            else: 
                max_blocker = max(list_of_blockers)
        start = min([wert, max_blocker])
        next = min([i for i in range(start, wert+1) if i not in seen and i not in blocker])
        seen.append(next)
    return seen

def rotate(circles, length=9):
    circles = [(y, length-x) for x, y in circles]
    return sorted(circles)

def move_north_rotate(circles, squares, length):
    new_circles = []
    for i in range(length):
        werte = [j[0] for j in circles if j[1] == i]
        blocker = [j[0] for j in squares if j[1] == i]
        north = move_north(werte, blocker)
        for k in north:
            new_circles.append((k, i))
    return new_circles, squares 

def rotate_after(circles, squares, length):
    circles = rotate(circles, length)
    squares = rotate(squares, length)
    return circles, squares

def get_north_support_beams(list_of_stones):
    list_of_stones = [i for i, j in list_of_stones]
    didi = {}
    for i in list_of_stones:
        try: 
            didi[10-i] += 1
        except KeyError: 
            didi[10-i] = 1
    result = 0
    for key, value in didi.items():
        result += key * value 
    return result

circles = []
squares = []
for x in range(len(lines)): 
    for y in range(len(lines[0])):
        if lines[x][y] == "O":
            circles.append((x, y))
        if lines[x][y] == "#":
            squares.append((x, y))


first_circle = circles[::]
seen_circles = [circles]
seen_squares = []
big_number = 1000000000
loop_found = False
i = 0
loop_index = 0
while not loop_found and i < big_number: 
    for j in range(4):
        circles, squares = move_north_rotate(circles, squares, len(lines[0]))
        circles, squares = rotate_after(circles, squares, len(lines[0])-1)
    if not circles in seen_circles:
        seen_circles.append(circles)
    else: 
        repeater = seen_circles.index(circles)
        # cycle_length = print(f"{i - seen_circles.index(circles)}")
        loop_found = True
        cycle_length = i-seen_circles.index(circles)
        first_repeat = i
        loop_found = True
    i+= 1


for i in range(1, 2000):
    bla = (big_number - i*(repeater+1)) % cycle_length
    print(bla)
    if bla != 0:
        break

result = get_north_support_beams(seen_circles[bla + repeater +1])
print(result)