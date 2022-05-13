# Advent of Code - 2016
## Day 10

import numpy as np

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

bots = {}
instructions = {}
list_of_bots = []

def parse_input(line):
    if line.startswith('value'):
        array = line.split()   
        botnr = array[-1]
        botnr = 'bot ' + botnr
        value = int(array[1])
        if botnr in bots:
            bots[botnr].append(value)
        else:
            bots[botnr] = [value]
        if botnr not in list_of_bots:
            list_of_bots.append(botnr)
    else:
        line = line.replace('gives low to ', '#')
        line = line.replace('and high to ', '#')
        executor, low, high = line.split('#')
        instructions[executor.strip()] = {"low": low.strip(), "high": high.strip()}


def execute_instruction(bot):
    bot_values = bots[bot]
    high_value = max(bot_values)
    low_value = min(bot_values)
    low, high = instructions[bot].values()
    distribute_values_to_bots(high, high_value)
    distribute_values_to_bots(low, low_value)
    list_of_bots.remove(bot)


def distribute_values_to_bots(bot, bot_value):
    if bot in bots:
        bots[bot].append(bot_value)
    else:
        bots[bot] = [bot_value]
    if not bot in list_of_bots and not bot.startswith('output'):
        list_of_bots.append(bot)


def find_responsible_bot():
    for bot, bot_values in bots.items():
        if set([61, 17]) == set(bot_values):
            bot_number = bot.split()[1]
            return bot_number


def multiply_outputs():
    resulting_values = [bots['output ' + str(i)][0] for i in range(3)]
    result = np.prod(resulting_values)
    return result

for line in lines:
    parse_input(line)

while list_of_bots:
    for bot in list_of_bots:
        if len(bots[bot]) == 2:
            execute_instruction(bot)

print(f"Part 1: {find_responsible_bot()}")
print(f"Part 2: {multiply_outputs()}")