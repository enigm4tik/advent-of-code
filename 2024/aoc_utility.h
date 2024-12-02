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
std::vector<std::vector<int>> splitToInt(std::vector<std::string>& puzzleinput, char delimiter);

void preResults(int); // ASCII Snow + Header
void afterResults(); // ASCII Snow