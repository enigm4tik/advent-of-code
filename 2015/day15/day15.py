# Advent of Code - 2015
## Day 15

import itertools

def prepare_data(line):
    result = {}
    exploded_results = line.split(" ")
    ingredient = exploded_results.pop(0)
    properties = {}
    for i in range(0, len(exploded_results)-1, 2):
        property = exploded_results[i]
        value = exploded_results[i+1].rstrip()
        if value.endswith(','):
            value = value[:-1]
        value = int(value)
        properties[property] = value
    result[ingredient] = properties
    return result

class Ingredient():
    name = ""
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    highest_priority = ''

    def __init__(self, ingredient) -> None:
        for key, value in ingredient.items():
            self.name = key[:-1]
            self.capacity = value['capacity']
            self.durability = value['durability']
            self.flavor = value['flavor']
            self.texture = value['texture']
            self.calories = value['calories']
            self.highest_priority = max(value.values())

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [Ingredient(prepare_data(line)) for line in lines]

numbers = range(1, 100)
target = 100
results = []
for i in itertools.combinations_with_replacement(numbers, 4):
    if sum(i) == target:
        results.append(i)


def determine_possible_solution(iteration):
    a, b, c, d = iteration
    # a, b = iteration
    # if a < 5 * c and c < d and b < 2 * a and c < 5 * b:
    # print(a, b, c, d)
    # print(2*d > 0, ((5*c)-(2*d)-b > 0), 5*b > 2*a, 4*a > c)
    # print( 2*d > 0 and ((5*c)-(2*d)-b > 0) and 5*b > 2*a and 4*a > c)
    # print(4*a-1*c > 0 and (-2)*a + 5*b > 0 and (-1)*b + 5*c -2*d > 0 and 2*d > 0)
    # if 4*a-1*c > 0 and (-2)*a + 5*b > 0 and 5*c -2*d -b > 0 and 2*d > 0:
    # # if 2*b > a and 3*b > 2*a and 3*a > 2*b and 3*a > b: 
    #     return True
    # else:
    #     return False
    return True


def calculate_score_for_solution(iteration, ingredients):
    a, b, c, d = iteration
    # a, b = iteration
    result = []
    frosting = ingredients[0]
    candy = ingredients[1]
    butterscotch = ingredients[2]
    sugar = ingredients[3]
    for i in range(4):
        # a, b = b, a
        a, b, c, d = b, c, d, a
        # calculated_calories =  a * frosting.calories + b * candy.calories + c * butterscotch.calories + d * sugar.calories
        # if not calculated_calories == 500:
        #     result.append(0)
        #     continue
        # else: 
        calculated_capacity = a * frosting.capacity + b * candy.capacity + c * butterscotch.capacity + d * sugar.capacity
        calculated_durability = a * frosting.durability + b * candy.durability + c * butterscotch.durability + d * sugar.durability
        calculated_flavor = a * frosting.flavor + b * candy.flavor + c * butterscotch.flavor + d * sugar.flavor
        calculated_texture = a * frosting.texture + b * candy.texture + c * butterscotch.texture + d * sugar.texture
        if any(x < 0 for x in [calculated_flavor, calculated_capacity, calculated_texture, calculated_durability]):
            result.append(0)
            continue
        else:
            calculated_result = calculated_capacity * calculated_durability * calculated_flavor * calculated_texture
            result.append(calculated_result)

    return max(result)

best_score = 0

for result in results: 
    new_score = calculate_score_for_solution(result, lines)
    if new_score > best_score:    
        best_score = new_score

print(best_score)