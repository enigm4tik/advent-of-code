# Advent of Code - 2023
## Day 2

with open('puzzle_input') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    games = create_games(lines)

class Pull: 
    order = 0
    red = 0
    blue = 0
    green = 0

    def __init__(self, order, game):
        """
        Initialize each pull with the amount of cubes pulled
        :param order: number of pull (turned out to be irrelevant)
        :param game: list of values and colors
        """
        self.order = order
        for id, value in enumerate(game): 
            if value == "red" or value == "red,":
                self.red = int(game[id-1])
            if value == "blue" or value == "blue,":
                self.blue = int(game[id-1])
            if value == "green" or value == "green,": 
                self.green = int(game[id-1])
            
    def __str__(self):   
        return f"Pull#{self.order}: Red - {self.red}, Green - {self.green}, Blue - {self.blue}"
    
    def __repr__(self):
        return f"Pull#{self.order}: Red - {self.red}, Green - {self.green}, Blue - {self.blue}"
    
    def is_game_possible(self, red, green, blue):
        """
        Determining if the maximum seen cubes is higher than the maximum given cubes.
        :param red, green, blue: integers, maximum allowed numbers of cubes
        """
        if self.red <= red and self.blue <= blue and self.green <= green:
            return True 
        return False
    

def create_games(lines):
    """
    Parse the given lines into games containing pull objects.
    :param lines: list of strings
    :return: dictionary of lists of pull objects
    """
    games = {}
    for line in lines: 
        game_id, pulls = line.split(':')
        pulls = [pull.lstrip().split(' ') for pull in pulls.lstrip().split(";")]
        game_id = game_id.strip().split("Game ")[1]
        for i, pull in enumerate(pulls):
            try: 
                games[game_id].append(Pull(i, pull))
            except KeyError:
                games[game_id] = [Pull(i, pull)]
    return games 


def find_sum_of_possible_games(games):
    """
    Calculate the sum of ids of possible games.
    Games are possible if red, green, blue <= 12, 13, 14 (per definition)
    :param games: dictionary of lists of pull objects
    :return: integer, sum of ids of possible games
    """
    possible_games = [int(game) for game in games.keys()]
    for game, pulls in games.items(): 
        for pull in pulls: 
            if not pull.is_game_possible(12, 13, 14):
                possible_games.remove(int(game))
                break
    return sum(possible_games)

# Part 2

def calculate_power_of_cubes(games):
    """
    Calculate the minimal amount of cubes necessary. 
    Multiply their values and sum them up
    :param games: dictionary of lists of pull objects
    :return: integer, sum of power of cubes
    """
    sum_of_power = 0
    for pulls in games.values(): 
        red = blue = green = 0
        for pull in pulls:
            if pull.red > red: 
                red = pull.red 
            if pull.blue > blue:
                blue = pull.blue
            if pull.green > green:
                green = pull.green

        power = green * red * blue
        sum_of_power += power   
    return sum_of_power

part1 = find_sum_of_possible_games(games)
part2 = calculate_power_of_cubes(games)

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 2':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1:^55}")
print(f"Part 2: {part2:^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")