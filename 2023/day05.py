# Advent of Code - 2023
## Day 5

import itertools

def navigate_lists(source_id, list_of_maps):
    """
    Find the corresponding destination id for a given source id
    according to a list of mappings.
    :param source_id: integer
    :param list_of_maps: list of strings
    :return: integer
    """
    result = source_id
    for mapping in list_of_maps[1:]:
        destination, source, range = [int(i) for i in mapping.split(' ')]
        if source_id < source: 
            continue
        elif source_id >= source and source_id <= source + range: 
            result = destination + source_id - source
            return result 
    return result   


def determine_minimal_location(list_of_seeds):
    """
    Calculate the minimal location by going through multiple
    iterations of map comparisons. 
    :param list_of_seeds: list of integers
    :return: integer
    """
    minimal_location = 10000000000 #arbitrary big number
    for seed in list_of_seeds:
        soil = navigate_lists(seed, parsed_lines[1])
        fertilizer = navigate_lists(soil, parsed_lines[2])
        water = navigate_lists(fertilizer, parsed_lines[3])
        light = navigate_lists(water, parsed_lines[4])
        temperature = navigate_lists(light, parsed_lines[5])
        humidity = navigate_lists(temperature, parsed_lines[6])
        location = navigate_lists(humidity, parsed_lines[7])
        if location < minimal_location:
            minimal_location = location
    return minimal_location     
            

def get_ranges(mappings):
    """
    Create a dictionary for all mappings in a map section (input).
    :param mappings: list of strings
    :return: dictionary {destination: (source_start, source_end)}
    """
    dictionary = {}
    for mapping in mappings[1:]:
        destination, source, range_ = [int(i) for i in mapping.split(' ')]
        dictionary[destination] = (source, source + range_)
    return dictionary


def one_iteration(list_of_seeds, map_to_check):
    """
    Figuring out the ranges of sources to map them to ranges of destinations.
    There are 4 different cases: 
    1) the source is completely enveloped in the mapping
    2) the source has a left overlap
    3) the source has a right overlap
    4) the source has an overlap on each side 
    :param list_of_seeds: list of tuples (start_of_range, end_of_range)
    :param map_to_check: dictionary {destination: (source_start, source_end)}
    :result: list of tuples
    """
    seeds_to_process = []
    seen_seeds = []
    while list_of_seeds:
        seed = list_of_seeds[0]
        if not seed in seen_seeds:
            seen_seeds.append(seed)
        else:
            seen_seeds.remove(seed)
            list_of_seeds.remove(seed)
            continue
        seed_start, seed_end = seed
        for mapping in map_to_check:        
            map_start, map_end = map_to_check[mapping]
            # no overhang
            if seed_start >= map_start and seed_end < map_end: 
                new_seed = (seed_start - map_start + mapping-1, seed_end - map_start + mapping)                         
                if not new_seed in seeds_to_process:
                     seeds_to_process.append(new_seed)
                list_of_seeds.remove(seed)
                seen_seeds.remove(seed)
                break
            # left overhang
            if seed_start < map_start and seed_end < map_end and seed_end > map_start:
                new_seed = (seed_start, map_start-1)
                if not new_seed in list_of_seeds:
                    list_of_seeds.append(new_seed)
                list_of_seeds.remove(seed)
                new_seed = (mapping, seed_end - map_start + mapping)
                if not new_seed in seeds_to_process:
                     seeds_to_process.append(new_seed)
                seen_seeds.remove(seed)
                break
            #right overhang
            if seed_start > map_start and seed_end > map_end and seed_start < map_end:
                list_of_seeds.remove(seed)
                new_seed = (map_end+1, seed_end)
                if not new_seed in list_of_seeds:
                    list_of_seeds.append(new_seed)
                new_seed = (seed_start - map_start + mapping, map_end -map_start + mapping)
                if not new_seed in seeds_to_process:
                    seeds_to_process.append(new_seed)
                seen_seeds.remove(seed)
                break
            #overhangs on both sides
            if seed_start < map_start and seed_end > map_end:
                list_of_seeds.remove(seed)
                new_seed = (seed_start, map_start-1)
                if not new_seed in list_of_seeds:
                    list_of_seeds.append(new_seed)
                new_seed = (map_end+1, seed_end)
                if not new_seed in list_of_seeds:
                    list_of_seeds.append(new_seed)
                new_seed = (mapping, seed_end-seed_start+mapping)
                if not new_seed in seeds_to_process:
                    seeds_to_process.append(new_seed)
                seen_seeds.remove(seed)
                break
        if seed in seen_seeds:
            for seed in seen_seeds:
                seeds_to_process.append(seed)
    return list(set(seeds_to_process))


def all_iterations():
    """
    Iterating through all mappings to find the smallest location.
    :return: integer
    """
    list_of_seeds = []
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        seed_range = seeds[i+1]
        list_of_seeds.append((start, start+seed_range-1))

    seed_to_soil = get_ranges(parsed_lines[1])
    soil_to_fertilizer = get_ranges(parsed_lines[2])
    fertilizer_to_water = get_ranges(parsed_lines[3])
    water_to_light = get_ranges(parsed_lines[4])
    light_to_temperature = get_ranges(parsed_lines[5])
    temperature_to_humidity = get_ranges(parsed_lines[6])
    humidity_to_location = get_ranges(parsed_lines[7])
    list_of_maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

    for mapping in list_of_maps:
        list_of_seeds = one_iteration(list_of_seeds, mapping)
    return(min(list_of_seeds)[0])

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

grouper = itertools.groupby(lines, key= lambda x: x == "") #separate the list by newline
parsed_lines = [list(j) for i, j in grouper if not i]

seeds = [int(i) for i in parsed_lines[0][0].split(':')[1].split(' ') if not i == ""]

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 5':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {determine_minimal_location(seeds):^55}")
print(f"Part 2: {all_iterations():^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")