# Advent of Code - 2021
## Day 3 - Part 1

with open('day03_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def find_most_and_least_common_bit(input_string, evaluate_equal=False, get_gamma=False):
    string_len = len(input_string)
    zeroes = sum('0' in s for s in input_string)
    ones = string_len - zeroes
    if ones > zeroes: 
        most_common_bit = '1'
        least_common_bit = '0'
    elif get_gamma and ones == zeroes and evaluate_equal:
        most_common_bit = least_common_bit = '1'
    elif not get_gamma and ones == zeroes and evaluate_equal: 
        most_common_bit = least_common_bit = '0'
    else:
        most_common_bit = '0'
        least_common_bit = '1'
    return most_common_bit, least_common_bit

def calculate_binary_values(lines, get_gamma=False, evaluate_equal=False):
    gamma = ''
    epsilon = ''
    output = {}
    for line in lines:
        for bit in range(len(line)):
            if bit in output:
                output[bit] = output[bit] + line[bit]
            else: 
                output[bit] = line[bit]

    for i in range(len(line)):
        gamma_bit, epsilon_bit = find_most_and_least_common_bit(output[i], evaluate_equal=evaluate_equal, get_gamma=get_gamma)
        gamma += gamma_bit
        epsilon += epsilon_bit
    if get_gamma: 
        return gamma
    else:
        return epsilon

def binary_to_decimal(binary_value):
    return int(binary_value, 2)

epsilon = calculate_binary_values(lines)
gamma = calculate_binary_values(lines, get_gamma=True)

decimal_epsilon = binary_to_decimal(epsilon)
decimal_gamma = binary_to_decimal(gamma)

print(f"Part 1 - Result: {decimal_epsilon * decimal_gamma}")

## Day 3 - Part 2

def filter_list_by_common_bits(input_list, common_bits, get_gamma=False, iteration=0):
    if len(input_list) == 1:
        return input_list[0]
    while iteration <= len(input_list[0]):
        filtered = filter(lambda c: c[iteration] == common_bits[iteration], input_list)
        filtered_list = list(filtered)
        new_epsilon = calculate_binary_values(filtered_list, get_gamma=get_gamma, evaluate_equal=True)
        return filter_list_by_common_bits(filtered_list, new_epsilon, get_gamma, iteration + 1)

oxy = filter_list_by_common_bits(lines, gamma, get_gamma=True)
co2 = filter_list_by_common_bits(lines, epsilon, get_gamma=False)

decimal_oxy = binary_to_decimal(oxy)
decimal_co2 = binary_to_decimal(co2)

print(f"Part 2 - Result: {decimal_oxy * decimal_co2}")
