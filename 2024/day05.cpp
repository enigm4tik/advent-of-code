/* Advent of Code 
 * Day 5
 */

#include "aoc_utility.h"

int getMiddleValue(std::vector<int> &updateList)
{
	int size = updateList.size();
	if (size % 2 == 0)
		return updateList[size/2];
	return updateList[(size-1)/2];
}

int checkPageOrder(std::vector<int> &update, std::unordered_map<int, std::vector<int>> &rules)
{
	bool okay = true;
	for (auto rule : rules)
	{
		int firstPage = rule.first;
		auto foundFirst = std::find(update.begin(), update.end(), firstPage);
		if (foundFirst != update.end()) //if first number is found
		{
			for (auto page : rule.second) // check if second number is found
			{
				if (okay)
				{
					auto foundSecond = std::find(update.begin(), update.end(), page);
					if (foundSecond != update.end())
					{
						if (foundFirst > foundSecond)
						{
							okay = false;
						}
					}
				}
			}
		}
	}
	if (okay)
		return 1;
	return 0;
}

void createRuleSet(std::vector<std::string> &ruleStrings, std::unordered_map<int, std::vector<int>> &rules)
{
	std::vector<int> temp;
	for (std::string rule : ruleStrings)
	{
		temp = splitLineToInt(rule, '|');
		auto found = rules.find(temp[0]);
		if (found == rules.end())
			rules[temp[0]] = std::vector<int>{ temp[1] };	
		else
			rules[temp[0]].push_back(temp[1]);
	}
}

void createManualUpdates(std::vector<std::string> &pageStrings, std::vector<std::vector<int>> &manualUpdates)
{
	for (auto page : pageStrings)
		manualUpdates.push_back(splitLineToInt(page, ','));
}

void filterRules(std::unordered_map<int, std::vector<int>>& rules, std::vector<int> &filteredRules, std::vector<int> &update, int page)
{
	std::copy_if(rules[page].begin(), rules[page].end(), std::back_inserter(filteredRules), [update](int i) {auto found = std::find(update.begin(), update.end(), i); return found != update.end(); });
}

bool dfs(std::vector<int> &update, std::unordered_map<int, std::vector<int>> &rules, int node, int& result, std::vector<int> visited = {})
{
	visited.push_back(node);
	
	std::vector<int>adjacencyList;
	filterRules(rules, adjacencyList, update, node);

	for (int rule: adjacencyList)
	{
		if (std::find(visited.begin(), visited.end(), rule) == visited.end())
		{
			if (dfs(update, rules, rule, result, visited))
				return true;
		}
	}
	if (visited.size() == update.size())
	{
		result = getMiddleValue(visited);
		return true;
	}
	return false;
}

int main()
{
	std::vector<std::string> ruleStrings = getLines("rules.txt");
	std::vector<std::string> pageStrings = getLines("pages.txt");

	std::unordered_map<int, std::vector<int>> rules;
	std::vector<std::vector<int>> manualUpdates;

	createRuleSet(ruleStrings, rules);
	createManualUpdates(pageStrings, manualUpdates);

	int middlePageSum = 0;
	int middleFixedSum = 0;
	for (auto update : manualUpdates)
	{
		if (checkPageOrder(update, rules))
			middlePageSum += getMiddleValue(update);
		else
		{
			int result = 0;
			for (auto page : update)
			{
				if (result == 0)
					dfs(update, rules, page, result);	
			}
			middleFixedSum += result;
		}
	}

	preResults(5, 2024);
	std::cout << "Part 1: " << middlePageSum << std::endl;
	std::cout << "Part 2: " << middleFixedSum << std::endl;
	afterResults();

	return 0;
}