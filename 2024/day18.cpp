/*
 * Advent of Code - 2024
 * Day 18
 */

#include "aoc_utility.h"

void printMaze(std::vector<Coord> &slice, std::vector<int> &sizes)
{
	Coord fallingByte;
	for (int i = 0; i < sizes[0]; i++)
	{
		for (int j = 0; j < sizes[1]; j++)
		{
			fallingByte = Coord(i, j);
			if (std::find(slice.begin(), slice.end(), fallingByte) != slice.end())
			{
				std::cout << "#";
			}
			else
				std::cout << ".";
		}
		std::cout << "\n";
	}
}

std::unordered_map<Coord, int> getPositions(std::vector<Coord>& slice, std::vector<int>& sizes, int bigNumber)
{
	Coord fallingByte;
	std::unordered_map<Coord, int> unvisitedNodes;
	for (int i = 0; i < sizes[0]; i++)
	{
		for (int j = 0; j < sizes[1]; j++)
		{
			fallingByte = Coord(i, j);
			if (std::find(slice.begin(), slice.end(), fallingByte) == slice.end())
				unvisitedNodes[fallingByte] = bigNumber;
		}
	}
	return unvisitedNodes;
}

Coord getSmallest(std::unordered_map<Coord, int>& unvisited)
{
	if (unvisited.size() == 1)
		for (auto node : unvisited)
			return node.first;
		
	int smallestSteps = 10000;
	std::vector<Coord> smallestNodes;
	for (auto node : unvisited)
	{
		if (node.second < smallestSteps)
		{
			smallestSteps = node.second;
			smallestNodes.push_back(node.first);
		}
	}

	std::sort(smallestNodes.begin(), smallestNodes.end());
	if (smallestNodes.size())
	{
		for (int i = 0; i < smallestNodes.size(); i++)
		{
			if (unvisited[smallestNodes[i]] == smallestSteps)
				return smallestNodes[i];
		}
	}
	else 
	{
		for (auto node : unvisited)
			return node.first;
	}
	
}

void dijkstra(std::unordered_map<Coord, int> &allNodes, std::vector<int> &sizes, Coord &start)
{
	allNodes[start] = 0;
	std::unordered_map<Coord, int> unvisited = allNodes;
	Coord up;
	Coord down;
	Coord right;
	Coord left;
	Coord current;
	while (unvisited.size())
	{
		current = getSmallest(unvisited);
		up = current + Coord(-1, 0);
		down = current + Coord(1, 0);
		right = current + Coord(0, 1);
		left = current + Coord(0, -1);
		std::vector<Coord> neighbors = { up, down, right, left };
		for (Coord neighbor : neighbors)
		{
			if (neighbor.x < 0 || neighbor.y < 0 || neighbor.x >= sizes[0] || neighbor.y >= sizes[1])
			{
				continue;
			}
			
			if (allNodes.find(neighbor) == allNodes.end())
			{
				continue;
			}

			int newScore = allNodes[current] + 1;
			if (newScore < allNodes[neighbor])
			{
				unvisited[neighbor] = newScore;
				allNodes[neighbor] = newScore;
			}
				
		}
		unvisited.erase(current);
	}
}

int part1(std::vector<Coord> &bytes, int amount, std::vector<int> &sizes, Coord &start, Coord &end, int bigNumber, bool drawMaze = false)
{
	std::vector<Coord> slice;
	slice.insert(slice.begin(), bytes.begin(), bytes.begin() + amount +1);
	//std::cout << "SLICES: " << slice.size() << std::endl;
	if (drawMaze)
		printMaze(slice, sizes);
	std::unordered_map<Coord, int> unvisitedNodes = getPositions(slice, sizes, bigNumber);
	dijkstra(unvisitedNodes, sizes, start);
	return unvisitedNodes[end];
}

int main()
{
	std::vector<int> sizes = { 71, 71 };
	std::vector<std::string> lines = getLines("input.txt");
	std::vector<std::vector<int>> coordinates = splitToInt(lines, ',');

	std::vector<Coord> bytes;
	for (std::vector<int> coordinate : coordinates)
	{
		bytes.push_back(Coord(coordinate[1], coordinate[0]));
	}

	Coord start = Coord(0, 0);
	Coord end = Coord(sizes[0] - 1, sizes[1] - 1);
	int amount = 1024;
	int bigNumber = 10000000;

	// Part 1
	int part1Steps = part1(bytes, amount, sizes, start, end, bigNumber);

	// Part 2
	int steps = 0;
	while (steps != bigNumber)
	{
		amount++;
		steps = part1(bytes, amount, sizes, start, end, bigNumber);
	}

	part1(bytes, amount, sizes, start, end, bigNumber, true); // maze that does not work anymore

	preResults(20, 2024);
	std::cout << "Part 1: " << part1Steps << "\n";
	std::cout << "Part 2: " << bytes[amount].y << "," << bytes[amount].x << "\n";
	afterResults();

	return 0;
}