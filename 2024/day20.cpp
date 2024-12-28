/*
 * Advent of Code - 2024
 * Day 20
 */

#include "aoc_utility.h"

void getOptimalPath(std::vector<Coord> &walls, std::vector<Coord> paths, std::vector<Coord> &optimalPath, Coord start, Coord exit)
{
	optimalPath.push_back(start);
	Coord current = start;
	Coord up, left, down, right;
	std::vector<Coord> neighbors;
	while (!(current == exit))
	{
		up = current + Coord(-1, 0);
		left = current + Coord(0, -1);
		down = current + Coord(1, 0);
		right = current + Coord(0, 1);
		neighbors = { up, left, down, right };
		for (const Coord& neighbor : neighbors)
		{
			auto found = std::find(paths.begin(), paths.end(), neighbor);
			if (found != paths.end() && std::find(optimalPath.begin(), optimalPath.end(), neighbor) == optimalPath.end())
			{
				optimalPath.push_back(neighbor);
				current = neighbor;
				paths.erase(found);
				break;
			}
		}		
	}
}

void parseMaze(std::vector<std::string> &lines, std::vector<Coord> &walls, std::vector<Coord> &paths, Coord &start, Coord &exit)
{
	Coord temp;
	for (int i = 0; i < lines.size(); i++)
	{
		for (int j = 0; j < lines[0].size(); j++)
		{
			temp = Coord(i, j);
			if (lines[i][j] == '#')
			{
				walls.push_back(temp);
				continue;
			}
			if (lines[i][j] == 'E')
				exit = temp;
			if (lines[i][j] == 'S')
				start = temp;
			paths.push_back(temp);
		}
	}
}

void part1(std::vector<Coord> &optimalPath, std::vector<Coord> &walls, std::vector<Coord> &nextDirections, std::map<int, std::vector<std::pair<Coord, Coord>>> &cheats)
{
	Coord step;
	Coord next;
	Coord overnext;
	int saved = 0;
	for (int i = 0; i < optimalPath.size(); i++)
	{
		step = optimalPath[i];
		for (Coord dir : nextDirections)
		{
			next = step + dir;
			if (std::find(walls.begin(), walls.end(), next) != walls.end())
			{
				overnext = next + dir;
				if (overnext.x > 0 && overnext.y > 0 && overnext.x < optimalPath.size() && overnext.y < optimalPath.size())
				{
					auto found = std::find(optimalPath.begin() + i, optimalPath.end(), overnext);
					if (found != optimalPath.end())
					{
						saved = found - optimalPath.begin() - i - 2;
						if (cheats.find(saved) == cheats.end())
							cheats[saved] = { std::make_pair(next, overnext) };
						else
							cheats[saved].push_back(std::make_pair(next, overnext));
					}
				}
			}
		}
	}
}

void part2(std::vector<Coord>& optimalPath, std::vector<Coord>& walls, std::vector<Coord>& nextDirections, std::map<int, std::vector<std::pair<Coord, Coord>>>& cheats)
{
	Coord step;
	Coord next;
	int savedDistance;
	for (int i = 0; i < optimalPath.size(); i++)
	{
		step = optimalPath[i];
		for (Coord dir : nextDirections)
		{
			next = step + dir;
			if (std::find(walls.begin(), walls.end(), next) != walls.end())
			{
				for (int j = i; j < optimalPath.size(); j++)
				{
					int distance = getDistance(step, optimalPath[j]);
					if (distance <= 20 && distance > 0)
					{
						savedDistance = j - i - distance;
						if (distance < j - i && savedDistance >= 100)
						{
							if (cheats.find(savedDistance) == cheats.end())
								cheats[savedDistance] = { std::make_pair(step, optimalPath[j]) };
							else
								if (std::find(cheats[savedDistance].begin(), cheats[savedDistance].end(), std::make_pair(step, optimalPath[j])) == cheats[savedDistance].end())
									cheats[savedDistance].push_back(std::make_pair(step, optimalPath[j]));
						}
					}
				}
			}
		}
	}
}

int main()
{
	std::vector<std::string> lines = getLines("input.txt");
	std::vector<Coord> walls;
	std::vector<Coord> paths;
	Coord start;
	Coord exit;
	
	parseMaze(lines, walls, paths, start, exit);

	std::vector<Coord> optimalPath;
	
	getOptimalPath(walls, paths, optimalPath, start, exit);

	std::vector<Coord> nextDirections = { Coord(-1, 0), Coord(1, 0), Coord(0, -1), Coord(0, 1) };

	std::map<int, std::vector<std::pair<Coord, Coord>>> cheats;

	part1(optimalPath, walls, nextDirections, cheats);

	int foundCheats = 0;
	for (auto cheat : cheats)
		if (cheat.first >= 100)
			foundCheats += cheat.second.size();

	std::map<int, std::vector<std::pair<Coord, Coord>>> cheatsPart2;

	part2(optimalPath, walls, nextDirections, cheatsPart2);

	int foundLongerCheats = 0;
	for (auto x : cheatsPart2)
		foundLongerCheats += x.second.size();

	preResults(20, 2024);
	std::cout << "Part 1: " << foundCheats << "\n";
	std::cout << "Part 2: " << foundLongerCheats << "\n";
	afterResults();
		
	return 0;
}