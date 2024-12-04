/*
 * Advent of Code - 2024
 * Day 4
 */

#include "aoc_utility.h"

bool isXMAS(std::string candidate, std::string testString="XMAS")
{
	std::string reverseCandidate = std::string(candidate.rbegin(), candidate.rend());
	if (testString == candidate || testString == reverseCandidate)
		return 1;
	return 0;
}

int getHorizontalXMAS(std::vector<std::string>& wordSearch)
{
	int horizontalFound = 0;
	for (int i = 0; i < wordSearch.size(); i++)
	{
		for (int k = 0; k < wordSearch[0].size() - 3; k++)
		{
			std::string testString;
			for (int l = 0; l < 4; l++)
				testString += wordSearch[i][k + l];
			
			if (isXMAS(testString))
				horizontalFound++;
		}
	}
	return horizontalFound;
}

int getVerticalXMAS(std::vector<std::string>& wordSearch)
{
	int verticalFound = 0;
	for (int i = 0; i < wordSearch.size(); i++)
	{
		for (int k = 0; k < wordSearch.size() - 3; k++)
		{
			std::string testString;
			for (int l = 0; l < 4; l++)
				testString += wordSearch[k+l][i];

			if (isXMAS(testString))
				verticalFound++;
		}
	}
	return verticalFound;
}

int getdiagOneXMAS(std::vector<std::string>& wordSearch, std::string searchString = "XMAS")
{
	int diagonalFound = 0;
	int adjusted = searchString.length() - 1;
	for (int i = 0; i < wordSearch.size(); i++)
	{
		for (int k = 0; k < wordSearch[0].size(); k++)
		{
			if ((k + adjusted) >= wordSearch[0].size())
				continue;
			if ((i + adjusted) >= wordSearch[0].size())
				continue;

			std::string testString;
			for (int l = 0; l < searchString.size(); l++)
				testString += wordSearch[i + l][k + l];
				
			if (isXMAS(testString, searchString))
				diagonalFound++;
		}
	}
	return diagonalFound;
}

int getdiagTwoXMAS(std::vector<std::string>& wordSearch, std::string searchString = "XMAS")
{
	int diagonalFound = 0;
	int adjusted = searchString.length() - 1;

	for (int i = 0; i < wordSearch.size(); i++)
	{
		for (int k = 0; k < wordSearch[0].size(); k++)
		{
			if ((k + adjusted) >= wordSearch[0].size())
				continue;
			if ((i + adjusted) >= wordSearch[0].size())
				continue;

			std::string testString;
			for (int l = 0; l < searchString.size(); l++)
				testString += wordSearch[i + l][k + searchString.length() - l - 1];
			
			if (isXMAS(testString, searchString))
				diagonalFound++;
		}
	}
	return diagonalFound;
}

int part2(std::vector<std::string> &wordSearch)
{
	int MASfound = 0;
	for (int i = 0; i < wordSearch.size() - 2; i++)
	{
		for (int j = 0; j < wordSearch.size() - 2; j++)
		{
			std::string rowString;
			std::vector<std::string> window;

			for (int l = 0; l < 3; l++)
				rowString += wordSearch[i][j + l];
			window.push_back(rowString);
			rowString = "";

			for (int l = 0; l < 3; l++)
				rowString += wordSearch[i+1][j + l];
			window.push_back(rowString);
			rowString = "";

			for (int l = 0; l < 3; l++)
				rowString += wordSearch[i+2][j + l];
			window.push_back(rowString);

			if (getdiagOneXMAS(window, "MAS") && getdiagTwoXMAS(window, "MAS"))
				MASfound++;
		}
	}
		
	return MASfound;
}

int main()
{
	std::vector<std::string> wordSearch = getLines("puzzle.txt");

	int foundXMAS = 0;
	int horizontalXMAS = getHorizontalXMAS(wordSearch);
	int verticalXMAS = getVerticalXMAS(wordSearch);
	int diagonalXMAS = getdiagOneXMAS(wordSearch);
	int diagonalXMAS2 = getdiagTwoXMAS(wordSearch);

	foundXMAS = horizontalXMAS + verticalXMAS + diagonalXMAS + diagonalXMAS2;
	
	int foundMAS = part2(wordSearch);

	preResults(4, 2024);
	std::cout << "Part 1: " << foundXMAS << std::endl;
	std::cout << "Part 2: " << foundMAS << std::endl;
	afterResults();

	return 0;
}
