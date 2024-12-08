/*
 * Advent of Code - 2024
 * Day 2
 */

#include "aoc_utility.h"

bool checkDirection(std::vector<int>& report)
{
	bool initial = report[0] > report[1] && report[0] != report[1];
	
	for (int i = 0; i < report.size()-1; i++)
	{
		if ((report[i] > report[i + 1]) != initial)
			return false;
	}
	return true;
}

std::set<int> checkDirection(std::vector<int>& report, bool remove)
{
	bool initial = report[0] > report[1];
	bool initial2 = report[1] > report[2];
	std::set<int> badIndices;
	for (int i = 0; i < report.size() - 1; i++)
	{
		if (i == 0)
		{
			if ((report[i] > report[i + 1]) != initial2)
			{
				badIndices.insert(i + 1);
				badIndices.insert(i);
			}
		}
		if ((report[i] > report[i + 1]) != initial)
		{
			badIndices.insert(i + 1);
			badIndices.insert(i);
		}

		if (report[i] == report[i + 1])
		{ 
			badIndices.insert(i);
			badIndices.insert(i+1);
		}
			
	}
	return badIndices;
}

bool checkLevels(std::vector<int>& report)
{
	for (int i = 0; i < report.size() - 1; i++)
	{
		int calc = report[i] - report[i + 1];
		if (calc < 0)
		{
			if (calc < -3 || calc > -1)
				return false;
		}
		else
		{
			if (calc < 1 || calc > 3)
				return false;
		}
	}
	return true;
}

std::set<int> checkLevels(std::vector<int>& report, bool)
{
	std::set<int> badIndices;
	for (int i = 0; i < report.size() - 1; i++)
	{
		int calc = report[i] - report[i + 1];
		if (calc < 0)
		{
			if (calc < -3 || calc > -1)
			{
					badIndices.insert(i + 1);
					badIndices.insert(i);
			}
		}
		else
		{
			if (calc < 1 || calc > 3)
			{
				badIndices.insert(i + 1); 
				badIndices.insert(i);
			}
				
		}
	}
	return badIndices;
}

void part1(std::vector<std::vector<int>> &reports)
{
	int safeReports = 0;
	for (auto report : reports)
	{
		if (checkDirection(report) && checkLevels(report))
				safeReports++;
	}
	std::cout << "Part 1: " << safeReports << std::endl;
}

void removeUnsafe(std::vector<int> &report, std::set<int> &baddies, std::vector<std::vector<int>> &tryAgain)
{
	std::vector<int> tempReport = report;
	for (int baddie : baddies)
	{
		tempReport.erase(std::next(tempReport.begin(), baddie));
		tryAgain.push_back(tempReport);
		tempReport = report;
	}
}

void part2(std::vector<std::vector<int>> &reports)
{
	int safeReports = 0;
	for (auto report : reports)
	{
		std::set<int> baddies;
		if (checkDirection(report))
		{
			if (checkLevels(report))
			{
				safeReports++;
			}
			else
			{
				baddies = checkLevels(report, true);
			}
		}
		else
		{
			baddies = checkDirection(report, true);
		}

		if (baddies.size() > 0)
		{
			std::vector<std::vector<int>> tryAgain;
			removeUnsafe(report, baddies, tryAgain);
			bool safe = false;
			for (auto tryAgainReport : tryAgain)
			{
				if (checkDirection(tryAgainReport) && checkLevels(tryAgainReport))
				{
					safeReports++;
					safe = true;
					break;
				}
			}
		}
	}
	std::cout << "Part 2: " << safeReports << std::endl;
}

int main()
{
	std::vector<std::string> lines = getLines("input.txt");
	std::vector <std::vector<int>> reports;

	reports = splitToInt(lines, ' ');

	preResults(2, 2024);
	part1(reports);
	part2(reports);
	afterResults();
	return 0;
}