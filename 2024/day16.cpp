/*
 * Advent of Code - 2024
 * Day 16
 */

#include "aoc_utility.h"

struct Node : public Coord
{
	Node(): Coord()
	{}

	Node(int x, int y, long s) 
	{
		this->x = x; 
		this->y = y;
		this->score = s;
	}
	Node(int x, int y)
	{
		this->x = x;
		this->y = y;
	}

	bool operator > (const Node& other)
	{
		return this->x > other.x || (!(other.x > this->x) && this->y > other.y);
	}
		
	long score = 1874919424;
	int step = 0;
	int turn = 0;
	int dir = 0;
};

Node getSmallestNode(std::vector<Node>& unvisitedNodes)
{
	Node smallestNode;
	int smallestValue = 1000000000;
	for (Node &node: unvisitedNodes)
	{
		if (node.score < smallestValue)
		{
			smallestValue = node.score;
			smallestNode = node;
		}
	}

	return smallestNode;
}

std::vector<Node> dijkstra(std::vector<Node>& unvisitedNodes, Node exitNode)
{
	std::sort(unvisitedNodes.begin(), unvisitedNodes.end(), std::greater<>());
	std::vector<Node> visited;
	Node currentNode;
	std::vector<Node> exitNodes;
	bool checked = true;
	while (unvisitedNodes.size())
	{

		currentNode = getSmallestNode(unvisitedNodes);
		visited.push_back(currentNode);
		unvisitedNodes.erase(std::find(unvisitedNodes.begin(), unvisitedNodes.end(), currentNode));

		long currentScore;
		int verticalPenalty;
		int horizontalPenalty;
		if (currentNode.dir == 0)
		{
			verticalPenalty = 0;
			horizontalPenalty = 1000;
		}
		else
		{
			horizontalPenalty = 0;
			verticalPenalty = 1000;
		}
		for (Node& node : unvisitedNodes)
		{
			if (node.x == currentNode.x + 1 && node.y == currentNode.y
				|| node.x == currentNode.x - 1 && node.y == currentNode.y)
			{
				currentScore = currentNode.score + verticalPenalty + 1;
				if (node.score > currentScore)
			
				{
					node.score = currentScore;
					node.turn = node.score / 1000;
					node.step = node.score %1000;
					if (verticalPenalty)
						node.dir = (currentNode.dir + 1) % 2;
					else
						node.dir = currentNode.dir;
					
				}
			}
			if (node.x == currentNode.x && node.y == currentNode.y + 1
				|| node.x == currentNode.x && node.y == currentNode.y - 1)
			{
				currentScore = currentNode.score + horizontalPenalty + 1;
				if (node.score > currentScore)
				{
					node.score = currentScore;
					node.turn = node.score / 1000;
					node.step = node.score % 1000;
					if (horizontalPenalty)
						node.dir = (currentNode.dir + 1) % 2;
					else
						node.dir = currentNode.dir;
				}
			}
		}
	}

	return visited;
}

std::vector<Node> getNeighbors(std::vector<Node>& shortestDistances, Node &currentNode)
{
	std::vector<Node> neighbors;
	for (Node &node : shortestDistances)
	{
		if (node.x == currentNode.x + 1 && node.y == currentNode.y
			|| node.x == currentNode.x - 1 && node.y == currentNode.y
			|| node.x == currentNode.x && node.y == currentNode.y + 1
			|| node.x == currentNode.x && node.y == currentNode.y - 1)
		{
			neighbors.push_back(node);
		}
	}
	return neighbors;
}

std::vector<Node> getNeighbors(std::vector<Node>& shortestDistances, Node& currentNode, std::vector<Node> &visited)
{
	std::vector<Node> neighbors;
	for (Node& node : shortestDistances)
	{
		if (node.x == currentNode.x + 1 && node.y == currentNode.y
			|| node.x == currentNode.x - 1 && node.y == currentNode.y
			|| node.x == currentNode.x && node.y == currentNode.y + 1
			|| node.x == currentNode.x && node.y == currentNode.y - 1)
		{
			if (std::find(visited.begin(), visited.end(), node) == visited.end())
				neighbors.push_back(node);
		}
	}
	return neighbors;
}

void printPaths(std::vector<Coord> visited, std::vector<std::string> lines)
{ 
	for (int i = 0; i < lines.size(); i++)
	{
		for (int j = 0; j < lines[0].size(); j++)
		{
			if (std::find(visited.begin(), visited.end(), Coord(i, j)) != visited.end())
				std::cout << "O";
			else 
			{
				std::cout << lines[i][j];
			}
		}
		std::cout << "\n";
	}
	std::cout << "\n";
}

void printPaths(std::vector<Node> visited, std::vector<int> sizes)
{
	for (int i = 0; i < sizes[0]; i++)
	{
		for (int j = 0; j < sizes[1]; j++)
		{
			bool found = false;
			for (auto &node : visited)
			{
				if (node.x == i && node.y == j)
				{
					/*if (node.score < 100000)
						std::cout << " ";*/
					if (node.score < 10000)
						std::cout << " ";
					if (node.score < 1000)
						std::cout << " ";
					if (node.score < 100)
						std::cout << " ";
					if (node.score < 10)
						std::cout << " ";
					std::cout << node.score << " ";
					found = true;
					continue;
				}
			}
			if (!found)
				std::cout << "##### ";
		}
		std::cout << "\n";
	}
	std::cout << "\n";
}


void getPointsOnShortestPaths(std::vector<Node>& shortestDistances, Node& exitNode, Node &currentNode, std::set<Node> &result, std::set<Node> &optimal, std::vector<Node> visited = {})
{
	if (currentNode == exitNode + Coord(0, -1) || currentNode == exitNode + Coord(1, 0))
	{
		int nextScore = currentNode.score + 1;
		int biggerNext = currentNode.score + 1001;
		if (exitNode.score == nextScore || exitNode.score == biggerNext)
		{
			//std::cout << "found a different path!\n";
			for (const Node &x : visited)
				result.insert(x);
			//std::set_union(result.begin(), result.end(), visited.begin(), visited.end());
			result.insert(currentNode);
			return;
		}
		return;
	}

	std::vector<Node> neighbors = getNeighbors(shortestDistances, currentNode, visited);
	for (Node& neighbor : neighbors)
	{
		if (std::find(visited.begin(), visited.end(), neighbor) != visited.end())
			continue;
		
		if (optimal.find(currentNode) == optimal.end() && optimal.find(neighbor) != optimal.end())
		{
			
			std::vector<Node> neighborOfNeighbor = getNeighbors(shortestDistances, neighbor);
			bool found = false;
			for (const Node &n : neighborOfNeighbor)
			{

				if (n.step == neighbor.step + 1 && optimal.find(n) != optimal.end())
					if (currentNode.turn <= n.turn)
						found = true;
			}
			
			if (found)
			{

			
				for (const Node& x : visited)
					result.insert(x);
				result.insert(currentNode);
			}
			else
				return;
		}

		if (currentNode.step == neighbor.step - 1)
		{
			visited.push_back(currentNode);
			getPointsOnShortestPaths(shortestDistances, exitNode, neighbor, result, optimal, visited);
				
		}
	}
	return;
}


std::set<Node> getOptimalPath(std::vector<Node>& shortestDistances, Node& exitNode, Node& startNode)
{
	Node currentNode = exitNode;
	std::set<Node> path;
	path.insert(exitNode);
	while (!((currentNode == startNode)))
	{
		std::vector<Node> neighbors = getNeighbors(shortestDistances, currentNode);

		currentNode = getSmallestNode(neighbors);
		path.insert(currentNode);
	}
	return path;
}	

int main()
{
	std::vector<Node> unvisitedNodes;

	std::vector<std::string> lines = getLines("input.txt");
	std::vector<int> sizes = {int(lines.size()), int(lines[0].size())};
	Node exitNode;
	Node startNode;
	for (int i = 0; i < lines.size(); i++)
	{
		for (int j = 0; j < lines[0].size(); j++)
		{
			if (lines[i][j] == 'S')
			{
				startNode = Node(i, j, 0);
				startNode.dir = 1;
				unvisitedNodes.push_back(startNode);
			}
			else if (lines[i][j] != '#')
			{
				if (lines[i][j] == 'E')
					exitNode = Node(i, j);
				unvisitedNodes.push_back(Node(i, j));
			}
		}
	}
	
	std::vector<Node> shortestDistances = dijkstra(unvisitedNodes, exitNode);
	std::sort(shortestDistances.begin(), shortestDistances.end());

	for (Node &node : shortestDistances)
	{
		if (node.x == exitNode.x && node.y == exitNode.y)
		{
			exitNode = node;
		}
	}

	std::set<Node> optimalPath = getOptimalPath(shortestDistances, exitNode, startNode);
	getPointsOnShortestPaths(shortestDistances, exitNode, startNode, optimalPath, optimalPath);

	preResults(16, 2024);
	std::cout << "Part 1: " << exitNode.score << "\n";
	std::cout << "Part 2: " << optimalPath.size() << "\n";
	afterResults();

	return 0;
}
