# Advent of Code - 2015
## Day 7

def string_is_integer(n):
    """
    Determine if a string representation is an integer
    :param n: string
    :return: boolean
    """
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
    
def determine_wire_value(wires_to_check, assignments):
    """
    Determine the value of each wire in a huge list of wires.
    The wires are connected by bitwise operations based on other values.
    :param wires_to_check: list of strings
    :param assignments: dictionary {wire: operation}
    """
    available_wires = {}
    while wires_to_check:
        current_wire = wires_to_check.pop(0)
        operation = assignments[current_wire]

        if "AND" in operation:
            if (string_is_integer(operation[0])) and operation[2] in available_wires:
                calculation = int(operation[0]) & available_wires[operation[2]]
                available_wires[current_wire] = calculation
            elif operation[0] in available_wires and operation[2] in available_wires:
                calculation = available_wires[operation[0]] & available_wires[operation[2]]
                available_wires[current_wire] = calculation
            else: 
                wires_to_check.append(current_wire)
                continue
        
        elif "OR" in operation:
            if (operation[0] in available_wires and operation[2] in available_wires):
                calculation = available_wires[operation[0]] | available_wires[operation[2]]
                available_wires[current_wire] = calculation
            else: 
                wires_to_check.append(current_wire)
                continue

        elif "NOT" in operation: 
            if operation[1] in available_wires:
                calculation = 65536 + (~ available_wires[operation[1]])
                available_wires[current_wire] = calculation
            else: 
                wires_to_check.append(current_wire)
                continue

        elif "RSHIFT" in operation: 
            if operation[0] in available_wires:
                calculation = available_wires[operation[0]] >> int(operation[2])
                available_wires[current_wire] = calculation
            else: 
                wires_to_check.append(current_wire)
                continue

        elif "LSHIFT" in operation: 
            if operation[0] in available_wires:
                calculation = available_wires[operation[0]] << int(operation[2])
                available_wires[current_wire] = calculation
            else: 
                wires_to_check.append(current_wire)
                continue
        else: 
            if operation[0] in available_wires:
                calculation = available_wires[operation[0]]
                available_wires[current_wire] = calculation
            elif string_is_integer(operation[0]):
                calculation = int(operation[0])
                available_wires[current_wire] = calculation
            else:
                wires_to_check.append(current_wire)
                continue

    return available_wires["a"]

with open('puzzle_input', 'r') as file: 
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

assignments = {}
for line in lines: 
    operation, assignment = line.split(" -> ")
    operation = operation.split(' ')
    if not assignment in assignments:
        assignments[assignment] = operation


wires_to_check = list(assignments.keys())
part1 = determine_wire_value(wires_to_check, assignments)
print(part1)

assignments['b'] = [str(part1)]
wires_to_check = list(assignments.keys())
part2 = determine_wire_value(wires_to_check, assignments)
print(part2)
