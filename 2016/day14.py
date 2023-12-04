# Advent of Code - 2016
## Day 14
import hashlib
import re

hash_salt = 'ihaygndm'
hash_i = 0

def calculate_a_hash(hash_salt=hash_salt, string_index=hash_i, stretch=False):
    hash_salt += str(string_index)
    result = hashlib.md5(hash_salt.encode())
    result = result.hexdigest()
    if stretch:
        result = stretch_key_2016_times(result)
    return result 


def stretch_key_2016_times(hex_hash):
    for i in range(2016):
        hex_hash = hashlib.md5(hex_hash.encode())
        hex_hash = hex_hash.hexdigest()
    return hex_hash


def find_3_hash_contender(hex_hash):
    pattern = r'(.)\1{2}'
    found_pattern = re.findall(pattern, hex_hash)
    if found_pattern:
        return found_pattern[0]
    else:
        return False


def find_5_hash_contender(hex_hash):
    pattern = r'(.)\1{4}'
    found_pattern = re.findall(pattern, hex_hash)
    if found_pattern:
        return found_pattern[0]
    else:
        return False

def find_5_hashes_in_1000(hex_index, last_found_hash=0, stretch=False):
    upper_limit = hex_index + 1000
    for i in range(last_found_hash, upper_limit):
        calculated_hash = calculate_a_hash(string_index=i, stretch=stretch)
        found_five_hash = find_5_hash_contender(calculated_hash)
        found_three_hash = find_3_hash_contender(calculated_hash)
        if found_five_hash: 
            if not i in five_hashes:
                five_hashes[i] = found_five_hash[0]
        if found_three_hash:
            if not i in three_hashes:
                three_hashes[i] = found_three_hash[0]


def check_validity(hex_index):
    character = three_hashes[hex_index]
    validity = {k:v for k, v in five_hashes.items() if k > hex_index and k <= hex_index+1000 and v == character}
    if validity:
        return True
    else:
        return False

three_hashes = {}
five_hashes = {}
def day14(hash_i=hash_i, stretch=False):
    valid_keys = []
    first_3_hash_found = False
    while len(valid_keys) != 64:
        if not first_3_hash_found:
            calculated_hash = calculate_a_hash(string_index=hash_i, stretch=stretch)
            contender = find_3_hash_contender(calculated_hash)
            if contender:
                find_5_hashes_in_1000(hash_i, stretch=stretch)
                if check_validity(hash_i):
                    valid_keys.append(hash_i)
                    first_3_hash_found = True
            hash_i += 1
        else:
            next_iteration = min(three_hashes.keys())
            max_iteration = max(three_hashes.keys())
            if not max_iteration: 
                max_iteration = 0
            find_5_hashes_in_1000(next_iteration, max_iteration, stretch=stretch)
            if check_validity(next_iteration):
                if not next_iteration in valid_keys:
                    valid_keys.append(next_iteration)
            three_hashes.pop(next_iteration)

    return valid_keys[63]

# print(f'Part 1: {day14()}')
print(f'Part 2: {day14(stretch=True)}')