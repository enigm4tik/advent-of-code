/*
 * Advent of Code - 2024
 * Day 10
 */

#include "aoc_utility.h"

bool exploreTopographicMap(std::vector<std::vector<int>>& topographicMap, Coord& trailhead, int &found, std::vector<Coord> seen = {})
{
	// Find all unique paths in graph to reach a 9 from a 0 (trailhead).
	if (topographicMap[trailhead.x][trailhead.y] == 9)
	{
		seen.push_back(trailhead);
		found++;
		return true;
	}
	std::queue<Coord> toCheck;
	toCheck.push(trailhead);
	Coord current;
	
	while (toCheck.size() > 0)
	{
		current = toCheck.front();
		toCheck.pop();
		int currentHeight = topographicMap[current.x][current.y];
		Coord rightNeighbor = current + Coord(1, 0);
		Coord leftNeighbor = current + Coord(0, -1);
		Coord downNeighbor = current + Coord(0, 1);
		Coord upNeighbor = current + Coord(-1, 0);
		std::vector<Coord> neighbors = { rightNeighbor, leftNeighbor, downNeighbor, upNeighbor };
		int seenHeight;
		for (Coord neighbor : neighbors)
		{
			if (neighbor.x < topographicMap.size() && neighbor.y < topographicMap[0].size() && neighbor.x >= 0 && neighbor.y >= 0)
			{
				seenHeight = topographicMap[neighbor.x][neighbor.y];
				if ((seenHeight == currentHeight + 1) && std::find(seen.begin(), seen.end(), neighbor) == seen.end())
				{
					exploreTopographicMap(topographicMap, neighbor, found, seen);
				}
			}
		}
		seen.push_back(current);
	}
	return false;
}

void exploreTopographicMap(std::vector<std::vector<int>>& topographicMap, Coord& trailhead, std::unordered_map<Coord, std::set<Coord>> &peaks)
{
	// Find all heights == 9 in graph that can be reached from a 0 (trailhead).
	std::queue<Coord> toCheck;
	toCheck.push(trailhead);
	std::vector<Coord> seen;
	Coord current;
	while (toCheck.size() > 0)
	{
		current = toCheck.front();
		toCheck.pop();
		int currentHeight = topographicMap[current.x][current.y];
		Coord rightNeighbor = current + Coord(1, 0);
		Coord leftNeighbor = current + Coord(0, -1);
		Coord downNeighbor = current + Coord(0, 1);
		Coord upNeighbor = current + Coord(-1, 0);
		std::vector<Coord> neighbors = { rightNeighbor, leftNeighbor, downNeighbor, upNeighbor };
		int seenHeight;
		for (Coord neighbor : neighbors)
		{
			if (neighbor.x < topographicMap.size() && neighbor.y < topographicMap[0].size() && neighbor.x >= 0 && neighbor.y >= 0)
			{
				seenHeight = topographicMap[neighbor.x][neighbor.y];
				if ((seenHeight == currentHeight + 1) && std::find(seen.begin(), seen.end(), neighbor) == seen.end())
				{
					toCheck.push(neighbor);
					if (seenHeight == 9)
					{
						peaks[trailhead].insert(neighbor);
					}
				}
			}
		}
		seen.push_back(current);
	}
}

int main()
{
	std::vector<std::string> lines = getLines("input.txt");
	
	std::vector<std::vector<int>> topographicMap;
	std::vector<int> temp;
	std::vector<Coord> trailheads;
	for (int i = 0; i < lines.size(); i++)
	{
		temp = {};
		for(int j = 0; j < lines[i].size(); j++)
		{
			temp.push_back(charNumberToInt(lines[i][j]));
			if (lines[i][j] == '0')
				trailheads.push_back(Coord(i, j));
		}
		topographicMap.push_back(temp);
	}

	std::unordered_map<Coord, std::set<Coord>> peaks;

	for (auto trailhead : trailheads)
	{
		exploreTopographicMap(topographicMap, trailhead, peaks);
	}

	int sumOfPeaks = 0;
	for (auto peak : peaks)
		sumOfPeaks += peak.second.size();
	preResults(10, 2024);
	std::cout << "Part 1: " << sumOfPeaks << std::endl;

	int sumOfUniquePaths = 0;

	for (auto trailhead : trailheads) {
		int foundPeaks = 0;
		exploreTopographicMap(topographicMap, trailhead, foundPeaks);
		sumOfUniquePaths += foundPeaks;
		foundPeaks = 0;
	}

	std::cout << "Part 2: " << sumOfUniquePaths << std::endl;
	afterResults();

	return 0;
}