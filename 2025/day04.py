# Advent of Code - 2025
## Day 3

with open('input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
   
new_grid=[]
for line in lines:
    row=[0 if l=="." else 1 for l in line]
    new_grid.append(row)

def get_neighbors(grid, position):
    """
    Get the 8 neighbors surrounding a position in a grid.
    If the position is on an edge, set it to "" instead. 
    
    :param grid: A 2d grid containing of 0s and 1s
    :param position: tuple of x and y position
    :return: list of 8 values, either boolean or ""
    """
    x,y=position
    max_width=len(grid[0])-1
    max_height=len(grid)-1
    one=grid[x-1][y-1] if x>0 and y>0 else ""
    two=grid[x][y-1] if y>0 else ""
    three=grid[x+1][y-1] if x<max_height and y>0 else ""
    four=grid[x-1][y] if x>0 else ""
    five=grid[x+1][y] if x<max_height else ""
    six=grid[x-1][y+1] if x>0 and y<max_width else ""
    seven=grid[x][y+1] if y<max_width else ""
    eight=grid[x+1][y+1] if x<max_height and y<max_width else ""
    neighbors=[one,two,three,four,five,six,seven,eight]
    return neighbors

def remove_rolls(grid,rolls):
    """
    Set the positions given in <rolls> to 0 in the grid. 
    
    :param grid: A 2d grid containing of 0s and 1s
    :param rolls: list of tuples (x,y)
    :return: updated grid 
    """
    for roll in rolls:
        x, y, = roll
        grid[x][y]=0
    return grid

def count_valid_rolls(grid):
    """
    Count each position of the grid that has at most 3 neighbors.
    
    :param grid: A 2d grid containing of 0s and 1s
    :return: tuple (count of grid, list of positions as tuple (x,y))
    """
    good=0
    good_rolls=[]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y]==1: neighbors=get_neighbors(grid, (x,y))
            else: continue
            if neighbors.count(1)<4:
                good_rolls.append((x,y))
                good+=1
    return (good, good_rolls)

good, good_rolls=count_valid_rolls(new_grid)
total=good
print("Part 1: ", total)
while good:
    grid=remove_rolls(new_grid[:], good_rolls)
    good, good_rolls=count_valid_rolls(grid)
    total+=good
print("Part 2: ", total)