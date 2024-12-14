/*
 * Advent of Code - 2024
 * Day 12
 */

#include "aoc_utility.h"

std::vector<int> SIZES;

std::vector<Coord> getNeighbors(Coord &me)
{
	std::vector<Coord> directions = {
	Coord(-1, 0), // up
	Coord(0, 1),
	Coord(1, 0),
	Coord(0, -1),
	};

	std::vector<Coord> neighbors;
	Coord neighbor;
	
	for (auto direction : directions)
	{
		neighbor = me + direction;
		if (neighbor.x >= 0 && neighbor.x < SIZES[0] && neighbor.y >= 0 && neighbor.y < SIZES[1])
		{
			neighbors.push_back(neighbor);
		}
	}
	return neighbors;
}

std::vector<Coord> getvalidNeighbors(std::vector<Coord>& group, Coord& me)
{
	std::vector<Coord> myNeighbors = getNeighbors(me);
	std::vector<Coord> validNeighbors;
	for (Coord myNeighbor : myNeighbors)
	{
		if (std::find(group.begin(), group.end(), myNeighbor) != group.end())
			validNeighbors.push_back(myNeighbor);
	}
	return validNeighbors;
}

std::vector<std::vector<Coord>> divideInRegions(std::vector<Coord> &plots)
{
	std::vector<Coord> allPlots = plots;
	std::vector<Coord> toCheck;
	std::vector<Coord> neighbors;
	std::vector<std::vector<Coord>> result;
	Coord currentPlot;
	while (allPlots.size() > 0)
	{
		currentPlot = allPlots.front();
		allPlots.erase(allPlots.begin());
		std::vector<Coord> currentGroup = { currentPlot };
		toCheck.push_back(currentPlot);
		
		while (toCheck.size() > 0)
		{
			currentPlot = toCheck.front();
			toCheck.erase(toCheck.begin());
			neighbors = getvalidNeighbors(allPlots, currentPlot);
			for (Coord neighbor : neighbors)
			{
	
				if (std::find(allPlots.begin(), allPlots.end(), neighbor) != allPlots.end())
				{
					allPlots.erase(std::find(allPlots.begin(), allPlots.end(), neighbor));
				}

				if (std::find(currentGroup.begin(), currentGroup.end(), neighbor) == currentGroup.end())
				{
					currentGroup.push_back(neighbor);
					toCheck.push_back(neighbor);
				}
			}
		}
		result.push_back(currentGroup);	
	}
	return result;
}

int calculateArea(std::vector<Coord> &group)
{
	return group.size();
}

int calculatePerimeter(std::vector<Coord> &group)
{
	int perimeterOverall = 0;
	int perimeterPlot;
	for (Coord plot : group)
	{
		perimeterPlot = 4;
		for (Coord neighbor : getvalidNeighbors(group, plot))
		{
			perimeterPlot--;
		}
		perimeterOverall += perimeterPlot;
	}
	return perimeterOverall;
}

int calculatePrize(std::vector<std::vector<Coord>>& crop)
{
	int prize = 0;
	for (std::vector<Coord> group : crop)
	{
		prize += calculateArea(group) * calculatePerimeter(group);
	}
	return prize;
}

int calculateTotalPrize(std::unordered_map<int, std::vector<std::vector<Coord>>>& regions)
{
	int totalPrize = 0;
	for (auto region : regions)
	{
		totalPrize += calculatePrize(region.second);
	}
	return totalPrize;
}

void fillMatrix(std::vector<Coord> &group, std::unordered_map <Coord, std::vector<int>> &mapOfWalls)
{
	long sides = 0;
	Coord leftNeighbor;
	Coord topNeighbor;
	Coord rightNeighbor;
	Coord bottomNeighbor;
	std::vector<Coord> validNeighbors;
	std::vector<Coord> testNeighbors;
	std::vector<int> walls = { 0, 0, 0, 0 };
	for (Coord plot : group)
	{
		leftNeighbor = Coord(plot.x, plot.y - 1);
		rightNeighbor = Coord(plot.x, plot.y + 1);
		topNeighbor = Coord(plot.x - 1, plot.y);
		bottomNeighbor = Coord(plot.x + 1, plot.y);
		testNeighbors = { leftNeighbor, topNeighbor, bottomNeighbor, rightNeighbor };
		validNeighbors = getvalidNeighbors(group, plot);
		if (validNeighbors.size() == 0)
			continue;
		for (int i = 0; i < 4; i++)
		{
			if (std::find(validNeighbors.begin(), validNeighbors.end(), testNeighbors[i]) == validNeighbors.end())
			{
				//didnt find the neighbor in the list!
				walls[i] = 1;
			}
			else
				walls[i] = 0;
		}
		mapOfWalls[plot] = walls;
	}

}

void getDimensions(std::vector<Coord>& group, std::vector<int> &dimensions)
{
	int &smallestX = dimensions[0];
	int &biggestX = dimensions[1];
	int &smallestY = dimensions[2];
	int &biggestY = dimensions[3];

	for (auto plot : group)
	{
		if (plot.x < smallestX)
			smallestX = plot.x;
		if (plot.x > biggestX)
			biggestX = plot.x;
		if (plot.y < smallestY)
			smallestY = plot.y;
		if (plot.y > biggestY)
			biggestY = plot.y;
	}
	biggestX++;
	biggestY++;
}

long long getSidesForGroup(std::vector<Coord>& group)
{
	if (group.size() == 1 || group.size() == 2)
		return 4;

	std::unordered_map <Coord, std::vector<int>> walls;
	fillMatrix(group, walls);

	std::vector<int> dimensions = { 10000, 0, 10000, 0 };
	getDimensions(group, dimensions);
	Coord me;
	Coord left;
	Coord up;
	int sides = 0;
	for (int i = dimensions[0]; i < dimensions[1]; i++)
	{
		for (int j = dimensions[2]; j < dimensions[3]; j++)
		{
			me = Coord(i, j);
			if (std::find(group.begin(), group.end(), me) != group.end())
			{
				left = Coord(i, j - 1);
				up = Coord(i - 1, j);

				bool foundleft = std::find(group.begin(), group.end(), left) != group.end();
				bool foundup = std::find(group.begin(), group.end(), up) != group.end();
					
				if (foundleft && !foundup)
				{ 
					//check left neighbor
					for (int k = 0; k < 4; k++)
					{
						if (!walls[left][k])
							if (walls[me][k])
								sides++;
					}
				}
				if (foundup && !foundleft)
				{
					// check upper neighbor
					for (int k = 0; k < 4; k++)
					{
						if (!walls[up][k])
							if (walls[me][k])
								sides++;
					}
				}
				if (foundup && foundleft)
				{
					// check both neighbors
					for (int k = 0; k < 4; k++)
					{
						if (!walls[left][k] && !walls[up][k])
							if (walls[me][k])
								sides++;
					}
				}
				if (!foundup && !foundleft)
				{
					// add all walls
					for (int k = 0; k < 4; k++)
					{
						sides += walls[me][k];
					}
				}
			}
		}
	}
	return sides;
}

int calculateBulkPrize(std::vector<std::vector<Coord>>& crop)
{
	int prize = 0;
	for (std::vector<Coord> group : crop)
	{
		prize += calculateArea(group) * getSidesForGroup(group);
	}
	return prize;
}

int calculateTotalBulkPrize(std::unordered_map<int, std::vector<std::vector<Coord>>>& regions)
{
	int totalPrize = 0;
	for (auto region : regions)
	{
		totalPrize += calculateBulkPrize(region.second);
	}
	return totalPrize;
}

int main()
{
	std::vector<std::string> lines = getLines("input.txt");
	SIZES = { int(lines.size()), int(lines[0].size()) };
	std::vector<Coord> toCheck;

	for (int i = 0; i < lines.size(); i++)
	{
		for (int j = 0; j < lines[0].size(); j++)
		{
			toCheck.push_back(Coord(i, j));
		}
	}

	std::unordered_map<int, std::vector<Coord>> crops;
	Coord current;
	int currentChar;
	for (int i = 0; i < lines.size(); i++)
	{
		for (int j = 0; j < lines[0].size(); j++)
		{
			current = Coord(i, j);
			currentChar = lines[i][j];
			if (crops.find(currentChar) == crops.end())
			{
				crops[currentChar] = { current };
			}
			else
			{
				crops[currentChar].push_back(current);
			}
		}
	}

	std::unordered_map<int, std::vector<std::vector<Coord>>> regions;
	for (auto crop : crops)
	{
		regions[crop.first] = divideInRegions(crop.second);
	}

	preResults(12, 2024);
	std::cout << calculateTotalPrize(regions) << "\n";
	std::cout << calculateTotalBulkPrize(regions) << "\n";
	afterResults();

	return 0;
}
