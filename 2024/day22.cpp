/*
 * Advent of Code - 2024
 * Day 20
 */

#include "aoc_utility.h"

void mix(long long &number, long long &value)
{
	number ^= value;
}

void prune(long long &value)
{
	value = value % 16777216;
}

long long getNextNumber(long long number)
{
	long long value = number << 6;
	mix(number, value);
	prune(number);
	value = number >> 5;
	mix(number, value);
	prune(number);
	value = number << 11;
	mix(number, value);
	prune(number);
	return number;
}

int getlastInteger(int number)
{
	std::string temp;
	temp = std::to_string(number);
	temp = *temp.rbegin();
	return stoi(temp);
}

void getBananaCount(std::unordered_map<int, std::vector<int>> &differences, std::unordered_map<int, std::vector<int>> &bananas, std::map<std::vector<int>, int> &bananaMap)
{
	std::vector<int> frame;
	for (auto buyer : differences)
	{
		std::map<std::vector<int>, bool> seen; // switched this from vector to map to optimize for speed
		for (int i = 0; i < buyer.second.size() - 4; i++)
		{
			frame = { buyer.second[i], buyer.second[i + 1], buyer.second[i + 2], buyer.second[i + 3] };
			if (seen.find(frame) == seen.end())
			{
				if (bananaMap.find(frame) == bananaMap.end())
					bananaMap[frame] = bananas[buyer.first][i + 4];
				else
					bananaMap[frame] += bananas[buyer.first][i + 4];
				seen[frame] = true;
			}
		
			
		}
	}
}

void part1(std::vector<std::string>& input, long long &result, std::unordered_map<int, std::vector<int>> &bid, std::unordered_map<int, std::vector<int>> &differences)
{
	long long startingNumber;
	int tempI;
	int i = 0;
	for (std::string line : input)
	{
		startingNumber = stoll(line);
		std::vector<int> temp;
		temp.push_back(getlastInteger(startingNumber));
		std::vector<int> diffTemp;
		for (int i = 0; i < 2000; i++)
		{
			startingNumber = getNextNumber(startingNumber);
			tempI = getlastInteger(startingNumber);
			temp.push_back(tempI);
			diffTemp.push_back(tempI - temp[i]);

		}
		result += startingNumber;
		bid[i] = temp;
		differences[i] = diffTemp;
		i++;
	}
}

int main()
{
	std::vector<std::string> input = getLines("input.txt");

	long long result = 0;
	std::unordered_map<int, std::vector<int>> bid;
	std::unordered_map<int, std::vector<int>> differences;
	part1(input, result, bid, differences);

	// Part 2
	
	std::map<std::vector<int>, int> bananaMap;
	std::vector<int> frame;

	getBananaCount(differences, bid, bananaMap);

	int bananas = 0;
	for (auto sequence : bananaMap)
	{
		if (sequence.second > bananas)
		{
			bananas = sequence.second;
		}
	}
	
	preResults(22, 2024);
	std::cout << "Part 1: " << result << "\n";
	std::cout << "Part 2: " << bananas << "\n";
	afterResults();

}