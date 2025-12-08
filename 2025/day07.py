#day 07

with open('input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    lines = [[l for l in line] for line in lines]
# print(lines)

list_of_splitters=[] # leere liste aller splitter
starter=() # koordinaten unseres starters
for x in range(len(lines)): 
    for y in range(len(lines[0])): 
        if lines[x][y]=="^": # wenn das zeichen an koordinate (x,y) ^ ist
            list_of_splitters.append((x,y)) # kommt es in die liste der splitter
        if lines[x][y]=="S": # wenn wir unseren starter gefunden haben
            starter = (x,y) # speichere die koordinaten

def move_down(position): 
    new_position=(position[0]+2,position[1]) # bewegt den beam um 1 zeile nach unten
    return new_position

list_of_beams=[starter] # hier kommen alle beams rein, die wir uns anschauen wollen
looked_at=[] # hier sind alle beams drinnen die wir schonmal gesehen haben 
splits = [] # hier sind alle splits drinnen, die getroffen wurden

while list_of_beams: # solange noch ein beam zum anschauen drinnen ist mache:
    beam=list_of_beams[0] # unser beam ist der 1. in der liste
    # print(beam)
    looked_at.append(beam) # wir haben ihn angeschaut
    new_beam = move_down(beam) # wir gehen eine zeile runten
    if new_beam[0] >=(len(lines)) or new_beam[1] <=0 or new_beam[1] >= len(lines[0]):
        # wenn wir am linken, rechten oder unteren rand sind:
        del list_of_beams[0] # lösche den beam, da gehts nicht weiter
        continue
    if new_beam in list_of_splitters: # wenn der neue beam auf einen splitter trifft
        if new_beam not in splits: # und der splitter noch nicht in unseren splits ist
            splits.append(new_beam) # füge ihn hinzu
        left = (new_beam[0],new_beam[1]-1) # spalte den splitter in links 
        right = (new_beam[0],new_beam[1]+1) # und rechts 
        if not left in list_of_beams and left not in looked_at: # wenn er noch nicht in unserer liste zum anschauen ist
            list_of_beams.append((new_beam[0],new_beam[1]-1)) # füge ihn hinzu
        if not right in list_of_beams and right not in looked_at: # gilt genauso 
            list_of_beams.append((new_beam[0],new_beam[1]+1)) # für rechts 
        del list_of_beams[0] # und entferne den beam den wir uns gerade angeschaut haben
    else: # wenn der neue beam NICHT auf einen splitter trifft
        list_of_beams[0]=new_beam # entferne den beam aus der liste zum anschauen
        looked_at.append(new_beam)
        list_of_beams.append(new_beam)
    list_of_beams = sorted(list_of_beams,key=lambda x:(x[0],x[1]))

print("Part 1: ", len(splits)) # wir wollen nur wissen wieviele es sind, nicht welche genau es sind
# len = länge der liste splits

list_of_beams=[starter] # hier kommen alle beams rein, die wir uns anschauen wollen
looked_at=[] # hier sind alle beams drinnen die wir schonmal gesehen haben 
splits = [] # hier sind alle splits drinnen, die getroffen wurden

splitdict = {split:0 for split in list_of_splitters}
# print(splitdict)

def move_down(position): 
    new_position=(position[0]+2,position[1]) # bewegt den beam um 1 zeile nach unten
    return new_position

while list_of_beams: 
    beam=list_of_beams[0] 
    new_beam = move_down(beam)
    if new_beam[0] >(len(lines)) or new_beam[1] <0 or new_beam[1] > len(lines[0]):
        del list_of_beams[0]
        continue
    if new_beam in list_of_splitters:
        splitdict[new_beam] += 1
        left = (new_beam[0],new_beam[1]-1)
        right = (new_beam[0],new_beam[1]+1)
        list_of_beams.append((new_beam[0],new_beam[1]-1)) # füge ihn hinzu
        list_of_beams.append((new_beam[0],new_beam[1]+1)) # für rechts 
        del list_of_beams[0] # und entferne den beam den wir uns gerade angeschaut haben
    else: # wenn der neue beam NICHT auf einen splitter trifft
        if new_beam not in splitdict:
            splitdict[new_beam] = 1
        else:
            splitdict[new_beam] += 1
        # list_of_beams[0]=new_beam # entferne den beam aus der liste zum anschauen
        del list_of_beams[0]
        list_of_beams.append(new_beam)
    # print(splitdict)

print(splitdict)

xx = {i: 0 for i in range(0,18,2)}
for i in range(16):
    for key in splitdict.keys():
        if key[0] == i:
            xx[i] += splitdict[key]
print(xx)