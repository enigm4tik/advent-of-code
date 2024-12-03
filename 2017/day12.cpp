/*
 * Advent of Code 2017
 * Day 12
 */

#include "aoc_utility.h"

std::vector<int> findGroupFromNode(std::unordered_map<int, std::vector<int>>& graph, int node)
{
	std::deque<int> queue = { node };
	std::vector<int> seen;

	while (queue.size())
	{
		std::vector<int> current = graph[queue[0]];
		for (int pipe : current)
		{
			if (std::find(seen.begin(), seen.end(), pipe) == seen.end())
			{
				seen.push_back(pipe);
				queue.push_back(pipe);
			}
		}
		queue.pop_front();
	}

	return seen;
}

int findAllGroupsInGraph(std::unordered_map<int, std::vector<int>> & graph)
{
	std::deque<int> queue;
	for (auto val : graph)
	{
		queue.push_back(val.first);
	}
	int seen_groups = 0;
	while (queue.size())
	{
		int current = queue[0];
		std::vector<int> seen = findGroupFromNode(graph, current);
		for (int pipe : seen)
		{
			queue.erase(std::find(queue.begin(), queue.end(), pipe));
		}
		seen_groups++;
	}
	return seen_groups;
}


int main()
{
	std::vector<std::string> lines = getLines("puzzle.txt");
	std::vector<std::vector<std::string>> programs = splitToString(lines, " <-> ");
	
	std::unordered_map<int, std::vector<int>> graph;

	for (auto program: programs)
	{
		int program_name = std::stoi(program[0]);
		std::vector<int> connections = splitLineToInt(program[1], ', ');
		graph[program_name] = connections;
	}

	std::vector<int> part1 = findGroupFromNode(graph, 0);
	preResults(12, 2017);
	std::cout << "Part 1: " << part1.size() << std::endl;
	std::cout << "Part 2: " << findAllGroupsInGraph(graph) << std::endl;
	afterResults();

	return 0;
}

