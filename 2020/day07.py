# Advent of Code - 2020
## Day 7 - Part 1

with open('puzzle_input', 'r') as file:
# with open('test-input', 'r') as file:
# with open('test_input2', 'r') as file:
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
with_amounts = {}
contained_in_shiny_gold = ['shiny gold']

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
        if bag == 'shiny gold' or bag in contained_in_shiny_gold:
            contained_in_shiny_gold.append(neighbor_bag)
        amount = sum(all_bags[bag].values())
        if neighbor_bag not in to_check and neighbor_bag not in done:
            to_check.append(neighbor_bag)
        if not neighbor_bag in containers:
            containers[neighbor_bag] = [bag]
            with_amounts[neighbor_bag] = {bag: amount}
        else: 
            containers[neighbor_bag].append(bag)
            with_amounts[neighbor_bag].update({bag: amount})

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

# print(f"Part 1: {len(result)}")

## Part 2

contained_in_shiny_gold = list(set(contained_in_shiny_gold))

amount_of_bags_per_bag = {bag: 1 for bag in all_bags.keys()}

starting_bags = [bag for bag in all_bags if not bag in containers]
empty_bags = [bag for bag in all_bags if not all_bags[bag].values()]


to_check = empty_bags[:]
done = []
while to_check:
    current_bag_to_check = to_check[0]
    done.append(current_bag_to_check)
    if containers[current_bag_to_check]:
        for bag in containers[current_bag_to_check]:
            if bag in empty_bags or bag in starting_bags or bag not in contained_in_shiny_gold:
                continue
            elif bag =='shiny gold':
                continue
            elif not bag in to_check and not bag in done:
                to_check.append(bag)
                amount = 1 + all_bags.get(bag) * amount_of_bags_per_bag[current_bag_to_check]
                amount_of_bags_per_bag[bag] = amount
    to_check.remove(current_bag_to_check)


def calculate_amount_of_bags_in_shiny_gold():
    bag_sum = 0
    for bag in all_bags['shiny gold']:
        bag_sum += amount_of_bags_per_bag[bag] * all_bags['shiny gold'].get(bag)
    return bag_sum

print(calculate_amount_of_bags_in_shiny_gold())
