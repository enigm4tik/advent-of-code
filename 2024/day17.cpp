/*
 * Advent of Code - 2024
 * Day 17
 */

#include "aoc_utility.h"

void printRegisters(std::unordered_map<char, long long>& registers)
{
	for (std::pair<char, long long> reg: registers)
	{
		std::cout << reg.first << ": " << reg.second << "\n";
	}
}

void printProgramlist(std::vector<int>& programList)
{
	for (int program : programList)
		std::cout << program << " - ";
	std::cout << "\n";
}

long long comboOperand(int operand, std::unordered_map<char, long long> &registers)
{
	if (operand <= 3)
		return operand;
		
	if (operand == 4)
		return registers['A'];
		
	if (operand == 5)
		return registers['B'];
		
	if (operand == 6)
		return registers['C'];
		
	if (operand == 7)
		return -1;
}

void adv(std::unordered_map<char, long long> &registers, long long operand)
{
	operand = comboOperand(operand, registers);
	long denominator = std::pow(2, operand);
	long long result = registers['A'] / denominator;
	registers['A'] = result;
}

void bdv(std::unordered_map<char, long long>& registers, long long operand)
{
	operand = comboOperand(operand, registers);
	long denominator = std::pow(2, operand);
	long long result = registers['A'] / denominator;
	registers['B'] = result;
}

void cdv(std::unordered_map<char, long long>& registers, long long operand)
{
	operand = comboOperand(operand, registers);
	long denominator = std::pow(2, operand);
	long long result = registers['A'] / denominator;
	registers['C'] = result;
}

void bxl(std::unordered_map<char, long long>& registers, int operand)
{
	long long result = registers['B'] ^ operand;
	registers['B'] = result;
}

void bxc(std::unordered_map<char, long long>& registers, int operand)
{
	long long result = registers['B'] ^ registers['C'];
	registers['B'] = result;
}

void bst(std::unordered_map<char, long long>& registers, long long operand)
{
	operand = comboOperand(operand, registers);
	long long result = operand % 8;
	registers['B'] = result;
}

void jnz(std::unordered_map<char, long long>& registers, int operand)
{
	if (registers['A'] == 0)
	{
		registers['I'] += 2;
		return;
	}
	registers['I'] = operand;
}

bool out(std::unordered_map<char, long long>& registers, long long operand, std::vector<int> &outList)
{
	operand = comboOperand(operand, registers);
	int result = operand % 8;
	outList.push_back(result);
	return true;
}

void runProgram(std::unordered_map<char, long long>& registers, std::vector<int>&programList, std::vector<int> &outList)
{
	while (registers['I'] < programList.size() - 1)
	{
		long long opcode = programList[registers['I']];
		long long operand = programList[registers['I'] + 1];

		switch (opcode)
		{
		case 0:
			adv(registers, operand);
			registers['I'] += 2;
			break;
		case 1:
			bxl(registers, operand);
			registers['I'] += 2;
			break;
		case 2:
			bst(registers, operand);
			registers['I'] += 2;
			break;
		case 3:
			jnz(registers, operand);
			break;
		case 4:
			bxc(registers, operand);
			registers['I'] += 2;
			break;
		case 5:
			out(registers, operand, outList);
			registers['I'] += 2;
			break;
		case 6:
			bdv(registers, operand);
			registers['I'] += 2;
			break;
		case 7:
			cdv(registers, operand);
			registers['I'] += 2;
			break;
		}
	}
}

void part1(std::vector<int> programList, long long registerA)
{
	std::vector<int> outList;
	std::unordered_map<char, long long> registers;
	registers['A'] = registerA;
	registers['B'] = 0;
	registers['C'] = 0;
	registers['I'] = 0;
	runProgram(registers, programList, outList);
	for (int i = 0; i < outList.size(); i++)
	{
		if (i != 0)
			std::cout << ",";
		std::cout << outList[i];
	}
	std::cout << "\n";
}

int main()
{
	std::vector<std::string> programInput = getLines("rules.txt");
	std::vector<std::string> registerInput = getLines("input.txt");

	std::unordered_map<char, long long> registers;
	registers['A'] = stoi(splitLineToString(registerInput[0], "Register A: ")[1]);
	registers['B'] = stoi(splitLineToString(registerInput[1], "Register B: ")[1]);
	registers['C'] = stoi(splitLineToString(registerInput[2], "Register C: ")[1]);
	registers['I'] = 0;
	std::vector<int> programList;
	programList = splitLineToInt(programInput[0], ',');

	/*
	Octal to Decimal -> 
	Manual calculation: we need 16 digits work from top to bottom
	start with 0 -> if result correct -> continue
	else: go down from 7 until result for digit is ok -> continue
	*/

	long long a16 = 5 * std::pow(8, 15); 
	long long a15 = 3 * std::pow(8, 14); 
	long long a14 = 2 * std::pow(8, 13);
	long long a13 = 2 * std::pow(8, 12); // ...
	long long a12 = 3 * std::pow(8, 11); // 8589934592
	long long a11 = 5 * std::pow(8, 10); // 1073741824
	long long a10 = 3 * std::pow(8, 9); // 134217728
	long long a9 = 7 * std::pow(8, 8); // 16777216
	long long a8 = 0 * std::pow(8, 7); // 2097152
	long long a7 = 1 * std::pow(8, 6); // 262144
	long long a6 = 2 * std::pow(8, 5); // 32768
	long long a5 = 3 * std::pow(8, 4); // 4096
	long long a4 = 6 * std::pow(8, 3); // 512
	long long a3 = 0 * std::pow(8, 2); // 64
	long long a2 = 1 * std::pow(8, 1); // 8
	long long a1 = 7 * std::pow(8, 0); // 1
	long long i = a16 + a15 + a14 + a13 + a12 + a11 + a10 + a9 + a8 + a7 + a6 + a5 + a4 + a3 + a2 + a1;

	preResults(17, 2024);
	std::cout << "Part 1: ";
	part1(programList, registers['A']);
	//std::cout << programInput[0] << "\n";
	std::cout << "Part 2: "; part1(programList, i);
	std::cout << "Part 2: " << i << std::endl;
	afterResults();
		
	return 0;
}