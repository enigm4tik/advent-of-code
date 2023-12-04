# Advent of Code - 2021
## Day 6 - Part 1

fish_list = [4,3,3,5,4,1,2,1,3,1,1,1,1,1,2,4,1,3,3,1,1,1,1,2,3,1,1,1,4,1,1,2,1,2,2,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,5,1,4,2,1,1,2,1,3,1,1,2,2,1,1,1,1,1,1,1,1,1,1,4,1,3,2,2,3,1,1,1,4,1,1,1,1,5,1,1,1,5,1,1,3,1,1,2,4,1,1,3,2,4,1,1,1,1,1,5,5,1,1,1,1,1,1,4,1,1,1,3,2,1,1,5,1,1,1,1,1,1,1,5,4,1,5,1,3,4,1,1,1,1,2,1,2,1,1,1,2,2,1,2,3,5,1,1,1,1,3,5,1,1,1,2,1,1,4,1,1,5,1,4,1,2,1,3,1,5,1,4,3,1,3,2,1,1,1,2,2,1,1,1,1,4,5,1,1,1,1,1,3,1,3,4,1,1,4,1,1,3,1,3,1,1,4,5,4,3,2,5,1,1,1,1,1,1,2,1,5,2,5,3,1,1,1,1,1,3,1,1,1,1,5,1,2,1,2,1,1,1,1,2,1,1,1,1,1,1,1,3,3,1,1,5,1,3,5,5,1,1,1,2,1,2,1,5,1,1,1,1,2,1,1,1,2,1]


def decrease_all_values_by_one(list_to_decrease):
    new_list = [value - 1 for value in list_to_decrease]
    return(new_list)

def add_new_fish(list_of_fishes):
    amount_of_new_fish = list_of_fishes.count(-1)
    if amount_of_new_fish: 
        list_of_new_fish = [8 for i in range(amount_of_new_fish)]
        list_of_fishes.extend(list_of_new_fish)
        list_of_fishes = [x if x != -1 else 6 for x in list_of_fishes]
    return(list_of_fishes)

def simulate_fish_growth(given_list, days):
    if days == 0:
        print(f"Part 1 - Result: {len(given_list)}")
        return True
    new_list = decrease_all_values_by_one(given_list)
    new_list = add_new_fish(new_list)
    simulate_fish_growth(new_list, days-1)
    return False

simulate_fish_growth(fish_list, 80)
# This is not possible with 256 because it runs out of memory.
# I went through the following ideas to solve this.

## Day 6 - Part 2
# Idea 1: Create Fish Class - This did not work the way I wanted it

class Fish():
    days_to_spawn = 0
    descendants = 0

    def __init__(self, days_to_spawn):
        self.days_to_spawn = days_to_spawn

    def live_days(self, days):
        for day in range(days):
            self.live_a_day()

    def live_a_day(self):
        self.days_to_spawn = self.days_to_spawn - 1
        if self.days_to_spawn == 0:
            self.days_to_spawn = 6
            self.spawn_baby()

    def spawn_baby(self):
        self.descendants += 1

list_of_fish = []

for i in fish_list:
   list_of_fish.append(Fish(i))

for fish in list_of_fish:
   fish.live_days(80)

# print(len(list_of_fish)) always 300 

# Idea 2: Calculate how long it takes one fish, then add it up - No real result.
def calculate_spawns_for_days_lived(lived, to_live):
    spawns = 0
    # Do magic here
    return spawns 

# Idea 3 (and solution for part 2): Accumulate the amount of fish in one list and work with amounts.

fish_amount_list = []
for i in range(9):
    fish_amount_list.append(fish_list.count(i))

for i in range(256):
    fish_amount_list[7] += fish_amount_list[0]
    fish_amount_list.append(fish_amount_list.pop(0))

print(f"Part 2 - Result: {sum(fish_amount_list)}")