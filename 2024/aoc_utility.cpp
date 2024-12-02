#include "aoc_utility.h"

std::vector<std::string> getLines(std::string filename)
{
    std::vector<std::string> puzzle;
    std::string temp;
    std::ifstream f(filename);
    while (getline(f, temp))
        puzzle.push_back(temp);
    return puzzle;
}

std::vector<std::vector<int>> splitToInt(std::vector<std::string>& puzzleinput, char delimiter)
{
    std::vector<std::vector<int>> result;
    for (std::string line : puzzleinput)
    {
        std::vector<int> tokens;
        std::stringstream   mySstream(line);
        std::string         temp;

        while (getline(mySstream, temp, delimiter)) {
            int tempI = stoi(temp);
            tokens.push_back(tempI);
        }

        result.push_back(tokens);
    }

    return result;
}

void preResults(int day)
{
    std::cout << "- -      -     -   *  -    -     -      -  *  *  - -   " << std::endl;
    std::cout << "*   -    .   .    .       *     .  .   .    *       -  " << std::endl;
    std::cout << "Advent of Code 2024 - Day " << day << std::endl;
}
void afterResults()
{
    std::cout << "    -      .    -  *    -    -    *    .  .  .    *   -" << std::endl;
    std::cout << ".       .      *      -        -     *     .     .    ." << std::endl;
}