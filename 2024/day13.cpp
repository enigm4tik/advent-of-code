/*
 * Advent of Code - 2024
 * Day 13
 */

#include "aoc_utility.h"

int solveSystem(Coord &A, Coord &B, Coord &Prize)
{
	int a = 0;
	int b = 0;
	int result = 0;
	int b1 = (A.x * Prize.y) - (Prize.x * A.y);
	int b2 = (A.x * B.y) - (B.x * A.y);
	if (b1 % b2 != 0)
		return 0;
	else
		b = b1 / b2;
	int a1 = Prize.x - (B.x * b);
	if (a1 % A.x != 0)
		return 0;
	else
		a = a1 / (A.x);
	if (a > 100 || b > 100)
		return 0;

	result = (a * 3) + b;
	return result;
}

long long solveSystem(Coord &A, Coord &B, Coord &Prize, long long &measurementError)
{
	long long a = 0;
	long long b = 0;
	long long result = 0;
	long long b1 = (A.x * (Prize.y + measurementError)) - ((Prize.x + measurementError) * A.y);
	long long b2 = (A.x * B.y) - (B.x * A.y);
	if (b1 % b2 != 0)
		return 0;
	else
		b = b1 / b2;
	long long a1 = (Prize.x + measurementError) - (B.x * b);
	if (a1 % A.x != 0)
		return 0;
	else
		a = a1 / (A.x);

	result = (a * 3) + b;
	return result;
}

void parseLinesToMachines(std::vector<std::string> &lines, std::vector<std::vector<Coord>> &machines)
{
	Coord A, B, Prize;
	int x, y;
	for (std::string line : lines)
	{
		if (line.find('A') != std::string::npos)
		{
			x = stoi(splitLineToString(line, "X+")[1]);
			y = stoi(splitLineToString(line, "Y+")[1]);
			A = Coord(x, y);
			continue;
		}

		if (line.find("B:") != std::string::npos)
		{
			x = stoi(splitLineToString(line, "X+")[1]);
			y = stoi(splitLineToString(line, "Y+")[1]);
			B = Coord(x, y);

		}

		if (line.find('P') != std::string::npos)
		{
			x = stoi(splitLineToString(line, "X=")[1]);
			y = stoi(splitLineToString(line, "Y=")[1]);
			Prize = Coord(x, y);
			machines.push_back({ A, B, Prize });
		}
	}
}

int main()
{
	std::vector<std::string> lines = getLines("input.txt");
	std::vector<std::vector<Coord>> machines;

	parseLinesToMachines(lines, machines);

	int part1 = 0;
	for (std::vector<Coord> machine : machines)
	{
		part1 += solveSystem(machine[0], machine[1], machine[2]);
	}
	preResults(13, 2024);
	std::cout << "Part 1: " << part1 << "\n";

	long long part2 = 0;
	long long measurementError = 10000000000000;

	for (std::vector<Coord> machine : machines)
	{
		part2 += solveSystem(machine[0], machine[1], machine[2], measurementError);
	}

	std::cout << "Part 2: " << part2 << "\n";
	afterResults();

	return 0;
}