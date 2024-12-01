/** Advent of Code - 2024
 * Day 01
 **/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <ctype.h>
using namespace std;

vector<string> WRITTENDIGITS = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

vector<string> getLines(int lines, string filename)
{
    vector<string> puzzle;
    string temp;
    ifstream f(filename);
    while (getline(f, temp))
        puzzle.push_back(temp);
    return puzzle;
}

char getInteger(string& line)
{
    for (auto l : line)
    {
        if (isdigit(l))
        {
            return l;
        }
    }
}

void part1(vector<string>& puzzle)
{
    int calibrationSum = 0;
    for (string line : puzzle)
    {
        //cout << line << endl;
        char a = getInteger(line);
        string reverse = string(line.rbegin(), line.rend());
        char b = getInteger(reverse);
        string c = string() + a + b;
        int d = stoi(c);
        //cout << d << endl;
        calibrationSum += d;
    }

    cout << "Part 1: " << calibrationSum << endl;
}

void part2(vector<string>& puzzle)
{
    int part2sum = 0;

    for (string line : puzzle)
    {
        int smallestindex = line.length();
        int biggestindex = -1;
        string smallestdigit = "";
        string biggestdigit = "";
        int i = 1;

        for (int i = 0; i < 10; i++)
        {
            vector<pair<int, int>> bla;
            std::string::size_type pos = 0;
            for (;;)
            {
                pos = line.find(WRITTENDIGITS[i], pos);
                if (pos == line.npos)
                    break;
                bla.push_back(pair<int, int>(pos, i));
                ++pos;
            }
            for (auto b : bla)
            {
                if (b.first < smallestindex)
                {
                    smallestindex = b.first;
                    smallestdigit = to_string(b.second);
                }
                if (b.first > biggestindex)
                {
                    biggestindex = b.first;
                    biggestdigit = to_string(b.second);
                }
            }
        }

        for (int j = 1; j < 10; j++)
        {
            vector<pair<int, int>> bla;
            std::string::size_type pos = 0;
            for (;;)
            {
                pos = line.find(to_string(j), pos);
                if (pos == line.npos)
                    break;
                bla.push_back(pair<int, int>(pos, j));
                ++pos;
            }
            for (auto b : bla)
            {
                if (b.first < smallestindex)
                {
                    smallestindex = b.first;
                    smallestdigit = to_string(b.second);
                }
                if (b.first > biggestindex)
                {
                    biggestindex = b.first;
                    biggestdigit = to_string(b.second);
                }
            }
        }
        part2sum += stoi(smallestdigit + biggestdigit);
    }

    cout << "Part 2: " << part2sum << endl;
}

int main()
{
    // READING FROM FILE
    const int lines = 4;
    vector<string> puzzle = getLines(lines, "puzzle.txt");

    cout << "- -      -     -   *  -    -     -      -  *  *  - -   " << endl;
    cout << "*   -    .   .    .       *     .  .   .    *       -  " << endl;
    cout << "Advent of Code 2023 - Day 1" << endl;
    part1(puzzle);
    part2(puzzle);
    cout << "    -      .    -  *    -    -    *    .  .  .    *   -" << endl;
    cout << ".       .      *      -        -     *     .     .    ." << endl;

    return 0;
}
