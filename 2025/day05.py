with open('input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

ranges=[]
ids=[]
idhinzufuegen=False
for element in lines:
    if element=="": 
        idhinzufuegen = True
        continue
    if idhinzufuegen==True: 
        ids.append(int(element))
    else: 
        ranges.append(element)

count=0
for zahl in ids: 
    for bereich in ranges: 
        links, rechts = bereich.split("-")
        links = int(links)
        rechts = int(rechts)
        if zahl >= links and zahl <=rechts: 
            count+=1
            break
print("Part 1: ", count)
#Part 2:
part2ranges=[]
for bereich in ranges: 
    links, rechts=bereich.split("-")
    links = int(links)
    rechts = int(rechts)
    part2ranges.append((links, rechts))

part2ranges = sorted(part2ranges, key=lambda x: x[0])

endranges = []
while part2ranges: 
    bereich=part2ranges[0]
    links, rechts = bereich
    del part2ranges[0]
    if not endranges:
        endranges.append(bereich)
        continue
    new_range=endranges[-1]
    links2, rechts2 = new_range
    if (links>=links2 and links<=rechts2) and (rechts>=links2 and rechts<=rechts2):
        continue
    elif (links>=links2 and links<=rechts2) and (rechts>rechts2):
        if not (rechts2+1,rechts) in endranges:
            endranges.append((rechts2+1,rechts))
    elif links>rechts2:
        if not(links,rechts) in endranges:
            endranges.append((links,rechts))
    else: 
        if rechts > rechts2: 
            if not (rechts2+1, rechts) in endranges:
                endranges.append((rechts2+1, rechts))
    endranges = sorted(endranges, key=lambda x: x[0])

ergebnis=0
for tupel in endranges: 
    ergebnis += (tupel[1]+1-tupel[0])
print("Part 2: ", ergebnis)