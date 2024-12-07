#include "aoc_utility.h"

void preResults(int day, int year)
{
    std::cout << "- -      -     -   *  -    -     -      -  *  *  - -   " << std::endl;
    std::cout << "*   -    .   .    .       *     .  .   .    *       -  " << std::endl;
    std::cout << "Advent of Code " << year << " - Day " << day << std::endl;
}
void afterResults()
{
    std::cout << "    -      .    -  *    -    -    *    .  .  .    *   -" << std::endl;
    std::cout << ".       .      *      -        -     *     .     .    ." << std::endl;
}

std::vector<std::string> getLines(std::string filename)
{
    std::vector<std::string> puzzle;
    std::string temp;
    std::ifstream f(filename);
    while (getline(f, temp))
        puzzle.push_back(temp);
    return puzzle;
}

std::vector<int> splitLineToInt(std::string& line, char delimiter)
{
    std::vector<int> tokens;
    std::stringstream   mySstream(line);
    std::string         temp;

    while (getline(mySstream, temp, delimiter)) {
        try
        {
            int tempI = stoi(temp);
            tokens.push_back(tempI);
        }
        catch (const std::invalid_argument& ia) {
            // Skipping unintable values
        }
    }

    return tokens;
}

std::vector<std::string> splitLineToString(std::string& line, std::string delimiter)
{
    std::vector<std::string> substrings;
    std::vector<int> positions = findSubstringPositions(line, delimiter);

    int initial = 0;
    int length = 0;
    for (int pos : positions)
    {
        length = pos - initial;
        std::string temp = line.substr(initial, length);
        initial = pos + delimiter.length();
        substrings.push_back(temp);
    }
    return substrings;
}

std::vector<std::vector<int>> splitToInt(std::vector<std::string>& puzzleinput, char delimiter)
{
    std::vector<std::vector<int>> result;
    for (std::string line : puzzleinput)
    {
        result.push_back(splitLineToInt(line, delimiter));
    }

    return result;
}

std::vector<std::vector<std::string>> splitToString(std::vector<std::string>& puzzleinput, std::string delimiter)
{
    std::vector<std::vector<std::string>> result;
    for (std::string line : puzzleinput)
    {
        result.push_back(splitLineToString(line, delimiter));
    }

    return result;
}

std::vector<int> findSubstringPositions(std::string& line, std::string substring)
{
    std::vector<int> positions;
    size_t pos = line.find(substring, 0);
    while (pos != std::string::npos)
    {
        positions.push_back(pos);
        pos = line.find(substring, pos + substring.length());
    }

    positions.push_back(line.size());

    return positions;
}

void printVector(std::vector<int> &myVector)
{
    for (int x : myVector)
        std::cout << x << ", ";
    std::cout << std::endl;
}