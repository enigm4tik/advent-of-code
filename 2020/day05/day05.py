# Advent of Code - 2020
## Day 5 - Part 1

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def binary_to_decimal(binary_string):
    return int(binary_string, 2)

def decimal_to_binary(decimal_number, seat=False):
    if seat: 
        return str(format(decimal_number, "03b"))
    else:
        return str(format(decimal_number, "07b"))

max_result = 0
for line in lines: 
    row = line[0:7].replace('F', '0').replace('B', '1')
    seat = line[7:10].replace('L', '0').replace('R', '1')
    dec_row = binary_to_decimal(row) 
    dec_seat = binary_to_decimal(seat)
    seat_id = dec_row*8 + dec_seat
    if seat_id > max_result:
        max_result = seat_id
    else:
        continue

print(f"Part 1 - Result: {max_result}")

## Day 5 - Part 2

def create_all_seats():
    all_seats = []
    for i in range(5, 110): # these numbers were chosen by trial and error :D
        for j in range(8):
            row = decimal_to_binary(i).replace('0', 'F').replace('1', 'B')
            seat = decimal_to_binary(j, True).replace('0', 'L').replace('1', 'R')
            result = row + seat
            all_seats.append(result)
    return all_seats

all_seats = create_all_seats()

result_list = list(set(all_seats).difference(lines))

for line in result_list:
    row = line[0:7].replace('F', '0').replace('B', '1')
    seat = line[7:10].replace('L', '0').replace('R', '1')
    dec_row = binary_to_decimal(row) 
    dec_seat = binary_to_decimal(seat)
    seat_id = dec_row*8 + dec_seat

print(f"Part 2 - Result: {seat_id}")