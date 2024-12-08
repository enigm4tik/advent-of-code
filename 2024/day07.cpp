/* Advent of Code
 * Day 07
 */

#include "aoc_utility.h"

long long calculateOperation(int operand, char operator_, long long& result)
{
	if (operator_ == '*')
	{
		result *= operand;
	}
	if (operator_ == '+')
	{
		result += operand;
	}
	if (operator_ == '|')
	{
		std::string temp1 = std::to_string(result);
		std::string temp2 = std::to_string(operand);
		std::string concatenated = temp1 + temp2;
		result = stoll(concatenated);

	}
	return result;
}

void calculateResult(std::vector<int>& operands, const std::string& operators, long long &result)
{
	result = operands[0];
	for (int i = 1; i < operands.size(); i++)
	{
		result = calculateOperation(operands[i], operators[i - 1], result);
	}
}

long long getCalibrationResult(std::vector<std::pair<long long, std::vector<int>>> &test, std::string operators)
{
	long long report = 0;
	for (auto pair : test)
	{
		std::set<std::string> operations;
		createCombinations(pair.second.size() - 1, operators, operations);
		long long result;
		while (operations.size() > 0)
		{
			calculateResult(pair.second, *operations.begin(), result);
			if (result == pair.first)
			{
				report += pair.first;
				break;
			}
			operations.erase(operations.begin());
		}
	}
	return report;
}

int main()
{
	std::vector<std::string> lines = getLines("input.txt");
	std::vector<std::pair<long long, std::vector<int>>> test;

	for (std::string line : lines)
	{
		std::vector<std::string> leftRight = splitLineToString(line, ": ");
		std::vector<int> operands = splitLineToInt(leftRight[1], ' ');
		std::pair<long long, std::vector<int>> myPair = std::make_pair(stoll(leftRight[0]), operands);
		test.push_back(myPair);
	}

	long long report = 0;

	std::string operators = "*+";

	long long part1 = getCalibrationResult(test, operators);

	operators = "*+|";

	long long part2 = getCalibrationResult(test, operators);
	
	preResults(7, 2024);
	std::cout << "Part 1: " << part1 << std::endl;
	std::cout << "Part 2: " << part2 << std::endl;
	afterResults();

	std::cout << report << std::endl;
	return 0;
}