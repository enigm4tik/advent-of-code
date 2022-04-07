# Advent of Code - 2016
## Day 4

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]


def get_room_id(code):
    room_id = code.split('[')[0]
    room_id = room_id.split('-')[-1]
    return int(room_id)


def get_letter_string(code):
    letter_string = code.split('-')[:-1]
    letter_string = '-'.join(letter_string)
    return letter_string


def get_checksum(code):
    checksum = code.split('[')[1]
    checksum = checksum.split(']')[0]
    return checksum


def get_most_used_letters(code):
    list_of_used_letters = []
    amount_of_letters = {}
    letters = code.split('-')[:-1]
    for word in letters:
        for letter in word:
            if not letter in list_of_used_letters:
                list_of_used_letters.append(letter)
                amount_of_letters[letter] = 1
            else:
                amount_of_letters[letter] += 1
    return amount_of_letters, list_of_used_letters

  
def create_checksum(code):
    amount_of_letters, list_of_used_letters = get_most_used_letters(code)
    sorted_dictionary = dict(sorted(amount_of_letters.items(), key=lambda item: item[1]))
    most_used = list(set(sorted_dictionary.values()))
    most_used.reverse()
    sorted_most_used = []
    for i in most_used:
        list_of_used_letters = [k for k,v in sorted_dictionary.items() if v == i]
        for element in sorted(list_of_used_letters):
            sorted_most_used.append(element)
    return(''.join(sorted_most_used[:5]))


def compare_checksums(code):
    provided_checksum = get_checksum(code)
    calculated_checksum = create_checksum(code)
    if provided_checksum == calculated_checksum:
        return True
    else:
        return False

list_of_correct_room_numbers = []
list_of_correct_codes = []

for line in lines:
    if compare_checksums(line):
        list_of_correct_room_numbers.append(get_room_id(line))
        list_of_correct_codes.append(line)

print(f"Part 1: {sum(list_of_correct_room_numbers)}")

# Part 2

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def move_character_by_room_id(character, room_id):
    initial_id = alphabet.index(character)
    move_by = room_id % 26
    resulting_id = initial_id + move_by
    if resulting_id >= 26:
        resulting_id = resulting_id - 26
    return alphabet[resulting_id]

deciphered_rooms = {}
for code in list_of_correct_codes:
    resulting_code = ''
    room_id = get_room_id(code)
    letter_string = get_letter_string(code)
    for character in letter_string:
        if not character == '-':
            resulting_code += move_character_by_room_id(character, room_id)
        else:
            resulting_code += character
    deciphered_rooms[resulting_code] = room_id

print(f"Part 2: {deciphered_rooms['northpole-object-storage']}")
