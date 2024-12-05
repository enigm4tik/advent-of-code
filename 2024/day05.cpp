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

void printVector(std::vector<int> myVector)
{
	for (int x : myVector)
		std::cout << x << ", ";
	std::cout << std::endl;
}

void filterRules(std::unordered_map<int, std::vector<int>>& rules, std::vector<int> &filteredRules, std::vector<int> &update, int page)
{
	std::copy_if(rules[page].begin(), rules[page].end(), std::back_inserter(filteredRules), [update](int i) {auto found = std::find(update.begin(), update.end(), i); return found != update.end(); });
}

void fixPages(std::vector<int>& update, std::unordered_map<int, std::vector<int>>& rules, int start = 0)
{
	for (int i = start; i < update.size(); i++)
	{
		int page = update[i];
		std::cout << "Current Page: " << page << std::endl;
		if (rules.find(page) != rules.end()) // there is a rule for this page
		{
			std::cout << "Current Page: " << page << std::endl;
			auto pagePosition = std::find(update.begin(), update.end(), page);
			std::vector<int> filteredRules;;
			filterRules(rules, filteredRules, update, page);
			for (int page2 : filteredRules)
			{
				auto currentPos = std::find(update.begin(), update.end(), page2);
				if (currentPos != update.end() && currentPos < pagePosition)
				{
					std::iter_swap(pagePosition, currentPos);
					fixPages(update, rules, start);
				}
			}
		}
	}
}

void sort(std::vector<int> update, std::unordered_map<int, std::vector<int>> rules)
{
	/*const std::vector<int> v1{ 1, 2, 5, 5, 5, 9 };
	const std::vector<int> v2{ 2, 5, 7 };
	std::vector<int> diff;

	std::set_difference(v1.begin(), v1.end(), v2.begin(), v2.end(), std::inserter(diff, diff.begin()));*/

	int pos = 0;
	int size = update.size();
	std::vector<int> rule;
	std::vector<int> pushedToBack;
	for (int i = 0; i < size; i++)
	{
		int page = update[i];
		std::cout << "Current Page: " << page << std::endl;
		if (rules.find(page) == rules.end())
		{ // no page exists
			std::vector<int> slice = std::vector<int>(update.begin() + 1, update.end());
			if (pushedToBack.size() == slice.size());
			break;

			pushedToBack.push_back(page);
			update.push_back(page);
			update.erase(update.begin() + i);
			printVector(update);
			i -= 1;
			continue;
		}
		rule = rules[page];
		//std::cout << "Page: " << page << std::endl;
		for (int j = pos + 1; j < size - i; j++)
		{
			if (i + j >= size)
				break;
			int nextPage = update[i + j];
			std::cout << "Next page: " << nextPage << std::endl;
			if (std::find(rule.begin(), rule.end(), nextPage) == rule.end())
			{
				//std::cout << page << " Before: \n";
					//printVector(update);
				update.insert(update.begin(), nextPage);
				//printVector(update);
				update.erase(update.begin() + j + 1);
				//std::cout << "After: \n";
				printVector(update);
				//std::cout << "_____ \n";
				i -= 1;
				break;
			}
			else
				std::cout << "found" << std::endl;
		}
	}
	printVector(update);
}


bool dfs(std::vector<int> &update, std::unordered_map<int, std::vector<int>> &rules, int node, int& result, std::vector<int> visited = {})
{
	if (result != 0)
	{
		return true;
	}
	if (std::find(update.begin(), update.end(), node) != update.end())
	{
		visited.push_back(node);
	}
	
	std::vector<int> adjacencyList = rules[node];

	for (int rule: adjacencyList)
	{
		if (std::find(update.begin(), update.end(), rule) != update.end())
		{
			if (std::find(visited.begin(), visited.end(), rule) == visited.end())
			{
				if (dfs(update, rules, rule, result, visited))
					return true;
			}
		}
	}
	if (visited.size() == update.size())
	{
		result = getMiddleValue(visited);
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
	int i = 0;
	for (auto update : manualUpdates)
	{
		std::cout << i++ << std::endl;
		if (checkPageOrder(update, rules))
			middlePageSum += getMiddleValue(update);
		else
		{
			//printVector(update);
			int result = 0;
			for (auto page : update)
			{
				dfs(update, rules, page, result);
			}
			middleFixedSum += result;
		}
	}
	std::cout << "Part 1: " << middlePageSum << std::endl;
	std::cout << "Part 2: " << middleFixedSum << std::endl;

	return 0;
}