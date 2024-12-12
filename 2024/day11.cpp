/*
 * Advent of Code - 2024
 * Day 11
 */

#include "aoc_utility.h"

std::vector<long long> getNewEngravings(long long number)
{
	std::vector<long long> returnVector;
	if (number == 0)
	{
		returnVector.push_back(1);
		return returnVector;
	}

	std::string representation = std::to_string(number);

	if (representation.length() % 2 == 0)
	{
		long long left = stoll(representation.substr(0, representation.length() / 2));
		long long right = stoll(representation.substr(representation.length() / 2));

		returnVector.push_back(left);
		returnVector.push_back(right);
		return returnVector;
	}

	returnVector.push_back(number * 2024);
	return returnVector;
}

void engraveStones(std::unordered_map<long long, long long>& stones)
{
	std::unordered_map<long long, long long> newStones;
	for (auto key : stones)
	{
		std::vector<long long> stonesToAdd = getNewEngravings(key.first);

		for (auto stoneToAdd : stonesToAdd)
		{
			if (newStones.find(stoneToAdd) == newStones.end())
				newStones[stoneToAdd] = stones[key.first];
			else
				newStones[stoneToAdd] += stones[key.first];
		}
	}
	stones = newStones;
}

long long turnStones(std::unordered_map<long long, long long> stones, long long steps)
{
	for (int i = 1; i < steps + 1; i++)
		engraveStones(stones);

	long long stoneAmount = 0;
	for (auto stone : stones)
		stoneAmount += stone.second;

	return stoneAmount;
}


int main()
{
	std::vector<std::string> lines = getLines("input.txt");
	std::vector<int> initialStones = splitLineToInt(lines[0], ' ');
	std::unordered_map<long long, long long> stones;

	for (long long stone : initialStones)
		stones[stone] = 1;

	long long part1 = turnStones(stones, 25);
	long long part2 = turnStones(stones, 75);

	preResults(11, 2024);
	std::cout << part1 << std::endl;
	std::cout << part2 << std::endl;
	afterResults();

	return 0;
}