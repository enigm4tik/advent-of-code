# Advent of Code - 2020
## Day 4 - Part 1

with open('day04_test', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

class Passport(object):
    ecl = None
    pid = None 
    eyr = None
    hcl = None 
    byr = None 
    iyr = None
    cid = None 
    hgt = None 

    def __init__(self, **entries):
        self.__dict__.update(entries)

def create_passport(passport_info_lists):
    blub = {}
    for info_container in passport_info_lists:
        for info in info_container:
            info_type, value = info.split(':')
            blub[info_type] = value
    passport = Passport(**blub)
    return passport

passport_info = []
passports = []
for line in lines: 
    if line == '':
        blub = create_passport(passport_info)
        passport_info = []
        passports.append(blub)
    else: 
        part = line.split(' ')
        passport_info.append(part)
    
blub = create_passport(passport_info)
passports.append(blub)

def passport_has_required_fields(passport):
    required_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    has_all_required_attribues = True
    for required_field in required_fields:
        if not getattr(passport, required_field):
            has_all_required_attribues = False
    return has_all_required_attribues

valid_passports = 0
for passport in passports:
    if passport_has_required_fields(passport):
        valid_passports += 1

print(f"Part 1 - Result: {valid_passports}")