/*
 * Advent of Code 2017
 * Day 13
 */

#include "aoc_utility.h"

bool checkLaser(int seconds, std::vector<int>& keys, std::unordered_map<int, std::vector<int>>& firewall)
{
	for (auto key : keys)
	{
		if ((key + seconds) % firewall[key].size() == 0) 
			return false;
	}
	return true;
}

void createFirewall(std::vector<std::vector<std::string>>& scanners, std::unordered_map<int, std::vector<int>>& firewall)
{
	for (auto scanner : scanners)
	{
		int scannerID = std::stoi(scanner[0]);
		std::vector<int>temp;

		for (int i = 0; i < stoi(scanner[1]); i++)
			temp.push_back(i);
		for (int i = stoi(scanner[1]) - 2; i > 0; i--)
			temp.push_back(i);

		firewall[scannerID] = temp;
	}
}

void part1(std::unordered_map<int, std::vector<int>> &firewall, int lastScanner)
{
	int caught = 0;
	for (int i = 0; i < lastScanner + 1; i++)
	{
		if (firewall.find(i) != firewall.end())
		{
			int lookup = i % firewall[i].size();
			if (lookup == 0)
			{
				double level = *std::max_element(firewall[i].begin(), firewall[i].end());
				caught += i * (level + 1);
			}
		}
	}
	std::cout << "Part 1: " << caught << std::endl;
}

void part2(std::unordered_map<int, std::vector<int>> firewall)
{
	std::vector<int> keys;
	for (auto key : firewall)
		keys.push_back(key.first);

	bool waiting = true;
	int seconds = 0;
	while (waiting)
	{
		if (checkLaser(seconds, keys, firewall))
			waiting = false;
		else
			seconds++;
	}
	std::cout << "Part 2: " << seconds << std::endl;
}

int main()
{
	std::vector<std::string> lines = getLines("puzzle.txt");
	std::vector<std::vector<std::string>> scanners = splitToString(lines, ": ");
	std::unordered_map<int, std::vector<int>> firewall;
	
	createFirewall(scanners, firewall);
	int lastScanner = stoi(scanners[scanners.size() - 1][0]);
	
	preResults(13, 2017);
	part1(firewall, lastScanner);
	part2(firewall);
	afterResults();
	return 0;
}