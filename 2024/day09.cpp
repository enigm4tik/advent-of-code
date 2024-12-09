/* Advent of Code 2024
 * Day 09
 */

#include "aoc_utility.h"

int charNumberToInt(char& character)
{
	int result = character - '0';
	return result++;
}

std::vector<int> createSpan(int pos, int length)
{
	std::vector<int> programPositions;
	for (int i = pos; i < pos + length; i++)
		programPositions.push_back(i);
	return programPositions;
}

void parseData(std::string &inputData, std::unordered_map<int, std::vector<int>> &fileSystem, std::vector<int> &freeSpace)
{
	int programID = 0;
	std::vector<int> temp;
	int length;
	int free = 0;
	for (int i = 0; i < inputData.length(); i++)
	{
		length = charNumberToInt(inputData[i]);
		if ((i % 2) == 0) // every other is a file
		{
			fileSystem[programID] = createSpan(free, length);
			if (fileSystem[programID].size() > 0)
				free = fileSystem[programID].back() + 1;
			programID++;
		}
		else // every other is free
		{ 
			temp = createSpan(free, length);
			if (temp.size() > 0)
			{
				free = temp.back() + 1;
				freeSpace.insert(freeSpace.end(), temp.begin(), temp.end());
			}
				
		}
	}
}

void defragment(std::unordered_map<int, std::vector<int>>& fileSystem, std::vector<int> &freeSpace)
{
	int free = freeSpace.front();
	for (int i = fileSystem.size() - 1; i >= 0; i--)
	{
		for (int j = fileSystem[i].size()-1; j >= 0; j--)
		{
			if (fileSystem[i][j] > free)
			{
				fileSystem[i][j] = free;
				freeSpace.erase(freeSpace.begin());
				free = freeSpace.front();
			}
			else
				break;
		}
		std::sort(fileSystem[i].begin(), fileSystem[i].end());
	}
}

void parseData(std::string& inputData, std::unordered_map<int, std::vector<int>>& fileSystem, std::vector<std::vector<int>>& freeSpace)
{
	int programID = 0;
	std::vector<int> temp;
	int length;
	int free = 0;
	for (int i = 0; i < inputData.length(); i++)
	{
		length = charNumberToInt(inputData[i]);
		if ((i % 2) == 0)
		{
			fileSystem[programID] = createSpan(free, length);
			if (fileSystem[programID].size() > 0)
				free = fileSystem[programID].back() + 1;
			programID++;
		}
		else
		{
			temp = createSpan(free, length);
			if (temp.size() > 0)
			{
				free = temp.back() + 1;
				freeSpace.push_back(temp);
			}

		}
	}
}

std::vector<int> moveChunk(std::vector<int> &freeSector, std::vector<int> &chunk)
{
	for (int k = 0; k < chunk.size(); k++)
	{
		chunk[k] = freeSector[k];
	}
	freeSector.erase(freeSector.begin(), freeSector.begin() + (chunk.size()));
	return freeSector;
}

void defragmentChunks(std::unordered_map<int, std::vector<int>>& fileSystem, std::vector<std::vector<int>>& freeSpace, std::vector<int> &sortedPrograms)
{
	std::vector<int> free;
	bool moved;
	for (int sortedProgram: sortedPrograms)
	{
		moved = false;
		for (int j = 0; j < freeSpace.size(); j++)
		{
			if (freeSpace[j].size() >= fileSystem[sortedProgram].size() && !moved)
			{
				if (fileSystem[sortedProgram][0] > freeSpace[j][0])
				{
					freeSpace[j] = moveChunk(freeSpace[j], fileSystem[sortedProgram]);
					moved = true;
				}
				else
					break;
			}
		}
	}
}

long long calculateCheckSum(std::unordered_map<int, std::vector<int>> &fileSystem)
{
	long long checkSum = 0;
	for (auto file : fileSystem)
		for (int program : file.second)
			checkSum += (file.first * program);
	return checkSum;
}

std::vector<int> getSortedKeys(std::unordered_map<int, std::vector<int>> unorderedMap)
{
	std::vector<int> sortedPrograms;
	for (auto keyValuePair : unorderedMap)
		sortedPrograms.push_back(keyValuePair.first);
	std::sort(sortedPrograms.begin(), sortedPrograms.end());
	std::reverse(sortedPrograms.begin(), sortedPrograms.end());
	return sortedPrograms;
}

int main()
{
	
	std::vector<std::string> data = getLines("input.txt");
	std::string inputData = data[0];
	std::vector<int> freeSpace;
	std::unordered_map<int, std::vector<int>> fileSystem;

	parseData(inputData, fileSystem, freeSpace);
	defragment(fileSystem, freeSpace);
	
	long long checkSumPart1 = calculateCheckSum(fileSystem);

	// Part 2

	std::vector<std::vector<int>> freeChunks;
	std::unordered_map<int, std::vector<int>> fileSystemPart2;

	parseData(inputData, fileSystemPart2, freeChunks);
	std::vector<int> sortedPrograms = getSortedKeys(fileSystemPart2);
	defragmentChunks(fileSystemPart2, freeChunks, sortedPrograms);

	long long checkSumPart2 = calculateCheckSum(fileSystemPart2);

	preResults(9, 2024);
	std::cout << checkSumPart1 << std::endl;
	std::cout << checkSumPart2 << std::endl;
	afterResults();

	return 0;
}