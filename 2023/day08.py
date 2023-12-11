# Advent of Code - 2023
## Day 8

import itertools
import math

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

lookup_map = {}
for line in lines[2:]:
    key, value = [x.strip() for x in line.split('=')]
    val, lue = [x.strip() for x in value[1:-1].split(',')]
    lookup_map[key] = (val, lue)

instruction = lines[0]

def determine_steps(node_name, instruction, step_map):
    """
    Determine the steps needed to move from solution to
    an end (xxZ).
    :param node_name: string
    :param instruction: string
    :param step_map: dictionary {node_name: (node_name, node_name)}
    :return: 
    """
    steps = 0
    for i in itertools.cycle(instruction):
        if i == 'L':
            node_name = step_map[node_name][0]
        else: 
            node_name = step_map[node_name][1]
        steps += 1
        if node_name.endswith('Z'):
            break
    return steps

def create_prime_list(n):
    """
    Taken from SO: https://stackoverflow.com/a/39106237/10041092
    Fast algorithm to create a list of prime numbers
    :param n: integer, upper end
    :return: list of prime numbers
    """
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

def prime_factorization(number, primes):
    """
    Determine all prime factors of a number.
    :param number: integer
    :param primes: list of prime factors
    :return list (prime factors that make up number)
    """
    prime_factors = []
    for prime in primes:
        if number % prime == 0:
            prime_factors.append(prime)
        if math.prod(prime_factors) == number:
            break
    return prime_factors

# Part 1:
part1 = determine_steps('AAA', instruction, lookup_map)

# Part 2:
all_starts = [start for start in lookup_map.keys() if start.endswith('A')]
required_steps = []
for start in all_starts:
    required_steps.append(determine_steps(start, instruction, lookup_map))

primes = create_prime_list(1000)

result_list = []
for number in required_steps:
    prime_factors = prime_factorization(number, primes)
    result_list += prime_factors

result_list = list(set(result_list))
part2 = 1 
for u in result_list:
    part2 *= u

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 8':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1:^55}")
print(f"Part 2: {part2:^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")
