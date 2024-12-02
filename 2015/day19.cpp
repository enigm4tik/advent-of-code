/*
 * Advent of Code - 2015
 * Day 15
 */ 

#include <iostream>
#include <vector>
#include <string>
#include "aoc_utility.h"
#include <set>
#include <regex>
#include <algorithm>
using namespace std;

string INPUT = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr";
int COUNTER = 1;

struct Substitution
{
	Substitution(string one, string two)
	{
		this->from = one;
		this->to = two;
	}
	string from;
	string to;
};

vector<Substitution> createSubstitutions(vector<string>& puzzle)
{
	vector<Substitution> substitutions;
	for (string line : puzzle)
	{
		bool found = false;
		int skip = 0;
		string one;
		string two;
		for (char l : line)
		{
			if (!found)
			{
				if (l != ' ')
					one += l;
				else
					found = true;
			}
			else
			{
				//cout << one << endl;
				if (skip < 3)
					skip++;
				else
					two += l;
			}
		}
		substitutions.push_back(Substitution(one, two));
	}
	return substitutions;
}

void substitute(Substitution &sub, string input, set<string> &found)
{
	int pos = 0;
	string changedInput = input;
	pos = input.find(sub.from, pos);
	while (pos >= 0)
	{
		string createdString = changedInput.replace(pos, sub.from.size(), sub.to);
		found.insert(createdString);
		pos = input.find(sub.from, pos+1);
		changedInput = input;
	}
	return;
}

void part1(vector<Substitution> &substitutions)
{
	set<string> uniquesubs;

	for (Substitution sub : substitutions)
	{
		substitute(sub, INPUT, uniquesubs);
	}

	cout << "Part 1: ";
	cout << uniquesubs.size() << endl;
}

string findTo(vector<Substitution>& substitutions, string match)
{
    // unused
	for (Substitution sub : substitutions)
	{
		if (sub.to == match)
		{
			return sub.from;
		}
	}
	return "empty";
}

void separateInElements(string &input, vector<string> &elements)
{
    //unused
	regex pattern("[A-Z][a-z]*");

	auto itBegin =
		std::sregex_iterator(input.begin(), input.end(), pattern);
	auto itEnd = std::sregex_iterator();
	for (std::sregex_iterator i = itBegin; i != itEnd; ++i)
	{
		std::smatch match = *i;
		std::string match_str = match.str();
		elements.push_back(match_str);
	}
}

void constructLonger(vector<string>& elements, vector<Substitution> substitutions)
{
    //unused
	int position_end = elements.size();
	int position_start = 0;
	for (int i = elements.size() - 1; i > 0; i--)
	{
		if (elements[i] == "Rn")
		{
			position_start = i; break;
		}
	}
	for (int i = position_start; i <= elements.size() - 1; i++)
	{
		if (elements[i] == "Ar")
		{
			position_end = i; break;
		}
	}
	string toFind;
	for (int i = position_start-1; i <= position_end; i++)
		toFind += elements[i];
	for (int i = position_start-1; i <= position_end; i++)
		if (i == position_end)
		{
			string found = findTo(substitutions, toFind);
			if (found == "empty")
				elements[position_start - 1] = toFind;
			else
				elements[position_start - 1] = found;
		}
		else 
			elements.erase(next(elements.begin(), position_start-1));
		

	return;
}

void printMolecule(vector<string>& elements)
{
    //unused
	cout << "Molecule: ";
	for (string x : elements)
		cout << x;
	cout << endl;
}

void moveOneStep(vector<string> &elements, vector<Substitution> substitutions, int pos = 0)
{
	//unused
	int position = elements.size() - 1 - pos;
	string left = elements[position - 1];
	string right = elements[position];

	string toFind;
	if (right == "Ar" || left == "Ar")
	{
		pos += 1;
		moveOneStep(elements, substitutions, pos);
		return;
	}
	if (left == "Rn")
	{	
		constructLonger(elements, substitutions);
		return;
	}
	else
	{
		toFind = elements[position - 1] + elements[position];
	}
	string found = findTo(substitutions, toFind);
	if (found == "empty") 
	{
		pos += 1;
		moveOneStep(elements, substitutions, pos);
		return;
	}
	else
	{
		COUNTER += 1;
		elements.erase(next(elements.begin(), position));
		if (found == "empty")
		{
			cout << "oh, oh!" << endl;
			return;
		}
		elements[position - 1] = found;
	}
	return;
}

int main()
{
	vector<string> lines = getLines("puzzle.txt");
	
	vector<Substitution> substitutions = createSubstitutions(lines);
	
	part1(substitutions);
	vector<string> elements;

	separateInElements(INPUT, elements);
	
	/* PART II 
	* For future reference:
	* I have spent hours trying to brute force and outsmart this puzzle.
	* After literally taking paper and pen and working the problem out, 
	* I realized that the elements are completely irrelevant.
	* I worked from the result backwards and replaced them with the one from the list. 
	* Everytime I did that, I clicked a counter. 
	* I tried it again, this time replacing them with F - it's the exact same result.
	* This is more of a mathematical, logical question than a coding puzzle. 
	* 
	* I then went on to the megasolutions and found this formula which gets the
	* exact same result: https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/
	* The following code is simply the implementation of the formula. 
	* 
	* For my sanity I'll leave the unused code in.
	*/
	
	int totalElements = elements.size();
	int RnandAr = count(elements.begin(), elements.end(), "Ar") + \
		count(elements.begin(), elements.end(), "Rn");
	int Y = count(elements.begin(), elements.end(), "Y");

	int feweststeps = totalElements - RnandAr - (Y * 2) - 1;
	cout << "Part 2: " << feweststeps << endl;

	return 0;	
}