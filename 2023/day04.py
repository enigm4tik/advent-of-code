# Advent of Code - 2023
## Day 4

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

dictionary_of_tickets = {x+1: 1 for x in range(len(lines))}

sum_of_points = 0
for id, line in enumerate(lines, start=1): 
    card, numbers = line.split(":")
    winners, played = numbers.split("|")
    winners = winners.strip().split(" ")
    played = played.strip().split(" ")
    winners = set(winners) - {''}
    played = set(played) - {''}
   
    winning = winners & played 
    if winning:        
        sum_of_points += 2**(len(winning)-1)
        for ticket, win in enumerate(winning, start=id):
            dictionary_of_tickets[ticket+1] += dictionary_of_tickets[id]

part1 = sum_of_points
part2 = sum(list(dictionary_of_tickets.values()))

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 4':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1:^55}")
print(f"Part 2: {part2:^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")