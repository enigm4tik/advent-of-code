# Advent of Code - 2015
## Day 10

def get_elements(input_list, decay_dictionary):
    """
    Find all elements the input element decays into
    :param input: list of elements
    :param decay_dictionary: dictionary {element: elements.it.decays.into}
    :return: list of elements
    """
    result = []
    for element in input_list:
        listy = [x for x in decay_dictionary[element].split('.')]
        for item in listy:
            result.append(item)
    return result


def look_and_see(input_list, decay, conway, runs=40):
    elements = input_list
    for i in range(runs):
        elements = get_elements(elements, decay_dictionary=decay)

    length = 0
    for element in elements:
        length += len(conway[element])
    return length

# testinput in this case is a list of Conway's atomic elements
#[Wikipedia](https://en.wikipedia.org/wiki/Look-and-say_sequence#Cosmological_decay)

with open('day_10_conway', 'r') as file:  
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

conway = {} # dictionary {element: sequence}
decay_into = {} # dictionary {element: elements.it.decays.into}

for line in lines:
    _, element, sequence, decay, _ = line.split(" ")
    conway[element] = sequence
    decay_into[element] = decay

input = 'Yb' # element based on my input
elements = [input]

part1 = look_and_see(elements, decay_into, conway, 40)
part2 = look_and_see(elements, decay_into, conway, 50)

print(part1)
print(part2)