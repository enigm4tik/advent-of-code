/* Advent of Code
 * Day 06
 */

#include "aoc_utility.h"

int FoundLoops = 0;

struct labMap
{
	void findObstacleInDirection(Coord& guard, Coord& direction, int dir, std::vector<int>& SIZES)
	{
		Coord temp = guard + direction;
		addToVector(guard, visited);
		addToVector(temp, visited);
		while (std::find(labMap.begin(), labMap.end(), temp) == labMap.end())
		{
				
			addToVector(temp, visited);
			temp = temp + direction;

			if (temp.x < 0 || temp.y < 0 || temp.x > SIZES[0] || temp.y > SIZES[1])
			{
				unsafe = false;
				finishing = false;
				hit.push_back(std::pair<int, Coord>{dir, temp});
				guard = temp;
				return;
			}
		}
		for (auto h : hit)
		{
			if (h.first == dir && h.second == temp)
			{
				finishing = false;
				FoundLoops++;
			}
		}
		
		hit.push_back(std::pair<int, Coord>{dir, temp});
		guard = temp;
		unsafe = true;
	}

	void resetLab()
	{
		labMap = std::vector<Coord>{};
		visited = std::vector<Coord>{};
		hit = std::vector<std::pair<int, Coord>>{ {} };
		unsafe = true;
		finishing = true;
	}

	std::vector<Coord> labMap;
	std::vector<Coord> visited;
	std::vector<std::pair<int, Coord>> hit;
	bool unsafe = true;
	bool finishing = true;
};

std::vector<Coord> DIRECTIONS = {
	Coord(-1, 0), // up
	Coord(0, 1),
	Coord(1, 0),
	Coord(0, -1),
};

void setUpHeist(std::vector<std::string> &patterns, std::vector<Coord> &obstacles, Coord &guard)
{

	for (int i = 0; i < patterns.size(); i++)
	{
		for (int j = 0; j < patterns[0].size(); j++)
		{
			if (patterns[i][j] == '^')
			{
				guard = Coord(i, j);
				continue;
			}
			if (patterns[i][j] != '.')
				obstacles.push_back(Coord(i, j));
		}
	}
}

void checkLaboratory(labMap& laboratory, Coord& guard, int i, std::vector<int>& sizeVector)
{
	Coord badGuy = guard + DIRECTIONS[(i - 1) % 4];
	Coord goodguy = guard + DIRECTIONS[i % 4];
	
	if (std::find(laboratory.labMap.begin(), laboratory.labMap.end(), badGuy) != laboratory.labMap.end())
	{
		if (std::find(laboratory.labMap.begin(), laboratory.labMap.end(), goodguy) != laboratory.labMap.end())
		{
			// the space I need to go to, is bad!! I need to turn around on the spot!
			guard = guard + DIRECTIONS[(i + 2) % 4];
		}
	}
	laboratory.findObstacleInDirection(guard, DIRECTIONS[i % 4], i%4, sizeVector);
	guard = guard + DIRECTIONS[(i + 2) % 4];
}

void part1(labMap &laboratory, Coord &guard, std::vector<int> &sizeVector)
{
	int i = 0;
	while (laboratory.unsafe)
	{
		checkLaboratory(laboratory, guard, i, sizeVector);
		i++;
	}
	preResults(5, 2024);
	std::cout << "Part 1: " << laboratory.visited.size() << std::endl;
}

void part2(labMap& laboratory, Coord& guard, std::vector<int>& sizeVector, std::vector<Coord> &obstacles)
{
	Coord copyGuard = guard;
	std::vector<Coord> allVisited = laboratory.visited;

	int allVisitedSize = allVisited.size();
	laboratory.resetLab();
	int found = 0;
	for (int i = 0; i < allVisitedSize; i++)
	{
		guard = copyGuard;
		laboratory.labMap = obstacles;
		Coord current = allVisited.back();

		laboratory.labMap.push_back(current);
		allVisited.pop_back();

		int j = 0;
		while (laboratory.finishing)
		{
			checkLaboratory(laboratory, guard, j, sizeVector);
			j++;
		}
		laboratory.labMap.pop_back();
		laboratory.resetLab();
	}
}

int main()
{
	std::vector<std::string> patterns = getLines("input.txt");
	int SIZEX = patterns.size() - 1;
	int SIZEY = patterns[0].size() - 1;
	std::vector<int> sizeVector = { SIZEX, SIZEY };

	std::vector<Coord> obstacles;
	Coord guard(0, 0);	
	setUpHeist(patterns, obstacles, guard);
	
	labMap laboratory;
	laboratory.labMap = obstacles;
	
	part1(laboratory, guard, sizeVector);

	setUpHeist(patterns, obstacles, guard);
	
	// part2 uses the information from the first run
	part2(laboratory, guard, sizeVector, obstacles); 

	std::cout << "Part 2: " << FoundLoops << std::endl;
	afterResults();

	return 0;
}