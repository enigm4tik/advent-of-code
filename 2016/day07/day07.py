# Advent of Code - 2016
## Day 7
import re

with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]


def is_this_abba(code):
    if code[0] == code[3] and code[1] == code[2] and not code[0] == code[1]:
        return True
    else:
        return False


def is_this_aba(code):
    if code[0] == code[2] and not code[0] == code[1]:
        return True
    else:
        return False


def split_into_characters_with_frame_shift(code, length=4):
    frameshifted_code = code[1:]
    code3 = code[2:]
    code4 = []
    if length == 4:
        code4 = code[3:]

    list_of_frameshifted_codes = []
    frameshifted_codes = [code, frameshifted_code, code3, code4]
    for frameshifted_code in frameshifted_codes:
        while len(frameshifted_code) > length-1:
            list_of_frameshifted_codes.append(frameshifted_code[0:length])
            frameshifted_code = frameshifted_code[length:]
        list_of_frameshifted_codes.append(frameshifted_code)

    finished = []
    for letter_code in list_of_frameshifted_codes:
        if letter_code and len(letter_code) == length:
            finished.append(letter_code)
    return finished


def get_outside_code(code, hypernet_sequences):
    for hypernet_sequence in hypernet_sequences:
        code = code.replace('[' + hypernet_sequence + ']', '#')
    code = code.split('#')
    return code


def get_hypernet_sequence(code):
    list_of_hypernet_sequences = re.findall(r'(?<=\[)[^]]+(?=\])', code)
    return list_of_hypernet_sequences


def determine_abba_for_list_of_strings(code_list):
    for code in code_list:
        all_codes = split_into_characters_with_frame_shift(code, 4)
        for frameshifted_code in all_codes:
            if is_this_abba(frameshifted_code):
                return True
    return False


def determine_valid_tls_ip(ip_adress):
    hypernet_sequences = get_hypernet_sequence(ip_adress)
    remaining_ip = get_outside_code(ip_adress, hypernet_sequences)
    if not determine_abba_for_list_of_strings(hypernet_sequences) and determine_abba_for_list_of_strings(remaining_ip):
        return 1
    else:
        return 0
    

def determine_aba_for_list_of_strings(list_of_codes):
    aba_codes = []
    for code in list_of_codes:
        all_codes = split_into_characters_with_frame_shift(code, 3)
        for frameshifted_code in all_codes:
            if is_this_aba(frameshifted_code):
                aba_codes.append(frameshifted_code)
    return aba_codes


def compare_aba_and_bab(abas, babs):
    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        if bab in babs:
            return True
    return False


def determine_valid_ssl_ip(ip_adress):
    hypernet_sequences = get_hypernet_sequence(ip_adress)
    remaining_ip = get_outside_code(ip_adress, hypernet_sequences)
    list_of_hypernet_abas = determine_aba_for_list_of_strings(hypernet_sequences)
    list_of_remaining_ip_abas = determine_aba_for_list_of_strings(remaining_ip)
    if compare_aba_and_bab(list_of_hypernet_abas, list_of_remaining_ip_abas):
        return 1
    else:
        return 0

valid_tls_ip_adresses = 0
valid_ssl_ip_adresses = 0
for line in lines: 
    valid_tls_ip_adresses += determine_valid_tls_ip(line)
    valid_ssl_ip_adresses += determine_valid_ssl_ip(line) 

print(f"Part 1: {valid_tls_ip_adresses}")
print(f"Part 2: {valid_ssl_ip_adresses}")
