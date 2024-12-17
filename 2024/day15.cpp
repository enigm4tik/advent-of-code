/*
 * Advent of Code - 2024
 * Day 15
 */

#include "aoc_utility.h"

using CoordPair = std::pair<Coord, Coord>;

// globals
std::unordered_map<char, Coord> robotDirections =
{
	{'<', Coord(0, -1)},
	{'>', Coord(0, 1)},
	{'^', Coord(-1, 0)},
	{'v', Coord(1, 0)}
};

// declarations
std::vector<Coord> getEntityFromMaze(std::vector<std::string>& maze, char entity);
void attemptMovement(std::vector<Coord>& boxes, std::vector<Coord>& walls, Coord& robot, char direction);

std::vector<CoordPair> getEntityFromMaze(std::vector<std::string>& maze, std::string& entity);
void attemptMovement(std::vector<CoordPair>& boxes, std::vector<Coord>& walls, Coord& robot, char direction);
void printMap(std::vector <CoordPair>& boxes, std::vector<Coord>& walls, Coord& robot, std::vector<int> sizes);

int main()
{
	// split in two files
	std::vector<std::string> movementInstructions = getLines("rules.txt");
	std::vector<std::string> maze = getLines("input.txt");

	std::vector<Coord> walls = getEntityFromMaze(maze, '#');
	std::vector<Coord> boxes = getEntityFromMaze(maze, 'O');
	std::string boxString = "[]";
	std::vector < CoordPair> boxes2 = getEntityFromMaze(maze, boxString);
	Coord robot = getEntityFromMaze(maze, '@')[0];

	std::vector<int> sizes = { int(maze.size()), int(maze[0].size()) };
	printMap(boxes2, walls, robot, sizes);
	for (int i = 0; i < movementInstructions.size(); i++)
	{
		for (int j = 0; j < movementInstructions[0].size(); j++)
		{
			attemptMovement(boxes2, walls, robot, movementInstructions[i][j]);
		}
	}
	printMap(boxes2, walls, robot, sizes);

	long gpscoord = 0;
	for (CoordPair box : boxes2)
	{
		gpscoord += box.first.x * 100 + box.first.y;
	}
	std::cout << gpscoord;
    
    // Part 1
	/*for (int i = 0; i < movementInstructions.size(); i++)
		for (int j = 0; j < movementInstructions[0].size(); j++)
		{
			attemptMovement(boxes, walls, robot, movementInstructions[i][j]);
		}

	int gpscoord = 0;
	for (Coord box : boxes)
	{
		gpscoord += box.x * 100 + box.y;
	}
	std::cout << gpscoord;*/

	return 0;
}

void printMap(std::vector <CoordPair>& boxes, std::vector<Coord>& walls, Coord& robot, std::vector<int> sizes)
{
	Coord temp;
	Coord temp2;
	for (int i = 0; i < sizes[0]; i++)
	{
		for (int j = 0; j < sizes[1]; j++)
		{
			temp = Coord(i, j);
			temp2 = Coord(i, j + 1);
			if (std::find(boxes.begin(), boxes.end(), std::make_pair(temp, temp2)) != boxes.end())
			{
				std::cout << "[]";
				j++;
				continue;
			}

			if (std::find(walls.begin(), walls.end(), temp) != walls.end())
			{
				std::cout << "#";
				continue;
			}

			if (temp == robot)
			{
				std::cout << "@";
				continue;
			}
			std::cout << ".";
		}
		std::cout << "\n";
	}
}

std::vector<Coord> getEntityFromMaze(std::vector<std::string>& maze, char entity)
{
	std::vector<Coord> entityVector;
	Coord temp;
	for (int i = 0; i < maze.size(); i++)
	{
		for (int j = 0; j < maze[0].size(); j++)
		{
			temp = Coord(i, j);
			if (maze[i][j] == entity)
			{
				entityVector.push_back(temp);
			}
		}
	}
	return entityVector;
}

std::vector<CoordPair> getEntityFromMaze(std::vector<std::string>& maze, std::string& entity)
{
	std::vector<CoordPair> entityVector;
	Coord temp;
	Coord temp2;
	for (int i = 0; i < maze.size(); i++)
	{
		for (int j = 0; j < maze[0].size(); j++)
		{
			temp = Coord(i, j);
			temp2 = Coord(i, j + 1);
			std::string box = "";
			box += maze[i][j];
			box += maze[i][j + 1];
			if (box == entity)
			{
				entityVector.push_back(std::make_pair(temp, temp2));
			}
		}
	}
	return entityVector;
}

std::vector<std::vector<Coord>> getGroupsInColumn(std::vector<Coord>& boxes, int columnIndex)
{
	Coord temp;
	std::vector<std::vector<Coord>> verticals;
	std::vector<Coord> tempVec;
	std::sort(boxes.begin(), boxes.end());
	for (Coord box : boxes)
	{
		if (tempVec.size() > 0)
		{
			if (box.x - tempVec[tempVec.size() - 1].x > 1)
			{
				verticals.push_back(tempVec);
				tempVec = {};
			}
		}

		if (box.y == columnIndex)
		{
			tempVec.push_back(box);
		}
	}
	verticals.push_back(tempVec);
	return verticals;
}

std::vector<CoordPair> getDownAll(std::vector<CoordPair>& boxes, CoordPair pair, char direction)
{
	std::vector<CoordPair> toCheck = { pair };
	std::vector<CoordPair> verticals;
	while (toCheck.size())
	{
		CoordPair current = toCheck.back();
		toCheck.pop_back();
		for (CoordPair box : boxes)
		{
			int xDistance = box.first.x - current.first.x;
			if (xDistance < 0)
				continue;
			if ((box.first.y == current.first.y && box.first.x - current.first.x <= 1)
				|| (box.first.y == current.second.y && box.first.x - current.first.x <= 1)
				|| (box.second.y == current.first.y && box.first.x - current.first.x <= 1))
			{
				if (std::find(verticals.begin(), verticals.end(), box) == verticals.end())
				{
					verticals.push_back(box);
					toCheck.push_back(box);
				}
			}
		}
	}
	std::sort(verticals.begin(), verticals.end());
	return verticals;
}

std::vector<CoordPair> getLeftAll(std::vector<CoordPair>& boxes, CoordPair pair, char direction)
{
	std::vector<CoordPair> toCheck = { pair };
	std::vector<CoordPair> horizontals;
	while (toCheck.size())
	{
		CoordPair current = toCheck.back();
		toCheck.pop_back();
		for (CoordPair box : boxes)
		{
			if (current.first.y - box.second.y < 0)
				continue;
			if (box.second.x == current.first.x && current.first.y - box.second.y <= 1)
			{
				if (std::find(horizontals.begin(), horizontals.end(), box) == horizontals.end())
				{
					horizontals.push_back(box);
					toCheck.push_back(box);
				}
			}
		}
	}
	horizontals.push_back(pair);
	std::sort(horizontals.begin(), horizontals.end());
	return horizontals;
}

std::vector<CoordPair> getRightAll(std::vector<CoordPair>& boxes, CoordPair pair, char direction)
{
	std::vector<CoordPair> toCheck = { pair };
	std::vector<CoordPair> horizontals;
	while (toCheck.size())
	{
		CoordPair current = toCheck.back();
		toCheck.pop_back();
		for (CoordPair box : boxes)
		{
			if (box.first.y - current.second.y < 0)
				continue;
			if (box.second.x == current.first.x && box.first.y - current.second.y <= 1)
			{
				if (std::find(horizontals.begin(), horizontals.end(), box) == horizontals.end())
				{
					horizontals.push_back(box);
					toCheck.push_back(box);
				}
			}
		}
	}
	horizontals.push_back(pair);
	std::sort(horizontals.begin(), horizontals.end());

	/*for (auto hh : horizontals)
	{
		hh.first.printCoord();
		hh.second.printCoord();
	}
	std::cout << "\n";*/


	return horizontals;
}

std::vector<CoordPair> getUpAll(std::vector<CoordPair>& boxes, CoordPair pair, char direction)
{
	std::vector<CoordPair> toCheck = { pair };
	std::vector<CoordPair> verticals;
	while (toCheck.size())
	{
		CoordPair current = toCheck.back();
		toCheck.pop_back();
		for (CoordPair box : boxes)
		{
			int xDistance = current.first.x - box.first.x;
			if (xDistance < 0)
				continue;
			if ((box.first.y == current.first.y && current.first.x - box.first.x <= 1)
				|| (box.first.y == current.second.y && current.first.x - box.first.x <= 1)
				|| (box.second.y == current.first.y && current.first.x - box.first.x <= 1))
			{
				if (std::find(verticals.begin(), verticals.end(), box) == verticals.end())
				{
					verticals.push_back(box);
					toCheck.push_back(box);
				}
			}
		}
	}
	std::sort(verticals.begin(), verticals.end());
	return verticals;
}

std::vector<std::vector<Coord>> getGroupsInRow(std::vector<Coord>& boxes, int rowIndex)
{
	Coord temp;
	std::vector<std::vector<Coord>> horizontals;
	std::vector<Coord> tempVec;
	std::sort(boxes.begin(), boxes.end());
	for (Coord box : boxes)
	{
		if (tempVec.size() > 0)
		{
			if (box.y - tempVec[tempVec.size() - 1].y > 1)
			{
				horizontals.push_back(tempVec);
				tempVec = {};
			}
		}

		if (box.x == rowIndex)
		{
			tempVec.push_back(box);
		}
	}
	horizontals.push_back(tempVec);
	return horizontals;
}

std::vector<Coord> findRelevantGroup(std::vector<std::vector<Coord>>& groups, Coord& nextPosition)
{
	std::vector<Coord> relevantGroup;
	for (std::vector<Coord> group : groups)
	{
		if (group.size() > 1)
		{
			auto found = std::find(group.begin(), group.end(), nextPosition);
			if (found != group.end())
			{
				relevantGroup = group;
			}
		}
	}
	return relevantGroup;
}

void attemptBoxMovement(std::vector<Coord>& relevantGroup, std::vector<Coord>& boxes, std::vector<Coord>& walls, char direction, Coord& robot)
{
	Coord movement = robotDirections[direction];
	if (relevantGroup.size())
	{
		Coord first = relevantGroup[0];
		Coord last = relevantGroup[relevantGroup.size() - 1];
		if (direction == '>' || direction == 'v')
		{
			Coord moveGroup = last + movement;
			if (std::find(walls.begin(), walls.end(), moveGroup) == walls.end())
			{
				boxes.erase(std::find(boxes.begin(), boxes.end(), first));
				first = last + movement;
				boxes.push_back(first);
				robot = robot + movement;
				return;
			}
			else
				return;
		}
		else
		{
			Coord moveGroup = first + movement;
			if (std::find(walls.begin(), walls.end(), moveGroup) == walls.end())
			{
				boxes.erase(std::find(boxes.begin(), boxes.end(), last));
				last = first + movement;
				boxes.push_back(last);
				robot = robot + movement;
				return;
			}
			else
				return;
		}
	}
	else
	{
		Coord movedBox = robot + movement + movement;
		if (std::find(walls.begin(), walls.end(), movedBox) == walls.end())
		{
			auto boxFound = std::find(boxes.begin(), boxes.end(), robot + movement);
			boxes.erase(boxFound);
			boxes.push_back(movedBox);
			robot = robot + movement;
			return;
		}
		else
			return;
	}
}

void attemptBoxMovement(std::vector<CoordPair>& relevantGroup, std::vector<CoordPair>& boxes, std::vector<Coord>& walls, char direction, CoordPair& box, Coord& robot)
{
	Coord movement = robotDirections[direction];
	std::sort(boxes.begin(), boxes.end());
	if (relevantGroup.size())
	{
		if (direction == '<')
		{
			Coord nextMove = relevantGroup[0].first + movement;
			if (std::find(walls.begin(), walls.end(), nextMove) == walls.end())
			{
				for (int i = 0; i < relevantGroup.size(); i++)
				{
					boxes.erase(std::find(boxes.begin(), boxes.end(), relevantGroup[i]));
					relevantGroup[i].first = relevantGroup[i].first + movement;
					relevantGroup[i].second = relevantGroup[i].second + movement;
					boxes.push_back(relevantGroup[i]);
				}
				robot = robot + movement;
				return;
			}
			return;
		}
		else if (direction == '>')
		{
			Coord nextMove = relevantGroup[relevantGroup.size() - 1].second + movement;
			if (std::find(walls.begin(), walls.end(), nextMove) == walls.end())
			{
				for (int i = 0; i < relevantGroup.size(); i++)
				{
					boxes.erase(std::find(boxes.begin(), boxes.end(), relevantGroup[i]));
					relevantGroup[i].first = relevantGroup[i].first + movement;
					relevantGroup[i].second = relevantGroup[i].second + movement;
					boxes.push_back(relevantGroup[i]);
				}
				robot = robot + movement;
				return;
			}
			return;
		}
		else if (direction == '^')
		{
			int rowCheck = relevantGroup[0].first.x;
			bool canMove = true;
			for (CoordPair pair : relevantGroup)
			{
				CoordPair nextPair = std::make_pair(pair.first + movement, pair.second + movement);
				auto foundFirst = std::find(walls.begin(), walls.end(), nextPair.first);
				auto foundSecond = std::find(walls.begin(), walls.end(), nextPair.second);
				if (foundFirst != walls.end() || foundSecond != walls.end())
				{
					canMove = false;
				}
			}
			if (canMove)
			{
				for (int i = 0; i < relevantGroup.size(); i++)
				{
					boxes.erase(std::find(boxes.begin(), boxes.end(), relevantGroup[i]));
					relevantGroup[i].first = relevantGroup[i].first + movement;
					relevantGroup[i].second = relevantGroup[i].second + movement;
					boxes.push_back(relevantGroup[i]);
				}
				robot = robot + movement;
				return;
			}
			return;
		}
		else
		{
			int rowCheck = relevantGroup[relevantGroup.size() - 1].first.x;
			bool canMove = true;
			for (CoordPair pair : relevantGroup)
			{
				CoordPair nextPair = std::make_pair(pair.first + movement, pair.second + movement);
				auto foundFirst = std::find(walls.begin(), walls.end(), nextPair.first);
				auto foundSecond = std::find(walls.begin(), walls.end(), nextPair.second);
				if (foundFirst != walls.end() || foundSecond != walls.end())
				{
					canMove = false;
				}
			}
			if (canMove)
			{
				for (int i = 0; i < relevantGroup.size(); i++)
				{
					boxes.erase(std::find(boxes.begin(), boxes.end(), relevantGroup[i]));
					relevantGroup[i].first = relevantGroup[i].first + movement;
					relevantGroup[i].second = relevantGroup[i].second + movement;
					boxes.push_back(relevantGroup[i]);
				}
				robot = robot + movement;
				return;
			}
			return;
		}
	}
	else
	{
		CoordPair nextMove = std::make_pair(box.first + movement, box.second + movement);
		auto foundFirst = std::find(walls.begin(), walls.end(), nextMove.first);
		auto foundSecond = std::find(walls.begin(), walls.end(), nextMove.second);
		if (direction == '^' || direction == 'v')
		{
			if (foundFirst == walls.end() && foundSecond == walls.end())
			{
				boxes.erase(std::find(boxes.begin(), boxes.end(), box));
				box = nextMove;
				boxes.push_back(box);
				robot = robot + movement;
				return;
			}
			return;

		}
		else if (direction == '>')
		{
			if (foundSecond == walls.end())
			{
				boxes.erase(std::find(boxes.begin(), boxes.end(), box));
				box = nextMove;
				boxes.push_back(box);
				robot = robot + movement;
				return;
			}
			return;
		}
		else
		{
			if (foundFirst == walls.end())
			{
				boxes.erase(std::find(boxes.begin(), boxes.end(), box));
				box = nextMove;
				boxes.push_back(box);
				robot = robot + movement;
				return;
			}
			return;
		}
	}
}

void attemptMovement(std::vector<Coord>& boxes, std::vector<Coord>& walls, Coord& robot, char direction)
{
	Coord movement = robotDirections[direction];
	Coord nextPosition = robot + movement;
	std::vector<std::vector<Coord>> groups;
	std::vector<Coord> relevantGroup;
	std::sort(boxes.begin(), boxes.end());

	if (std::find(walls.begin(), walls.end(), nextPosition) != walls.end())
	{
		return;
	}
	auto boxFound = std::find(boxes.begin(), boxes.end(), nextPosition);
	if (boxFound != boxes.end())
	{
		if (direction == '>' || direction == '<')
		{
			groups = getGroupsInRow(boxes, nextPosition.x);
			relevantGroup = findRelevantGroup(groups, nextPosition);
			attemptBoxMovement(relevantGroup, boxes, walls, direction, robot);
			return;
		}
		else
		{
			groups = getGroupsInColumn(boxes, nextPosition.y);
			relevantGroup = findRelevantGroup(groups, nextPosition);
			attemptBoxMovement(relevantGroup, boxes, walls, direction, robot);
			return;
		}
	}
	robot = nextPosition;
	return;
}

void attemptMovement(std::vector <CoordPair>& boxes, std::vector<Coord>& walls, Coord& robot, char direction)
{
	Coord movement = robotDirections[direction];
	Coord nextPosition = robot + movement;
	std::vector<std::vector<CoordPair>> groups;
	std::vector<CoordPair> relevantGroup;
	std::sort(boxes.begin(), boxes.end());
	if (std::find(walls.begin(), walls.end(), nextPosition) != walls.end())
	{
		return;
	}

	for (auto box : boxes)
	{
		if (box.first == nextPosition || box.second == nextPosition)
		{
			if (direction == 'v')
				relevantGroup = getDownAll(boxes, box, direction);
			if (direction == '^')
				relevantGroup = getUpAll(boxes, box, direction);
			if (direction == '>')
				relevantGroup = getRightAll(boxes, box, direction);
			if (direction == '<')
				relevantGroup = getLeftAll(boxes, box, direction);
			attemptBoxMovement(relevantGroup, boxes, walls, direction, box, robot);
			return;
		}
	}

	robot = nextPosition;
	return;
}
