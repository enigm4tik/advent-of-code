# Advent of Code - 2020
## Day 7 - Part 1

with open('puzzle_input', 'r') as file:
# with open('test-input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

all_bags = {}

for line in lines: 
    bag, contained_bag = line.split('contain')
    bag = bag.split('bags')[0]
    bag = bag.strip()
    all_bags[bag] = {}
    contained_bags = contained_bag.split(',')
    for contained_bag in contained_bags:
        contained_bag = contained_bag.strip()
        amount = contained_bag[0]
        if amount == 'n':
            continue
        else: 
            amount = int(amount)
        bag_name = contained_bag[2:]
        bag_name = bag_name.split('bag')[0]
        bag_name = bag_name.strip()
        all_bags[bag].update({bag_name:amount})

to_check = list(all_bags.keys())
done = []
can_contain_shiny = []
containers = {}

def iterate_over_graph(bag):
    if not bag in done:
        done.append(bag)
    my_neighbors = all_bags[bag]
    if 'shiny gold' in my_neighbors:
        if not bag in can_contain_shiny:
            can_contain_shiny.append(bag)
    if bag in to_check: 
        to_check.remove(bag)
    for neighbor_bag in my_neighbors:
        if neighbor_bag not in to_check and neighbor_bag not in done:
            to_check.append(neighbor_bag)
        if not neighbor_bag in containers:
            containers[neighbor_bag] = [bag]
        else: 
            containers[neighbor_bag].append(bag)

while to_check:
    iterate_over_graph(to_check[0])

done = []
result = can_contain_shiny[:]
def find_parent_bags(bag):
    if not bag in done:
        done.append(bag)
        can_contain_shiny.remove(bag)
    try: 
        my_containees = containers[bag]
        for container_bag in my_containees:
            if not container_bag in result:
                result.append(container_bag)
            if container_bag not in can_contain_shiny and container_bag not in done:
                can_contain_shiny.append(container_bag)
    except KeyError:
        if not bag in result:
            result.append(bag)

while can_contain_shiny:
    find_parent_bags(can_contain_shiny[0])

print(f"Part 1: {len(result)}")

