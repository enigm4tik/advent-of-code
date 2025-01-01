/*
 * Advent of Code - 2024
 * Day 23
 */

#include "aoc_utility.h"


std::set<std::string> getBiggestGroup(std::string computer, std::unordered_map<std::string, std::set<std::string>>& pcConnections)
{
	std::set<std::string> partners = pcConnections[computer];
	partners.insert(computer);
	
	for (std::string partner : pcConnections[computer])
	{
		if (std::find(partners.begin(), partners.end(), partner) != partners.end())
		{
			std::set<std::string> temp;
			std::set<std::string> partnerSet = pcConnections[partner];
			partnerSet.insert(partner);
			std::set_intersection(partners.begin(), partners.end(), partnerSet.begin(), partnerSet.end(), std::inserter(temp, temp.end()));
			partners = temp;
		}
	}

	return partners;
}

std::vector<std::string> getPassword(std::unordered_map<std::string, std::set<std::string>>& pcs)
{
	int biggestSize = 0;
	std::set<std::string> biggestGroup;
	std::set<std::string> candidate;
	for (auto pc : pcs)
	{
		candidate = getBiggestGroup(pc.first, pcs);
		if (candidate.size() > biggestSize)
		{
			biggestGroup = candidate;
			biggestSize = candidate.size();
		}
	}

	std::vector<std::string> password;
	for (std::string pc : biggestGroup)
		password.push_back(pc);
	std::sort(password.begin(), password.end());

	return password;
}

void parsePCConncetions(std::vector<std::vector<std::string>> &pcConnections, std::unordered_map<std::string, std::set<std::string>> &pcs)
{
	std::string pc1, pc2;
	for (std::vector<std::string> pcConnection : pcConnections)
	{
		pc1 = pcConnection[0];
		pc2 = pcConnection[1];
		if (pcs.find(pc1) != pcs.end())
			pcs[pc1].insert(pc2);
		else
			pcs[pc1] = { pc2 };
		if (pcs.find(pc2) != pcs.end())
			pcs[pc2].insert(pc1);
		else
			pcs[pc2] = { pc1 };
	}
}

void findGroupsOfPCs(std::unordered_map<std::string, std::set<std::string>> &pcs, std::vector < std::set<std::string>> &found)
{
	std::vector<std::string> seen;
	for (std::pair<std::string, std::set<std::string>> computer : pcs)
	{
		for (std::string partner : computer.second)
		{
			std::set<std::string> xx = { computer.first, partner };
			for (std::string conn : pcs[partner])
			{
				if (std::find(seen.begin(), seen.end(), conn) == seen.end())
				{
					if (std::find(computer.second.begin(), computer.second.end(), conn) != computer.second.end())
					{
						xx.insert(conn);
						if (std::find(found.begin(), found.end(), xx) == found.end())
							found.push_back(xx);
						xx.erase(conn);
					}
				}
			}
		}
		seen.push_back(computer.first);
	}
}

int func(std::vector < std::set<std::string>> groupsOfPCs)
{
	int groupsWithT = 0;
	for (auto group : groupsOfPCs)
	{
		if (group.size() == 3)
		{
			for (std::string pc : group)
			{
				if (pc.find("t") == 0)
				{
					groupsWithT++;
					break;
				}
			}
		}
	}
	return groupsWithT;

}

int main()
{
	std::vector<std::string> lines = getLines("input.txt");
	std::vector<std::vector<std::string>> pcConnections = splitToString(lines, "-");

	std::unordered_map<std::string, std::set<std::string>> pcs;
	
	parsePCConncetions(pcConnections, pcs);
	std::vector < std::set<std::string>> found;
	findGroupsOfPCs(pcs, found);
	int res = func(found);
	
	preResults(23, 2024);
	std::cout << "Part 1: " << res << "\n";
	
	// Part 2
	std::cout << "Part 2: ";
	std::vector<std::string> password = getPassword(pcs);
	for (int i = 0; i < password.size(); i++)
	{
		if (i != 0)
			std::cout << ",";
		std::cout << password[i];
	}
	std::cout << "\n";
	afterResults();

	return 0;
}