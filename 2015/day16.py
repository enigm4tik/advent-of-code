# Advent of Code - 2015
## Day 16

with open('puzzle_input') as file:
    lines = file.readlines()
    lines = [line.rstrip().split(', ') for line in lines]

class Aunt:
    number = 0
    children = None
    cats = None
    samoyeds = None
    pomeranians = None
    akitas = None
    vizslas = None
    goldfish = None
    trees = None
    cars = None
    perfumes = None

    def __init__(self, aunt_sue) -> None:
        for key, value in aunt_sue.items():
            self.number = key
            self.__dict__.update(value)


def prepare_data(aunt_sue): 
    return_dict = {}
    for index, value in enumerate(aunt_sue):
        if index == 0:
            sue, aunt_property, aunt_value = value.split(":")
            sue, number = sue.split(" ")
            return_dict[number] = {
                aunt_property.strip(): int(aunt_value.strip())
            }
        else:
            aunt_property, aunt_value = value.split(":")
            return_dict[number][aunt_property] = int(aunt_value.strip())
    return return_dict

all_aunts = []
for line in lines:
    all_aunts.append(Aunt(prepare_data(line)))

result_aunt = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

def compare_aunt(aunt_sue, part2 = False):
    for key, value in result_aunt.items():
        aunt_sue_property_value = getattr(aunt_sue, key)
        if aunt_sue_property_value is None:
            continue
        if part2:
            if key in ['cats', 'trees']:
                if aunt_sue_property_value > value:
                    continue
                else:
                    return False
            elif key in ['pomeranians', 'goldfish']:
                if aunt_sue_property_value < value:
                    continue
                else:
                    return False
        if aunt_sue_property_value == value:
            continue
        else:
            return False
    return True

part1 = 0
part2 = 0
for aunt in all_aunts:
    if compare_aunt(aunt):
        part1 = aunt.number
    if compare_aunt(aunt, True):
        part2 = aunt.number

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
