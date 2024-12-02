#include "aoc_utility.h"

vector<string> getLines(string filename)
{
    vector<string> puzzle;
    string temp;
    ifstream f(filename);
    while (getline(f, temp))
        puzzle.push_back(temp);
    return puzzle;
}
