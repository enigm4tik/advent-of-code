# Advent of Code - 2025
## Day 8

with open('input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    lines = [[l for l in line] for line in lines]

## exkurs container ##
# container sind datenstrukturen in denen man andere daten ablegen kann

# listen initialisiert man mit der eckigen klammer. 
# die element können nur aufgrund ihrer position aufgerufen werden:
# zb. hunde_list = [2, 4, 1]
# print(hunde_list[2]) -> ergibt 1

# dictionaries haben einen schlüssel für jedes element
# man initialisiert sie mit der geschwungenen klammer
# zb. hunde_dict = {"klein": 2, "groß": 4, "mittel": 1}
# daraufhin kann man die elemente sehr leicht abrufen
# print(hunde_dict["mittel"]) -> ergibt 1

# in listen und dictionaries kann man elemente verändern: sie sind mutable (veränderbar)
# hunde_dict["mittel"] = 3 
# print(hunde_dict["mittel"]) -> ergibt 3
# hunde_list[2] = 3 
# print(hunde_list[2]) -> 3

# tupel werden mit runden klammern initialisiert.
# sie sind "immutable" container, das heißt man kann sie nicht mehr verändern: 
# position=(1,0)
# position[0] = 1 # ERROR TypeError: 'tuple' object does not support item assignment

# dictionaries brauchen als schlüssel (key) einen immutablen datentypen. 
# strings (zeichenketten ("abc")) sind auch immutabel, deshalb kann man sie gut als schlüssel verwenden.

# sets sind container, die auch mit runden klammern aber mit dem keyword "set" initialisiert werden und erlaubt nur 1 parameter 
# also man muss es so machen: set(list(1, 2, 3)) oder set([1, 2, 3]) NICHT set(1, 2, 3)
# sets können nur einzigartige einträge beinhalten und werden deshalb oft verwendet um duplikate zu löschen
# zahlen_liste = [1, 2, 3, 4, 1, 2, 3, 4, 2, 3, 5]
# print(len(zahlen_liste)) # ergibt 11
# zahlen_set = set(zahlen_liste)
# print(len(zahlen_set)) # ergibt 5

list_of_splitters=[] # leere liste aller splitter
starter=() # koordinaten unseres starters
for x in range(len(lines)): # wir loopen durch alle zeilen von 0 bis len(lines)
    for y in range(len(lines[0])): # wir loopen durch alle spalten von 0 bis len(lines[0])
        #len(lines) = die länge der liste lines, jede zeile ist ein eigenes element in der liste, deshalb ist die länge dieser liste, die anzahl der zeilen
        #len(lines[0]) = die länge des 1. elements in der liste, jedes zeichen ist ein eigenes element, deshalb ist die länge dieser liste, die anzahl der spalten
        if lines[x][y]=="^": # wenn das zeichen an koordinate (x,y) ^ ist
            list_of_splitters.append((x,y)) # kommt es in die liste der splitter
        if lines[x][y]=="S": # wenn wir unseren starter gefunden haben
            starter = (x,y) # speichere die koordinaten

splitdict={starter:1} # wir initiieren einen dictionary container: starter ist ein tupel (x, y) und der wert = 1
seen_splitters=set() # ein set für alle splits die wir treffen
for i in range(2,len(lines),2): # wir loopen mittels der funktion range(start, end, step) über alle zeilen (len(lines))
    # start = wo beginnen wir? der 1. splitter ist in zeile 2
    # end = wo enden wir? bei der letzten zeile: len(lines)
    # step = in welchen schritten gehen wir voran? da jede 2. zeile leer ist, ist unsere schrittgröße 2 
    for j in range(len(lines[0])): # wir loopen über alle zeichen in der zeile (len(lines[0]))
        me = (i, j) # me = meine position, tupel (i, j)
        up = (i-2,j) # up = die position über mir
        if up in splitdict: # wenn mein splitdict einen eintrag hat kommt von daher ein beam!
            if me in list_of_splitters: # wenn ich ein splitter bin
                seen_splitters.add(me) # gib mich in das set, wenn ich schon vorhanden bin, egal, weil sets keine duplikate erlauben
                left = (i,j-1) # ich splitte mich in links
                right = (i,j+1) # und rechts 
                if not left in splitdict: # wenn ich noch nicht vorhanden bin:
                    splitdict[left] = splitdict[up] # übernimm die anzahl der beams, bis hierher
                else: 
                    splitdict[left] += splitdict[up] # sonst addiere die anzahl der beams bis hierher
                if not right in splitdict:
                    splitdict[right] = splitdict[up] # das selbe gilt
                else:
                    splitdict[right] += splitdict[up] # auch für rehcts
            else: # wenn ich kein splitter bin, dann muss ich mich nicht splitten
                if not me in splitdict: # überprüfe ob ICH in splitdict existiere
                    splitdict[me] = splitdict[up] # wenn nein, dann übernehme für mich die beams bis hierher
                else: 
                    splitdict[me] += splitdict[up] # sonst, addiere es auf
        
        # wenn es keinen eintrag ÜBER MIR gibt, dann kommt auch kein beam von oben und das ist uninteressant

result=0
for key, val in splitdict.items(): # wir itterieren über alle schlüssel und ihre werte in splitdict
    if key[0] == len(lines)-2: # da unser schlüssel ein tupel ist und uns nur die letzte zeile interessiert 
        # unser key = (zeile, spalte) -> nehmen wir das 0. element und schauen ist es die letzte zeile? 
        # wieso -2? in die letzte zeile mit splittern ist 2 zeilen über dem ende
        result+=val # wir addieren die werte die in dieser zeile stehen 

print("Part 1: ", len(seen_splitters)) # Part 1: alle Splitter die wir gesehen haben
print("Part 2: ", result) # Part 2: alle Beams, die unten ankommen