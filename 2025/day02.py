with open('input', 'r') as file:
    lines = file.readlines()
    lines = lines[0].split(",")

small_prime_numbers=[2,3,5,7,11,13]

def part2(number):
    """
    Function to determine if number is made up of repeated sequences (at least twice)
    :param number: integer
    :return: 0 if not repeating
    :return: number if repeating 
    """
    numstr=str(number)
    length=len(numstr)
    if length==1: return 0
    for prime in small_prime_numbers:
        if length%prime == 0:
            other=length//prime 
            strings=[numstr[i:i+prime]for i in range(0,len(numstr),prime)]
            sets=set(strings)
            if len(sets)==1 and len(strings)!=1:
                return number
            strings=[numstr[i:i+other]for i in range(0,len(numstr),other)]
            sets=set(strings)
            if len(sets)==1 and len(strings)!=1:
                return number
    return 0

def checkForDouble(number):
    """
    Function to determine if number is made up of repeated sequence (exactly twice)
    :param number: integer
    :return: 0 if not repeating
    :return: number if repeating 
    """
    length = len(str(number))
    if (length%2) != 0:
        return 0
    numstr = str(number)
    halflength = len(str(number))//2
    a = numstr[:halflength]
    b = numstr[halflength:]
    if a==b:
        return number
    return 0

result=0
result2=0

for line in lines:
    start, end = line.split("-")
    for i in range(int(start),int(end)+1):
          result+=checkForDouble(i)
          result2+=part2(i)

print("Part 1: ", result)
print("Part 2: ", result2)