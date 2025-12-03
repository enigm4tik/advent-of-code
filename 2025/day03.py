# Advent of Code - 2025
## Day 3

with open('input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def part1(list_of_strings):
    """
    Find the biggest 2-digit number in sequence
    for a list of strings made up of digits
    :param list_of_strings: list of strings of digits (eg. 123456789)
    :return: sum of biggest 2-digit numbers in sequence
    """
    result=0
    for str_num in list_of_strings:
        joltage=0
        for index, _ in enumerate(str_num):
            if index==len(str_num)-1:
                continue
            for i in range(1,len(str_num)-index):
                new_number = str_num[index]+str_num[index+i]
                new_number = int(new_number)
                if new_number > joltage:
                    joltage=new_number
        result+=joltage
    return result

def part2(list_of_strings):
    """
    Find the biggest 12-digit number in sequence
    for a list of strings made up of digits
    :param list_of_strings: list of strings of digits (eg. 123456789012)
    :return: sum of biggest 12-digit numbers in sequence
    """
    result=0
    for str_num in list_of_strings:
        joltage=""
        curr_len=12
        while curr_len:
            for i in range(9,0,-1): #find first biggest number
                found=str_num.find(str(i))
                if found!=-1:
                    if len(str_num)-found >= curr_len:
                        joltage+=str(i)
                        curr_len-=1
                        str_num=str_num[found+1:] #continue with shorter string
                        break
        result+=int(joltage)
    return result


print("Part 1: ", part1(lines))
print("Part 2: ", part2(lines))
