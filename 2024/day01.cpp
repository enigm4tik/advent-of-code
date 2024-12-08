/*
 * Advent of Code - 2024
 * Day 1
 */

#include "aoc_utility.h"

static void part1(std::vector<int> &firstList, std::vector<int> &secondList)
{
	// sort lists
	sort(firstList.begin(), firstList.end());
	sort(secondList.begin(), secondList.end());

	int sumofdistances = 0;

	for (int i = 0; i < firstList.size(); i++)
	{
		int result;
		if (secondList[i] < firstList[i])
			result = (firstList[i] - secondList[i]);
		else
			result = (secondList[i] - firstList[i]);
		sumofdistances += result;
	}

	std::cout << "Part 1: " << sumofdistances << std::endl;
}

static void part2(std::vector<int> &firstList, std::vector<int> &secondList)
{
	int similarity = 0;
	for (int i = 0; i < firstList.size(); i++)
	{
		int multiplier = count(secondList.begin(), secondList.end(), firstList[i]);	
		similarity += firstList[i] * multiplier;
	}
	std::cout << "Part 2: " << similarity << std::endl;
}

int main()
{
	std::vector<std::string> lines = getLines("puzzle.txt");
	std::vector<int> firstList;
	std::vector<int> secondList;
	std::string delimiter = "   ";
	int SIZE = 5;

	for (std::string line : lines)
	{
		firstList.push_back(std::stoi(line.substr(0, SIZE)));
		auto second = line.find_first_not_of(' ', SIZE+1);
		secondList.push_back(stoi(line.substr(second, SIZE)));
	}

	preResults(1, 2024);
	part1(firstList, secondList);
	part2(firstList, secondList);
	afterResults();
	return 0;
}