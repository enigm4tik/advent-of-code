# Advent of Code - 2025
## Day 6

with open('input', 'r') as file:
    lines = file.readlines()
    lines_part2 = lines[:]
    lines = [line.rstrip().split(" ") for line in lines]
    lines = [[value for value in line if value]for line in lines]

rows = len(lines)
cols = len(lines[0])

def get_result():
    part1=0
    for i in range(cols):
        numbers=[]
        for j in range(rows):
            number=lines[j][i]
            numbers.append(number)
        if numbers[-1] == "*":
            result=1
            for number in numbers:
                if number=="*":
                    continue
                number=int(number)
                result*=number
        if numbers[-1] == "+":
            result=0
            for number in numbers:
                if number=="+":
                    continue 
                number = int(number)
                result+=number
        part1+=result
    return part1

part1 = get_result()

# Part 2

def get_next_operand(start):
    plus = lines_part2[-1].find("+", start)
    mul = lines_part2[-1].find("*",start)
    if plus < 0 and mul < 0: 
        return ("E",len(lines_part2[0]))
    if plus < 0:
        return ("*", mul)
    if mul < 0: 
        return ("+", plus)
    if plus < mul: 
        return ("+", plus)
    if plus > mul: 
        return ("*", mul)
    
def switch_numbers(list_of_numbers):
    switched=[[] for _ in range(len(list_of_numbers[0]))]
    for i in range(len(list_of_numbers[0])):
        for j in range(len(list_of_numbers)):
            switched[i].append(numbers[j][-1-i])
    switched=[int("".join(number)) for number in switched]
    return switched

old_operand,start = get_next_operand(0)
new_operand,end = get_next_operand(1)
part2=0
while old_operand[0] != "E":
    numbers = []
    for i in range(rows-1):
        numbers.append(lines_part2[i][start:end-1])
    numbers = switch_numbers(numbers)
    if old_operand == "*":
        result=1
        for number in numbers: 
            result*=number 
    if old_operand == "+":
        result=0
        for number in numbers:
            result+=number
    part2+=result
    old_operand,start=new_operand,end
    new_operand,end=get_next_operand(start+1)

print("Part 1: ", part1)
print("Part 2: ", part2)
