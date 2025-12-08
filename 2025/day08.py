# Advent of Code - 2025
## Day 8

from math import sqrt,pow

with open('input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# Globals to create names for my objects
ITERATOR = 0
NAMEITERATOR = 0

class Junction:
    x = 0
    y = 0
    z = 0
    smallest_distance=999999999
    order={}

    def __init__(self,descriptor):
        self.x, self.y, self.z = [int(coordinate) for coordinate in descriptor.split(",")]
        global NAMEITERATOR
        NAMEITERATOR +=1
        self.name=NAMEITERATOR

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"

    def calculate_distance(self, other):
        distance_squared = pow((self.x-other.x),2)+pow((self.y-other.y),2)+pow((self.z-other.z),2)
        distance = sqrt(distance_squared)
        return distance 
    
    def sort_partners(self, others):
        for other in others:
            if other != self:
                calculated_distance = self.calculate_distance(other)
                self.order[other,self] = calculated_distance

class Circuit:
    members=[]
    smallest_distance=999999999999999
    closest_connection=-1
    name=""
    def __init__(self,junction):
        global ITERATOR
        ITERATOR +=1
        self.name = ITERATOR
        self.members=[junction]
    
    def add_junction(self,junction):
        self.members.append(junction)

    def merge_circuits(self, other):
        for junction in other.members:
            if junction not in self.members: 
                self.add_junction(junction)
        self.smallest_distance = 9999999999999
        
    def contains(self,junction):
        return junction in self.members
    
    def get_size(self):
        return len(self.members)
    
    def __repr__(self):
        return f"<Name: {self.name}, Members: {self.members}>"
    
    def __str__(self):
        return self.name

all_circuits=[]
all_junctions=[]
for line in lines: 
    new_junction = Junction(line)
    new_circuit = Circuit(new_junction)
    all_junctions.append(new_junction)
    all_circuits.append(new_circuit)

all_orders={}
for junction in all_junctions:
    junction.sort_partners(all_junctions)
    if not all_orders:
        all_orders = junction.order
    else: 
        all_orders.update(junction.order)

sorted_junctions = dict(sorted(all_orders.items(), key=lambda item: item[1]))

connected = 0
for index, element in enumerate(sorted_junctions.keys()):
    lengths=[circuit.get_size() for circuit in all_circuits]
    lengths = sorted(lengths)
    if connected==1000:
        part1 = lengths[-1]*lengths[-2]*lengths[-3]
    if index %2==0:
        continue
    left, right = element
    for circuit in all_circuits: 
        if circuit.contains(left):
            left_circuit = circuit
        if circuit.contains(right):
            right_circuit = circuit
    if left_circuit==right_circuit:
        connected+=1
        continue
    left_circuit.merge_circuits(right_circuit)
    all_circuits.remove(right_circuit)
    if len([circuit.get_size() for circuit in all_circuits]) == 1:
        part2=left.x*right.x
        break
    connected+=1

print("Part 1: ", part1)
print("Part 2: ", part2)