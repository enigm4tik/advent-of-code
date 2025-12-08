# Advent of Code - 2025
## Day 5

with open('input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

ranges=[]
ids=[]
add_id=False
for element in lines:
    if element=="": 
        add_id = True
        continue
    if add_id==True: 
        ids.append(int(element))
    else: 
        ranges.append(element)

count=0
for number in ids: 
    for range in ranges: 
        left, right = range.split("-")
        left = int(left)
        right = int(right)
        if number >= left and number <= right: 
            count += 1
            break

# Part 2
part2ranges=[]
for range in ranges: 
    for range in ranges: 
        left, right = range.split("-")
        left = int(left)
        right = int(right)
    part2ranges.append((left, right))

part2ranges = sorted(part2ranges, key=lambda x: x[0]) # sorted ranges by left value

endranges = []
while part2ranges: 
    range=part2ranges[0]
    left, right = range
    del part2ranges[0]
    if not endranges:
        endranges.append(range)
        continue
    new_range=endranges[-1]
    left2, right2 = new_range
    if (left>=left2 and left<=right2) and (right>=left2 and right<=right2):
        continue
    elif (left>=left2 and left<=right2) and (right>right2):
        if not (right2+1,right) in endranges:
            endranges.append((right2+1,right))
    elif left>right2:
        if not(left,right) in endranges:
            endranges.append((left,right))
    else: 
        if right > right2: 
            if not (right2+1, right) in endranges:
                endranges.append((right2+1, right))
    endranges = sorted(endranges, key=lambda x: x[0])

ergebnis=0
for range in endranges: 
    ergebnis += (range[1]+1-range[0])

print("Part 1: ", count)
print("Part 2: ", ergebnis)