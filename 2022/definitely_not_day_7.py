## Full disclaimer
# this code definitely does not work
# I learned a lot about dictionaries though, so I'll keep this up :D

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip().split(" ") for line in lines]


def scan_dir(directory_name, operations):
    contents = {}
    for index, line in enumerate(operations):
        if {directory_name, "$"}.issubset(line):
            i = 2
            next_command_found = False
            while not next_command_found and i < len(lines) - index:
                next_line = lines[index + i]
                if not next_line[0] == '$':
                    contents[next_line[1]] = next_line[0]
                    i += 1
                else:
                    next_command_found = True
    return contents


def dict_walk(d, item):
    for k, v in d.items():
        if type(v) == dict:
            dict_walk(v, item)
        else:
            if item == k:
                d[k] = scan_dir(k, lines)
    return d


def check_for_existence(d):
    for k, v in d.items():
        if type(v) == dict:
            yield k
            yield from check_for_existence(v)

current_path = []
file_system = {}
seen_directories = []
for index, line in enumerate(lines):
    if index == 0:
        continue
    if line[0] == "dir":
        print("found directory: ", line[1])
        directory = line[1]
        joined_path = "".join(current_path)
        file_system = dict_walk(file_system, directory)
        seen = set(check_for_existence(file_system))
        seen_directories = list(set(seen_directories).union(seen))
        if directory not in file_system and directory not in seen_directories:
            file_system[directory] = scan_dir(directory, lines)
    if line[1] == "cd":
        if line[2] == "..":
            current_path.pop()
        else:
            current_path.append(line[2])

# print(file_system)

def folders(d, directory):
    for k, v in d.items():
        if type(v) == dict:
            if k == directory:
                yield v
            yield from folders(v, directory)


def calculate_size(folder, subfolder, partial_sum=0):
    result = list(folders(folder, subfolder))
    checking = list(check_for_existence(result[0]))
    for value in result[0].values():
        try:
            partial_sum += int(value)
        except TypeError:
            continue
    if checking:
        return calculate_size(result[0], checking[0], partial_sum)
    else:
        return partial_sum

print("calculating sums")
sum_of_directories = {}
for directory in seen_directories:
    sum_of_directories[directory] = calculate_size(file_system, directory)

def part1(folder_sums):
    print(folder_sums)
    result = 0
    for folder_sum in folder_sums.values():
        if folder_sum < 100000:
            result += folder_sum
    print(result)

part1(sum_of_directories)