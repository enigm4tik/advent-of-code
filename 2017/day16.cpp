/* Advent of Code 
 * Day 16 
 */

#include "aoc_utility.h"

void spinPrograms(std::string &programs, int amount)
{
	std::string temp = programs.substr(programs.length() - amount);
	temp += programs.substr(0, programs.length() - amount);
	programs = temp;
}

void exchangePrograms(std::string& programs, int position1, int position2)
{
	std::string temp = programs.substr(position1, 1);
	programs[position1] = programs[position2];
	programs[position2] = temp[0];
}

void partnerPrograms(std::string& programs, std::string program1, std::string program2)
{
	int found1 = programs.find(program1);
	int found2 = programs.find(program2);
	exchangePrograms(programs, found1, found2);
}

void dance(std::string& programs, std::vector<std::string> &instructions)
{
	for (std::string instruction : instructions)
	{
		std::vector<int> positions;
		std::vector<std::string> partners;
		char type = instruction[0];
		std::string substring = instruction.substr(1);
		if (type == 's')
			spinPrograms(programs, stoi(substring));
		if (type == 'x')
		{
			positions = splitLineToInt(substring, '/');
			exchangePrograms(programs, positions[0], positions[1]);
		}
		if (type == 'p')
		{
			partners = splitLineToString(substring, "/");
			partnerPrograms(programs, partners[0], partners[1]);
		}
	}
}

int main()
{
	std::vector<std::string> puzzleInput = getLines("puzzle.txt");
	std::vector<std::string> instructions = splitLineToString(puzzleInput[0], ",");

	std::string programs = "abcdefghijklmnop";

	dance(programs, instructions);
	
	std::string afterOneDance = programs;
	int current = 0;
	int dances = 1000000000;
	int loop = 0;
	
	std::vector<std::string> dancepositions = { programs };

	while (current < dances)
	{
		dance(programs, instructions);
		dancepositions.push_back(programs);
		current++;
		if (programs == afterOneDance)
		{
			loop = current;
			current = dances;
		}
	}

	int positionInLoop = dances % loop;

	preResults(16, 2017);
	std::cout << "Part 1: " << afterOneDance << std::endl;
	std::cout << "Part 2: " << dancepositions[positionInLoop - 1] << std::endl;
	afterResults();

    return 0;
}