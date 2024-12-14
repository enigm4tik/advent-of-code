/*
 * Advent of Code - 2024
 * Day 14
 */

#include "aoc_utility.h"

void parseInputDay14(std::vector<std::vector<std::string>> &input, std::vector<std::pair<Coord, Coord>> &machineVelocityPairs)
{
	Coord robot;
	Coord velocity;
	std::string tempString;
	std::vector<int> tempVector;
	for (int i = 0; i < input.size(); i++)
	{
		tempString = splitLineToString(input[i][0], "=")[1];
		tempVector = splitLineToInt(tempString, ',');
		robot = Coord(tempVector[1], tempVector[0]);
		tempString = splitLineToString(input[i][1], "=")[1];
		tempVector = splitLineToInt(tempString, ',');
		velocity = Coord(tempVector[1], tempVector[0]);
		std::pair<Coord, Coord> mvPair = std::make_pair(robot, velocity);
		machineVelocityPairs.push_back(mvPair);
	}
}

std::vector<Coord> moveRobots(std::vector<std::pair<Coord, Coord>>& machineVelocityPairs, int width, int height, long long steps)
{
	std::vector<Coord> positions;
	Coord robot;
	int x = 0;
	int y = 0;
	for (std::pair<Coord, Coord> machine : machineVelocityPairs)
	{
		x = (machine.first.x + steps * machine.second.x) % width;
		y = (machine.first.y + steps * machine.second.y) % height;
		if (x < 0)
			x = width + x;
		if (y < 0)
			y = height + y;

		robot = Coord(x, y);
		positions.push_back(robot);
	}
	return positions;
}

long long calculateSafetyFactor(std::vector<Coord> &positions, int width, int height)
{
	int q1 = 0, q2 = 0, q3 = 0, q4 = 0;
	int middle = 0;
	for (Coord robot : positions)
	{
		if (robot.x < width / 2 && robot.y < height / 2)
			q1++;
		if (robot.x < width / 2 && robot.y > height / 2)
			q2++;
		if (robot.x > width / 2 && robot.y < height / 2)
			q3++;
		if (robot.x > width / 2 && robot.y > height / 2)
			q4++;
		if (robot.x == width / 2 || robot.y == height / 2)
			middle++;
	}

	long long result = q1 * q2 * q3 * q4;
	return result;
}

void printRobots(std::vector<Coord>& robots, int width, int height)
{
	for (int i = 0; i < width; i++)
	{
		for (int j = 0; j < width; j++)
		{
			if (std::find(robots.begin(), robots.end(), Coord(i, j)) != robots.end())
				std::cout << "#";
			else
				std::cout << ".";
		}
		std::cout << "\n";
	}
	std::cout << "\n";
}

int main()
{
	std::vector<std::string> lines = getLines("input.txt");
	std::vector<std::vector<std::string>> input = splitToString(lines, " ");
	std::vector<std::pair<Coord, Coord>> machineVelocityPairs;

	parseInputDay14(input, machineVelocityPairs);

	int width = 103; //7
	int height = 101; //11

	std::vector<Coord> positions = moveRobots(machineVelocityPairs, width, height, 100);
	long long part1 = calculateSafetyFactor(positions, width, height);

	std::vector<Coord> current;
	long long best = 9999999999999999; 
	int i = 0;
	int bestSteps = 0;
	while (i < 10000) // arbitrarily chosen number
	{
		current = moveRobots(machineVelocityPairs, width, height, i);
		long long calculated = calculateSafetyFactor(current, width, height);
		if (calculated < best)
		{
			best = calculated;
			bestSteps = i;
		}
		i++;
	}
	
	current = moveRobots(machineVelocityPairs, width, height, bestSteps);
	printRobots(current, width, height);

	preResults(14, 2024);
	std::cout << "Part 1: " << part1 << std::endl;
	std::cout << "Part 2: " << bestSteps << std::endl;
	afterResults();

	return 0;
}