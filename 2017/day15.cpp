/* Advent of Code 2017 
 * Day 15
 */

#include "aoc_utility.h"

int DIVISOR = 2147483647;

long long generateNumber(long long &value, int &factor)
{
	return (value * factor) % DIVISOR;
}

long long generateNumberPart2(long long& value, int& factor, int mask)
{
	long long candidate = generateNumber(value, factor);
	bool calculating = true;
	while (calculating)
	{ 
		if ((candidate & mask) == 0)
			calculating = false;
		else
			candidate = generateNumber(candidate, factor);
	}
	return candidate;
}

int part1(int startA, int startB, int factorA, int factorB)
{
	std::vector<long long> generatorA = { startA * factorA };
	std::vector<long long> generatorB = { startB * factorB };

	int found_matches = 0;
	int current = 0;
	int calculations = 40000000;
	long long generatedA = generatorA.back();
	long long generatedB = generatorB.back();
	int mask = 0x0000000000000000FFFF;
	while (current < calculations)
	{
		generatedA = generateNumber(generatedA, factorA);
		generatedB = generateNumber(generatedB, factorB);
		if ((generatedA & mask) == (generatedB & mask))
		{
			found_matches++;
		}
		current++;
	}
	return found_matches;
}

int part2(int startA, int startB, int factorA, int factorB)
{
	long long longA = startA; 
	long long longB = startB;
	int maskA = 3; // 0011
	int maskB = 7; // 0111
	int mask = 0x0000000000000000FFFF;
	long long generatedA = generateNumberPart2(longA, factorA, maskA);
	long long generatedB = generateNumberPart2(longB, factorB, maskB);

	int calculations = 5000000;
	int current = 0;
	int found_matches = 0;
	while (current < calculations)
	{
		generatedA = generateNumberPart2(generatedA, factorA, maskA);
		generatedB = generateNumberPart2(generatedB, factorB, maskB);

		if ((generatedA & mask) == (generatedB & mask))
		{
			found_matches++;
		}
		current++;
	}
	return found_matches;
}

int main()
{
	int startA = 65;
	int factorA = 16807;
	int startB = 8921;
	int factorB = 48271;

	int resultPart1 = part1(startA, startB, factorA, factorB);
	int resultPart2 = part2(startA, startB, factorA, factorB);

	preResults(15, 2017);
	std::cout << "Part 1: " << resultPart1 << std::endl;
	std::cout << "Part 2: " << resultPart2 << std::endl;
	afterResults();

	return 0;
}
