#day8

from math import sqrt,pow

with open('input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

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
    
    def get_coordinates(self):
        return (self.x, self.y, self.z)

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

    def calculate_distance_between_circuits(self,other):
        for junction in self.members:
            # print("Junction: ", junction)
            for junction2 in other.members:
                # print("Junction 2: ", junction2)
                calculated_distance = junction.calculate_distance(junction2)
                # print("Calculated Distance: ", calculated_distance)
                if calculated_distance < self.smallest_distance:
                    self.smallest_distance = calculated_distance
                    self.closest_connection = other
        # print("Smallest Distance: ", self.smallest_distance)
        # print("=========")

    def merge_circuits(self, other):
        print("Merging: ", self.name, " with ", other.name)
        # print(self.members, " with ", other.members)
        for junction in other.members:
            if junction not in self.members: 
                self.members.append(junction)
        self.smallest_distance = 9999999999999
        
    def contains(self,junction):
        return junction in self.members
    
    def get_size(self):
        return len(self.members)
    
    def __repr__(self):
        return f"<Name: {self.name}, Members: {self.members}>"#, Best Distance: {self.smallest_distance}, Partner: {self.closest_connection.name}>"
    
    def __str__(self):
        return self.name


all_circuits=[]
all_junctions=[]
for line in lines: 
    new_junction = Junction(line)
    new_circuit = Circuit(new_junction)
    all_junctions.append(new_junction)
    aaa = all_junctions[:]
    all_circuits.append(new_circuit)

def calculate_all_distances(list_of_circuits):
    for circuit in list_of_circuits:
        for circuit2 in list_of_circuits:
            if circuit2 != circuit:
                circuit.calculate_distance_between_circuits(circuit2)
    sorted_circuits=sorted(list_of_circuits, key=lambda x: x.smallest_distance)
    return sorted_circuits

def update_circuits(list_of_circuits, one, other):
    for circuit in list_of_circuits:
        if circuit.closest_connection == other:
            circuit.calculate_distance_between_circuits(one)
        if circuit != one:
            one.calculate_distance_between_circuits(circuit)
    sorted_circuits=sorted(list_of_circuits, key=lambda x: x.smallest_distance)
    # print(sorted_circuits)
    return sorted_circuits

# connections = 10 # 10 for example
# all_circuits=calculate_all_distances(all_circuits)
# print(all_circuits)
# while connections > 1:
#     circuit1 = all_circuits[0]
#     circuit1.merge_circuits(circuit1.closest_connection)
#     for circuit in all_circuits:
#         if circuit.name==circuit1.closest_connection.name:
#             all_circuits.remove(circuit)
#     all_circuits = calculate_all_distances(all_circuits)
#     connections-=1
#     lengths=[circuit.get_size() for circuit in all_circuits]
#     lengths = sorted(lengths)
#     print(lengths)
 
# lengths=[circuit.get_size() for circuit in all_circuits]
# lengths = sorted(lengths)
# print(lengths)
# part1 = lengths[-1]*lengths[-2]*lengths[-3]
# print("Part 1: ", part1)

all_orders={}
for junction in all_junctions:
    junction.sort_partners(all_junctions)
    if not all_orders:
        all_orders = junction.order
    else: 
        all_orders.update(junction.order)

# aaa = all_junctions[:]
print(aaa)
sorted_junctions = dict(sorted(all_orders.items(), key=lambda item: item[1]))

# all_circuits = calculate_all_distances(all_circuits)
connected = 0
for index, element in enumerate(sorted_junctions.keys()):
    lengths=[circuit.get_size() for circuit in all_circuits]
    lengths = sorted(lengths)
    if connected==1000:
        part1 = lengths[-1]*lengths[-2]*lengths[-3]
        print("Part 1: ", part1)
    if index %2==0:
        continue
    left, right = element
    left_circuit=""
    right_circuit=""
    for circuit in all_circuits: 
        if circuit.contains(left):
            left_circuit = circuit
        if circuit.contains(right):
            right_circuit = circuit
    if left_circuit==right_circuit:
        connected+=1
        continue
    # print("Merging based off: ", left, right)
    left_circuit.merge_circuits(right_circuit)
    all_circuits.remove(right_circuit)
    # print(all_circuits)
    if len([circuit.get_size() for circuit in all_circuits]) == 1:
        print("Part 2: ", left.x*right.x)
        break
    connected+=1
