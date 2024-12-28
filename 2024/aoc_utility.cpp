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
    for (int i = 0; i < myVector.size(); i++)
    {
        if (i != 0)
            std::cout << ", ";
        std::cout << myVector[i];
    }
    std::cout << std::endl;
}

int charNumberToInt(char& character)
{
    int result = character - '0';
    return result++;
}

// Working with grids ////////////////////////////////////////////////////////////

Coord::Coord()
{
    this->x = 0;
    this->y = 0;
}

Coord::Coord(int i, int j)
{
    this->x = i;
    this->y = j;
}

void Coord::printCoord()
{
    std::cout << "(" << x << ", " << y << ")";
}

Coord Coord::operator +(Coord& other) const
{
    return Coord(this->x + other.x, this->y + other.y);
}

Coord Coord::operator -(Coord& other) const
{
    return Coord(this->x - other.x, this->y - other.y);
}

bool Coord::operator < (const Coord& other)
{
    return this->x < other.x || (!(other.x < this->x) && this->y < other.y);
}

bool Coord::operator > (const Coord& other)
{
    return this->x > other.x || (!(other.x > this->x) && this->y > other.y);
}

bool Coord::operator ==(const Coord& other)
{
    return this->x == other.x && this->y == other.y;
}

bool Coord::operator ==(const Coord& other) const
{
    return this->x == other.x && this->y == other.y;
}

bool operator <(const Coord& one, const Coord& other)
{
    return one.x < other.x || (!(other.x < one.x) && one.y < other.y);
}

Coord operator +(const Coord& one, const Coord& other)
{
    return Coord(one. x+ other.x, one.y+ other.y);
}

void addToVector(Coord& item, std::vector<Coord>& coordVector)
{
    if (std::find(coordVector.begin(), coordVector.end(), item) == coordVector.end())
    {
        coordVector.push_back(item);
    }
}

int getDistance(Coord& item, Coord& other)
{
    return std::abs(item.x - other.x) + std::abs(item.y - other.y);
}

// Creating Combinations with replacement //////////////////////////////////////

void createCombinations(int sampleCount, const std::string& options, std::string& combination, std::set<std::string>& operations) {
    if (combination.size() == sampleCount) {
        operations.insert(combination);
    }
    else {
        combination.push_back(0);
        for (char op : options) {
            combination.back() = op;
            createCombinations(sampleCount, options, combination, operations);
        }
        combination.pop_back();
    }
}

void createCombinations(int sampleCount, const std::string& options, std::set<std::string>& operations) {
    std::string stack;
    createCombinations(sampleCount, options, stack, operations);
}

void createCombinations(int sampleCount, const std::vector<Coord>& options, std::vector<Coord>& combination, std::set<std::vector<Coord>>& operations) {
    if (combination.size() == sampleCount) {
        operations.insert(combination);
    }
    else {
        combination.push_back(Coord(0, 0));
        for (Coord op : options) {
            combination.back() = op;
            createCombinations(sampleCount, options, combination, operations);
        }
        combination.pop_back();
    }
}

void createCombinations(int sampleCount, const std::vector<Coord> options, std::set<std::vector<Coord>>& operations) {
    std::vector<Coord> stack;
    createCombinations(sampleCount, options, stack, operations);
}