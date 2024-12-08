/* Advent of Code 2024
 * Day 08
 */

#include "aoc_utility.h"

void findAllFrequencies(std::vector<std::string>& antennas, std::unordered_map<char, std::vector<Coord>>& frequencies)
{
	for (int i = 0; i < antennas.size(); i++)
	{
		char symbol;
		for (int j = 0; j < antennas[0].size(); j++)
		{
			symbol = antennas[i][j];
			if (symbol != '.')
			{
				if (frequencies.find(symbol) == frequencies.end())
				{
					frequencies[symbol] = std::vector<Coord>{ Coord(i, j) };
				}
				else
				{
					frequencies[symbol].push_back(Coord(i, j));
				}
			}

		}
	}
}

bool isAntiNodeValid(Coord antinode, std::vector<int>& sizes)
{
	if (antinode.x < 0 || antinode.y < 0 || antinode.x > sizes[0] - 1 || antinode.y > sizes[1] - 1)
		return false;
	return true;
}

std::vector<Coord> createAntiNode(Coord& one, Coord& two, Coord& zero)
{
	Coord distance = one - two;
	if (distance == zero)
		return std::vector<Coord> {Coord(-1, -1), one};
	Coord antinode = one + distance;
	return std::vector<Coord> {antinode, one};
}

void findAllAntiNodes(std::unordered_map<char, std::vector<Coord>>& frequencies, std::vector<int>& sizeVector, std::set<Coord>& uniqueAntinodes, bool findOne = false)
{
	Coord zero = Coord(0, 0);
	for (auto frequency : frequencies)
	{
		std::set<std::vector<Coord>> possibilities;
		createCombinations(2, frequency.second, possibilities);
		if (possibilities.size() == 1)
			continue;

		for (auto poss : possibilities)
		{
			Coord one = poss[0];
			std::vector<Coord> results;
			results = createAntiNode(poss[0], poss[1], zero);
			one = results[1];
			Coord antinode = results[0];
			uniqueAntinodes.insert(poss[0]);
			while (isAntiNodeValid(antinode, sizeVector) && !findOne) // find all antinodes
			{
				uniqueAntinodes.insert(antinode);
				if (findOne)
					continue;
				results = createAntiNode(antinode, one, zero);
				one = results[1];
				antinode = results[0];
			}
		}
	}
}

int main()
{
	std::vector<std::string> lines = getLines("input.txt");

	int sizex = lines.size();
	int sizey = lines[0].size();
	std::vector<int> sizeVector = { sizex, sizey };
	std::unordered_map<char, std::vector<Coord>> frequencies;
	findAllFrequencies(lines, frequencies);

	std::set<Coord> uniqueAntinodes;
	std::set<Coord> uniqueAntinodes2;
	findAllAntiNodes(frequencies, sizeVector, uniqueAntinodes, true);
	
	findAllAntiNodes(frequencies, sizeVector, uniqueAntinodes2, false);

	preResults(8, 2024);
	std::cout << "Part 1: " << uniqueAntinodes.size() << std::endl;
	std::cout << "Part 2: " << uniqueAntinodes2.size() << std::endl;
	afterResults();

	return 0;
}