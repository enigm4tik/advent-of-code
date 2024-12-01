/*
 * Advent of Code - 2015
 * Day 11
*/

#include <iostream>
#include <vector>
#include <set>
using namespace std;

bool checkSeq(vector<int>& password)
{
	// has a straight: at least 3 numbers are in sequence
	for (int i = 0; i < password.size() - 2; i++) {
		if (password[i] + 1 == password[i + 1] && password[i + 1] + 1 == password[i + 2])
			return true;
	}
	return false;
}

bool checkDoubles(vector<int>& password)
{
	// has at least two different pairs: 9797, 100100
	set<char> foundPairs;
	for (int i = 0; i < password.size() - 1; i++) {
		if (password[i] == password[i + 1])
			foundPairs.insert(password[i]);
	}
	if (foundPairs.size() > 1)
		return true;
	return false;
}

string turnToString(vector<int>& password)
{
	string passwordAsString;
	for (char p : password)
		passwordAsString += p;
	return passwordAsString;
}

vector<int> skipForbidden(vector<int>& password)
{
	for (int i = 0; i < password.size(); i++)
	{
		// has no forbidden numbers: 105, 111, 108
		if (password[i] == 105 || password[i] == 111 || password[i] == 108)
		{
			password[i] += 1;
			for (int j = i + 1; j < password.size(); j++)
				password[j] = 97;
		}
	}
	return password;
}

vector<int> increaseByOne(vector<int> &password, int pos)
{
	// a = 97
	// z = 122
	password[pos] += 1;
	if (password[pos] == 105 || password[pos] == 111 || password[pos] == 108)
		password[pos] += 1;
	if (password[pos] > 122)
	{
		password[pos] = 97;
		increaseByOne(password, pos - 1);
	}
return password;
}

void part1(vector<int> &password)
{
	password = increaseByOne(password, 7);
	skipForbidden(password);

	while (!checkSeq(password) || !checkDoubles(password))
	{
		skipForbidden(password);
		increaseByOne(password, 7);
	}
	
	cout << turnToString(password);
}

int main()
{
	string old_password = "cqjxjnds";

	vector<int> password;
	for (char p : old_password)
	{
		password.push_back(p);
	}
	
	// Find next password
	cout << "Part 1: ";
	part1(password);
	cout << endl;
	// Find the one after that
	cout << "Part 2: "; 
	part1(password);
	cout << endl;

	return 0;
}