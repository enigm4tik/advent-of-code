/*
 * Advent of Code - 2024
 * Day 19
 */

#include "aoc_utility.h"

bool isItPossible(std::pair<std::string, std::vector<std::string>> &colorCombo)
{
	std::string color = colorCombo.first;
	std::vector<std::string> blocks = colorCombo.second;
	std::set<size_t> allpos;
	for (std::string &block: blocks)
	{
		std::vector<size_t> positions;

		size_t pos = color.find(block, 0);
		while (pos != std::string::npos)
		{
			positions.push_back(pos);
			pos = color.find(block, pos + 1);
		}
		for (size_t pos: positions)
			for (int i = 0; i < block.length(); i++)
			{
				allpos.insert(pos + i);
			}
		if (allpos.size() == color.size())
			return true;
	}
	return false;	
}

void bfs(std::unordered_map<int, std::vector<std::vector<int>>> positions, int length, int &validPaths, std::vector<int> currentV = {})
{
	// Entirely unused, might be useful at some point :shrug:
	if (currentV.size() > 0 && currentV.back() == length - 1)
	{
		validPaths++;
			
		return;
	}

	if (currentV.size() == 0)
	{
		for (std::vector<int> pos : positions[0])
		{
			bfs(positions, length, validPaths, pos);
		}
	}
	else 
	{		
		int current = currentV.back();
		int next = current + 1;
		for (std::vector<int> pos : positions[next])
		{
			bfs(positions, length, validPaths, pos);
		}
	}
	
	return;
}

long long lookUp(std::string & color, std::string &rest, std::unordered_map<std::string, long long>& lookupMap, std::vector<std::string>& availableColors)
{
	if (rest.size() == 0)
	{
		if (lookupMap.find(color) != lookupMap.end())
			return lookupMap[color];
		else
		{
			if (std::find(availableColors.begin(), availableColors.end(), color) != availableColors.end())
			{
				lookupMap[color] = 1;
				return 1;
			}
			else
			{
				lookupMap[color] = 0;
				return 0;
			}
		}
	}
	else
	{
		if (std::find(availableColors.begin(), availableColors.end(), color) == availableColors.end())
			return 0;
		if (std::find(availableColors.begin(), availableColors.end(), rest) != availableColors.end())
			return lookupMap[rest];
		else
			if (lookupMap.find(rest) != lookupMap.end())
				return lookupMap[rest];
			else
				return 0;
	}
}

long long getPossibilites(std::unordered_map<std::string, long long> &lookupMap, std::vector<std::string> &availableColors, std::string &color)
{
	int i = 0;
	while (i < color.length())
	{
		std::string x = color.substr(color.size() - i - 1);
		std::string xx = color.substr(color.size() - i);
		int j = 0;
		long long calc = 0;
		if (lookupMap.find(x) == lookupMap.end())
		{
			while (j < x.length())
			{
				std::string y = x.substr(0, j + 1);
				std::string yy = x.substr(j + 1);
				j++;
				calc += lookUp(y, yy, lookupMap, availableColors);
			}
			lookupMap[x] = calc;
		}
		i++;
	}
	return lookupMap[color];
}

int main()
{
	std::vector<std::string> availableColors = getLines("rules.txt");
	std::vector<std::string> colorCombinations = getLines("input.txt");
	availableColors = splitLineToString(availableColors[0], ", ");

	std::unordered_map<std::string, std::vector<std::string>> possibilities;
	for (std::string color : colorCombinations)
	{
		std::vector<std::string> bla;
		for (std::string towel : availableColors)
		{
			if (color.find(towel) != std::string::npos)
				bla.push_back(towel);
		}
		possibilities[color] = bla;
	}

	int possibleCombinations = 0;
	std::vector<std::string> possibles;

	for (std::pair<std::string, std::vector<std::string>> possibility : possibilities)
	{
		possibleCombinations += isItPossible(possibility);
		if (isItPossible(possibility))
		{
			possibles.push_back(possibility.first);
		}
	}

	// Part 2
	std::unordered_map<std::string, long long> lookupMap;
	
	long long res = 0;
	for (auto color : possibles)
	{
		res += getPossibilites(lookupMap, availableColors, color);
	}
	
	preResults(20, 2024);
	std::cout << possibleCombinations << "\n";
	std::cout << res << "\n";
	afterResults();

	return 0;
}