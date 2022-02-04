# Advent of Code - 2015
## Day 14

from math import floor

class Reindeer: 
    name = ""
    speed = 0
    time = 0
    rest = 0
    awards = 0
    traveled_distance = 0

    def __init__(self, reindeer) -> None:
        self.name = reindeer[0]
        self.speed = int(reindeer[3])
        self.time = int(reindeer[6])
        self.rest = int(reindeer[-2])
        self.run_rest = self.time + self.rest

    def run_for_x_seconds(self, seconds):
        runs = floor(seconds / self.run_rest)
        time_left = seconds % self.run_rest
        if time_left > self.time:
            runs += 1
            time_left -= self.time
        return runs * self.speed * self.time

    def calculate_travel_distance(self, seconds):
        time_left = seconds % self.run_rest 
        runs = floor(seconds / self.run_rest)
        self.traveled_distance = runs * self.speed * self.time
        if time_left and time_left < self.time:
            self.traveled_distance += time_left * self.speed
        elif time_left > self.time: 
            self.traveled_distance += self.speed * self.time 
        elif time_left % self.time == 0:
            self.traveled_distance += int(time_left/self.time) * self.speed * self.time
        return self.traveled_distance

    def award_point(self):
        self.awards += 1

# with open('test_input') as file:
with open('puzzle_input') as file:
    lines = file.readlines()
    lines = [line.rstrip().split(" ") for line in lines]

reindeers = []
for line in lines: 
    reindeers.append(Reindeer(line))

reindeer_distances = {}
reindeer2 = {}
for reindeer in reindeers:
    reindeer_distances[reindeer.name] = reindeer.run_for_x_seconds(2503)

print(f"Part 1: {reindeer_distances[max(reindeer_distances)]}")

for i in range(2503):
    for reindeer in reindeers:
        reindeer.calculate_travel_distance(i)
    current_lead_distance = max([reindeer.traveled_distance for reindeer in reindeers])
    for reindeer in reindeers:
        if reindeer.traveled_distance == current_lead_distance:
            reindeer.award_point()

results_for_part2 = []
for reindeer in reindeers:
    results_for_part2.append(reindeer.awards)

print(f"Part 2: {max(results_for_part2) - 1}")