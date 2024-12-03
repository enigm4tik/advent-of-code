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

std::vector<std::string> getLines(std::string filename);

std::vector<int> splitLineToInt(std::string& line, char delimiter);
std::vector<std::vector<int>> splitToInt(std::vector<std::string>& puzzleinput, char delimiter);

std::vector<std::string> splitLineToString(std::string& line, std::string delimiter);
std::vector<std::vector<std::string>> splitToString(std::vector<std::string>& puzzleinput, std::string delimiter);

std::vector<int> findSubstringPositions(std::string& line, std::string substring);

void preResults(int); // ASCII Snow + Header
void afterResults(); // ASCII Snow