# Advent of Code - 2022
## Day 7

class Folder:
    """
    A class representing a folder and its contents

    Attributes
    ----------
    :attr name: str, folder name
    :attr parent: str, folder name
    :attr children: list, files and folders contained in folder
    :attr path: str, path representation to get to folder
    :attr files_size: int, size of all files contained in folder
    :attr folders: list, list of folder names
    """

    def __init__(self, name):
        """
        Initialize an empty object with just a name
        :param name: str, name of the folder
        """
        self.name = name
        self.parent = None
        self.children = []
        self.path = None
        self.files_size = None
        self.folders = []

    def __str__(self):
        """
        :return: name of the folder
        """
        return self.name

    def add_children(self, child):
        """
        Helper function to add a child of a folder
        and calculate the updated sizes (if it's a file)
        :param child: either folder (dir) or file
        """
        self.children.append(child)
        self.calculate_my_files_size()

    def calculate_my_files_size(self):
        """
        Helper function to calculate the size of all files
        in the folder.
        """
        calculated_file_size = 0
        for child in self.children:
            try:
                calculated_file_size += int(child[0])
            except ValueError:
                if not child[1] in self.folders:
                    self.folders.append(child[1])
        self.files_size = calculated_file_size


def create_file_system(input_list):
    """
    Create a file system (list) of folder objects
    update each object line by line
    :param input_list: list, either file/folder or command
    :return: list, list of folder objects
    """
    file_system = []
    current_path = []
    index = 0
    while index < len(input_list):
        if input_list[index][1] == "ls":  # listing directory contents
            current_directory = input_list[index - 1][2]
            folder = Folder(current_directory)
            if len(current_path) < 2:  # root directory
                folder.parent = ''
            else:  # any other directory
                folder.parent = current_path[-2]
            folder.path = current_path[:-1]
            abort = False
            i = 1
            while not abort and i <= len(input_list) - index - 1:
                if input_list[index + i][0] != "$":
                    first, second = input_list[index + i]
                    folder.add_children([first, second])
                else:
                    abort = True
                i += 1
            file_system.append(folder)
        if lines[index][1] == "cd":  # movement through folders
            if lines[index][2] == "..":  # go back up
                current_path.pop()
            else:  # go into a folder
                current_path.append(lines[index][2])
        index += 1
    return file_system


def find_folder_with_parent(child, path, file_system):
    """
    Find a folder in the <file_system> with the correct path.
    :param child: str, name of child
    :param path: str, representation of path
    :param file_system: list of folder objects
    :return: correct folder object
    """
    for folder in file_system:
        if folder.name == child and folder.path == path:
            return folder


def collect_all_sizes(file_system):
    """
    Create a list of all folders and their sizes.
    Iterate over all folders in each folder and accumulate their sizes.
    :param file_system: list, list of folder objects
    :return: dict, {<folder.path>: size}
    """
    size_dictionary = {}

    for folder in file_system:
        size = folder.files_size
        folders_to_check = [(folder.name, foldy, folder.path + [folder.name]) for foldy in folder.folders]
        checked_folders = []
        while folders_to_check and not folders_to_check[0] in checked_folders:
            current_parent, current_folder_name, path = folders_to_check[0]
            current_folder = find_folder_with_parent(current_folder_name, path, file_system)
            try:
                if current_folder.folders:
                    folders_to_check.extend(
                        [(current_folder.name, foldy, current_folder.path + [current_folder.name]) for foldy in
                         current_folder.folders if foldy not in checked_folders])
                size += current_folder.files_size
            except AttributeError:
                pass
            checked_folders.append(folders_to_check.pop(0))
        size_dictionary["/".join(folder.path + [folder.name])] = size
    return size_dictionary


def part1(input_list):
    """
    Accumulate the sizes of all folders with size smaller than 100000.
    :param input_list: list, puzzle input
    :return: int, accumulated size of all folders with size < 100000.
    """
    file_system = create_file_system(input_list)
    sizes = collect_all_sizes(file_system)
    result = 0
    for size in sizes.values():
        if size < 100000:
            result += size
    return result


def part2(input_list):
    """
    Find smallest folder to delete to get to <needed_space>.
    :param input_list: list, puzzle input
    :return: size of smallest folder to be deleted
    """
    total_size = 70000000
    needed_space = 30000000
    file_system = create_file_system(input_list)
    sizes = collect_all_sizes(file_system)

    used_space = max(sizes.values())
    current_free_space = total_size - used_space
    space_to_free = needed_space - current_free_space

    list_of_sizes = sorted([val for val in sizes.values() if val >= space_to_free])
    smallest_folder_size = list_of_sizes[0]
    return smallest_folder_size


with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip().split(" ") for line in lines]

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2022 - Day 7':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1(lines)}")
print(f"Part 2: {part2(lines)}")
