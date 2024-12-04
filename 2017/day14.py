from day10 import knot_hash

HASHMAP = {
    "0": "0000", "1": "0001", "2": "0010", "3": "0011",
    "4": "0100", "5": "0101", "6": "0110", "7": "0111",
    "8": "1000", "9": "1001", "a": "1010", "b": "1011",
    "c": "1100", "d": "1101", "e": "1110", "f": "1111",
}

def knot_hash_to_binary(knot_hash):
    global HASHMAP
    binarystring = ""
    for character in knot_hash:
        binarystring += HASHMAP[character]
    return binarystring

def create_grid(inputString):
    vector:list = []
    for i in range(128):
        currentInput = inputString + "-" + str(i)
        created_hash = knot_hash(currentInput)
        vector.append(knot_hash_to_binary(created_hash))
    return vector

def getActivated(vector):
    activated = []
    for indexh, hash in enumerate(vector):
        for indexc, character in enumerate(hash):
            if character == "1":
                activated.append((indexh, indexc))
    return activated

inputString = "flqrgnkx" #test string
myVector = create_grid(inputString)

all_activated = getActivated(myVector)

print("Advent of Code 2017: Day 14")
print("Part 1: ", len(all_activated))
# part 2

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_neighbors(coordinates, vector):
    x, y = coordinates
    for tuples in DIRECTIONS:
        x += tuples[0]
        y += tuples[1]
    print(x, y)

current_group = 0
while all_activated:
    check_for_group = [all_activated.pop(0)]
    current_group += 1
    while check_for_group:
        current = check_for_group.pop(0)
        for x, y in DIRECTIONS:
            new_tuple = (x+current[0], y+current[1])
            if new_tuple in all_activated:
                all_activated.remove(new_tuple)
                check_for_group.append(new_tuple)
            else:
                continue

print("Part 2: ", current_group)