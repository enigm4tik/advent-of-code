/*
 * Advent of Code - 2024
 * Day 3
 * REMEMBER: substr(position, length) NOT substr(begin, end)
 */

#include "aoc_utility.h"

int part1(std::string &lines)
{
	std::vector<std::string> leftSplit = splitLineToString(lines, "mul(");
	std::vector<std::vector<std::string>> listofCandidateLists = splitToString(leftSplit, ")");

	std::vector<int> numbers;
	int part1Sum = 0;
	for (auto candidateList : listofCandidateLists)
	{
		for (auto candidate : candidateList)
		{
			if (candidate.size())
			{
				numbers = splitLineToInt(candidate, ',');
				if (numbers.size() == 2)
				{
					std::string additionalTest = std::to_string(numbers[0]) + "," + std::to_string(numbers[1]);
					//eg. "329,480*from(" yields 329 and 480 by splitting on ','
					if (additionalTest.size() == candidate.size())
					{
						part1Sum += numbers[0] * numbers[1];
					}
				}
			}
		}
	}
	return part1Sum;
}

int part2(std::string lines)
{
	std::vector<int> alldos = findSubstringPositions(lines, "do()");
	std::vector<int> alldonts = findSubstringPositions(lines, "don't()");

	int stringPos = 0;
	int multiply = false;
	std::string part2Substring;
	auto found = std::find_if(alldonts.begin(), alldonts.end(), [stringPos](int a) {return a > stringPos; });
	int part2Sum = 0;
	while (stringPos < lines.length())
	{
		part2Substring = lines.substr(stringPos, *found - stringPos);
		stringPos = *found;
		if (multiply)
		{
			found = std::find_if(alldonts.begin(), alldonts.end(), [stringPos](int a) {return a > stringPos; });
			multiply = false;
		}
		else
		{
			part2Sum += part1(part2Substring);
			found = std::find_if(alldos.begin(), alldos.end(), [stringPos](int a) {return a > stringPos; });
			multiply = true;
		}
	}
	return part2Sum;
}

int main()
{
	std::vector<std::string> lines = getLines("puzzle.txt");
	
	preResults(3);
	std::cout << "Part 1: " << part1(lines[0]) << std::endl;
	std::cout << "Part 2: " << part2(lines[0]) << std::endl;
	afterResults();

	return 0;
}
