#include <iostream>
#include <fstream>
#include "aoc_utility.h"
#include <algorithm>

using namespace std;

static void part1(vector<int> &firstList, vector<int> &secondList)
{
	int sumofdistances = 0;

	for (int i = 0; i < firstList.size(); i++)
	{
		int result;
		if (secondList[i] < firstList[i])
			result = (firstList[i] - secondList[i]);
		else
			result = (secondList[i] - firstList[i]);
		sumofdistances += result;
	}

	cout << "Part 1: " << sumofdistances << endl;
}

static void part2(vector<int> &firstList, vector<int> &secondList)
{
	int similarity = 0;
	for (int i = 0; i < firstList.size(); i++)
	{
		int multiplier = count(secondList.begin(), secondList.end(), firstList[i]);	
		similarity += firstList[i] * multiplier;
	}
	cout << "Part 2: " << similarity << endl;
}

int main()
{
	vector<string> lines = getLines("puzzle.txt");
	vector<int> firstList;
	vector<int> secondList;
	string delimiter = "   ";
	int SIZE = 5;

	for (string line : lines)
	{
		firstList.push_back(stoi(line.substr(0, SIZE)));
		auto second = line.find_first_not_of(' ', SIZE+1);
		secondList.push_back(stoi(line.substr(second, SIZE)));
	}

	// sort lists
	// for future reference the order is not important in part 2
	// so I can simply sort it outside and pass as reference
	sort(firstList.begin(), firstList.end());
	sort(secondList.begin(), secondList.end());

	cout << "- -      -     -   *  -    -     -      -  *  *  - -   " << endl;
	cout << "*   -    .   .    .       *     .  .   .    *       -  " << endl;
	cout << "Advent of Code 2024 - Day 1" << endl;
	part1(firstList, secondList);
	part2(firstList, secondList);
	cout << "    -      .    -  *    -    -    *    .  .  .    *   -" << endl;
	cout << ".       .      *      -        -     *     .     .    ." << endl;
	return 0;
}
