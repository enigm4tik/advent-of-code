with open('input', 'r') as file:
    lines = file.readlines()
    lines = lines[0].split(",")

def part2(number):
    numstr=str(number)
    length=len(numstr)
    if length==1: return 0
    if length==9:
        if (numstr[0:3]==numstr[3:6]) and (numstr[3:6]==numstr[6:9]):
            return number
    if length==6:
        if (numstr[0:2]==numstr[2:4]) and (numstr[2:4]==numstr[4:6]):
            return number
    if length==10:
        if (numstr[0:2]==numstr[2:4]) and (numstr[4:6]==numstr[6:8]) and (numstr[0:2]==numstr[8:10]) and (numstr[4:6]==numstr[0:2]):
            return number
    for index, letter in enumerate(numstr):
        if index==length-1:
            continue
        if letter != numstr[index+1]:
            return 0
    return number

def checkForDouble(number, part1=True):
    length = len(str(number))
    if (length%2) != 0:
        if part1: return 0
        else:
            return part2(number)
    if (length==6 or length==10) and part1==False: 
        if part2(number)!=0:
            return number
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
          result+=checkForDouble(i, True)
          result2+=checkForDouble(i, False)

print("Part 1: ", result)
print("Part 2: ", result2)