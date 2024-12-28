#pragma once
#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <set>
#include <queue>
#include <list>
#include <sstream>
#include <algorithm>
#include <unordered_map>
#include <bitset>
#include <cmath>
#include <map>

std::vector<std::string> getLines(std::string filename);

std::vector<int> splitLineToInt(std::string& line, char delimiter);
std::vector<std::vector<int>> splitToInt(std::vector<std::string>& puzzleinput, char delimiter);

std::vector<std::string> splitLineToString(std::string& line, std::string delimiter);
std::vector<std::vector<std::string>> splitToString(std::vector<std::string>& puzzleinput, std::string delimiter);

std::vector<int> findSubstringPositions(std::string& line, std::string substring);

void printVector(std::vector<int> &myVector);

int charNumberToInt(char& character);

void preResults(int day, int year); // ASCII Snow + Header
void afterResults(); // ASCII Snow

// Working with grids

struct Coord
{
	Coord();
	Coord(int i, int j);

	void printCoord();

	Coord operator +(Coord& other) const;

	Coord operator -(Coord& other) const;

	bool operator < (const Coord& other);

	bool operator > (const Coord& other);

	bool operator ==(const Coord& other);
	bool operator ==(const Coord& other) const;

	int x = 0;
	int y = 0;
};

template <>
struct std::hash<Coord>
{
	size_t operator()(const Coord& other) const
	{
		size_t xHash = std::hash<int>()(other.x);
		size_t yHash = std::hash<int>()(other.y) << 1;
		return xHash ^ yHash;
	}
};

bool operator <(const Coord& one, const Coord& other);
Coord operator +(const Coord& one, const Coord& other);
void addToVector(Coord& item, std::vector<Coord>& coordVector);
int getDistance(Coord& item, Coord& other);

// Creating Combinations with replacement

void createCombinations(int sampleCount, const std::string& options, std::string& combination, std::set<std::string>& operations);
void createCombinations(int sampleCount, const std::string& options, std::set<std::string>& operations);

void createCombinations(int sampleCount, const std::vector<Coord>& options, std::vector<Coord>& combination, std::set<std::vector<Coord>>& operations);
void createCombinations(int sampleCount, const std::vector<Coord> options, std::set<std::vector<Coord>>& operations);