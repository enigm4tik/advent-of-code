##

with open('input', 'r') as file:
    lines = file.readlines()
    lines2 = lines[:]
    # print(lines)
    # lines1=[lines.rstrip() for line in lines]
    lines = [line.rstrip().split(" ") for line in lines] #.split(" ")
    # print(lines)
    lines = [[value for value in line if value]for line in lines]

# print(lines)

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
            ergebnis=1
            for zahl in numbers:
                if zahl=="*":
                    continue
                zahl=int(zahl)
                ergebnis*=zahl
        if numbers[-1] == "+":
            ergebnis=0
            for zahl in numbers:
                if zahl=="+":
                    continue 
                zahl = int(zahl)
                ergebnis+=zahl
        # print(numbers, ergebnis)
        part1+=ergebnis
    print(part1)
    return part1

get_result()

#part 2
# 1) wo ist der nächste operand
# 2) von altem operand bis neuer operand -1 = zahl
# 3) letztes, vorletztes, ...., element von jedem "string"
# 4) int über jede zahl 
# 5) den operand durchführen */+
# 6) aufaddieren von allen ergebnissen

def get_next_operand(start):
    plus = lines2[-1].find("+", start)
    mal = lines2[-1].find("*",start)
    if plus < 0 and mal < 0: 
        return ("E",len(lines2[0]))
    if plus < 0:
        return ("*", mal)
    if mal < 0: 
        return ("+", plus)
    if plus < mal: 
        return ("+", plus)
    if plus > mal: 
        return ("*", mal)
    
def switch_numbers(list_of_numbers):
    switched=[[] for i in range(len(list_of_numbers[0]))]
    # print(list_of_numbers)
    # print(switched)
    # "123", " 45", "  6"
    # "356", "24 ", "1  "
    # 123
    #  45
    #   6
    # print(one[-1], two[-1], three[-1])
# print(one[-2], two[-2], three[-2])
# print(one[-3], two[-3], three[-3])
    print(numbers)
    for i in range(len(list_of_numbers[0])):
        for j in range(len(list_of_numbers)):
            print(switched, i, j)
            switched[i].append(numbers[j][-1-i])
    switched=[int("".join(number)) for number in switched]
    return switched

# print(get_next_operand(0))
# print(get_next_operand(13))

old_operand,start = get_next_operand(0)
new_operand,end = get_next_operand(1)
part2=0
while old_operand[0] != "E":
    # print(old_operand, start)
    # print(new_operand,end)
    numbers = []
    for i in range(rows-1):
        numbers.append(lines2[i][start:end-1])
    numbers = switch_numbers(numbers)
    # print("Switched:", numbers)
    if old_operand == "*":
        ergebnis=1
        for zahl in numbers: 
            ergebnis*=zahl 
    if old_operand == "+":
        ergebnis=0
        for zahl in numbers:
            ergebnis+=zahl
    # print(ergebnis)
    part2+=ergebnis
    old_operand,start=new_operand,end
    new_operand,end=get_next_operand(start+1)
    # print("Nachher")
    # print(old_operand, start)
    # print(new_operand,end)
    # print("====")
    
print(part2)

# print("=====")
# print("lines: ", lines2)
# print(lines2[-1])
# print(lines2[-1].find("+")) # 4
# print(lines2[-1].find("*")) # 0

# one = lines2[0][0:3] 
# two = lines2[1][0:3]
# three = lines2[2][0:3]
# four = lines2[3][0:3]
# print(one, two, three, four)

# print(one[-1], two[-1], three[-1])
# print(one[-2], two[-2], three[-2])
# print(one[-3], two[-3], three[-3])

# print("".join([one[-1], two[-1], three[-1]]))
# print("".join([one[-2], two[-2], three[-2]]))
# print("".join([one[-3], two[-3], three[-3]]))

# print(int("".join([one[-1], two[-1], three[-1]])))
# print(int("".join([one[-2], two[-2], three[-2]])))
# print(int("".join([one[-3], two[-3], three[-3]])))

# print(int("".join([one[-1], two[-1], three[-1]])) * int("".join([one[-2], two[-2], three[-2]])) * int("".join([one[-3], two[-3], three[-3]])))