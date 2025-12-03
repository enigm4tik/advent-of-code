# Advent of Code - 2025
## Day 3

with open('input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def day03(list_of_strings, length):
    """
    Find the biggest number of <length> length in sequence
    for a list of strings made up of digits
    :param list_of_strings: list of strings of digits (eg. 123456789012)
    :return: sum of numbers of <length> length in sequence
    """
    result=0
    for str_num in list_of_strings:
        joltage=""
        curr_len=length
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


print("Part 1: ", day03(lines,2))
print("Part 2: ", day03(lines,12))
