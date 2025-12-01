# Advent of Code - 2025
## Day 1

with open('input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

possibilities=100
pointer = 50
part1 = 0
part2 = 0

for line in lines:
    direction = line[0]
    value = int(line[1:])
    if value > possibilities:
        clicks = value//possibilities ## full turns
        part2 += clicks
        value = value%possibilities ## remainder
    if direction == "L":
        if pointer==0:
            pointer-=value
            pointer=pointer%possibilities
            continue
        pointer-=value
        if pointer<=0: 
            part2+=1
    else:
        if pointer==0:
            pointer+=value
            pointer=pointer%possibilities
            continue
        pointer+=value
        if pointer>possibilities-1: 
            part2+=1 
    pointer=pointer%possibilities
    if pointer==0: ## Part 1: only when pointer is AT 0
        part1 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
