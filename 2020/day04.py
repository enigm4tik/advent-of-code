# Advent of Code - 2020
## Day 4 - Part 1
import re

with open('puzzle_input', 'r') as file:
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
    has_all_required_fields = False
    all_values_meet_criteria = True

    def __init__(self, **entries):
        self.__dict__.update(entries)
        self.has_all_required_fields = self.passport_has_required_fields()
        self.all_values_meet_criteria = self.passport_is_valid()

    def passport_has_required_fields(self):
        required_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
        has_all_required_attribues = True
        for required_field in required_fields:
            if not getattr(self, required_field):
                # print(f"missing field: {required_field}")
                has_all_required_attribues = False
                break
        return has_all_required_attribues

    def value_is_long_enough(self, passport_value, length):
        return len(passport_value) == length

    def value_in_range(self, passport_value, start, stop):
        return int(passport_value) >= start and int(passport_value) <= stop

    def year_value_is_valid(self, named_attribute, length, year_start, year_stop):
        passport_value = getattr(self, named_attribute)
        if not self.value_is_long_enough(passport_value, length):
            # print(f"{named_attribute}: {passport_value}, {length}")
            return False
        if not self.value_in_range(passport_value, year_start, year_stop):
            # print(f"{named_attribute}: {passport_value}, {year_start}, {year_stop}")
            return False
        return True

    def height_is_valid(self):
        passport_value = getattr(self, 'hgt')
        if not passport_value.endswith('in') and not passport_value.endswith('cm'):
            return False
        if passport_value.endswith('in'):
            height, nothing = passport_value.split('in')
            if not self.value_in_range(int(height), 59, 76):
                return False
        if passport_value.endswith('cm'):
            height, nothing = passport_value.split('cm')
            if not self.value_in_range(int(height), 150, 193):
                return False
        return True
    
    def hair_is_valid(self):
        hair_pattern = '^#(?:[0-9a-fA-F]{3}){1,2}$'
        passport_value = getattr(self, 'hcl')
        if not self.value_is_long_enough(passport_value, 7):
            return False
        result = re.match(hair_pattern, passport_value)
        if not result: 
            return False
        return True
    
    def eye_color_is_valid(self):
        passport_value = getattr(self, 'ecl')
        valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        # print(f"{passport_value} should be {valid_eye_colors}")
        if passport_value in valid_eye_colors:
            return True
        return False
    
    def pid_is_valid(self):
        digit_pattern = '[0-9]{9}$'
        passport_value = getattr(self, 'pid')
        if not self.value_is_long_enough(passport_value, 9):
            return False
        result = re.match(digit_pattern, passport_value)
        if not result:
            return False
        return True
        
    def passport_is_valid(self):
        if not self.has_all_required_fields:
            return False
        if not self.year_value_is_valid('byr', 4, 1920, 2002):
            return False
        if not self.year_value_is_valid('iyr', 4, 2010, 2020):
            return False
        if not self.year_value_is_valid('eyr', 4, 2020, 2030):
            return False
        if not self.height_is_valid():
            return False
        if not self.hair_is_valid():
            return False
        if not self.eye_color_is_valid():
            return False
        if not self.pid_is_valid():
            return False
        return True


def create_passport(passport_info_lists):
    passport_info_dict = {}
    for info_container in passport_info_lists:
        for info in info_container:
            info_type, value = info.split(':')
            passport_info_dict[info_type] = value
    passport = Passport(**passport_info_dict)
    return passport

passport_info = []
passports = []
for line in lines: 
    if line == '':
        passport_info_list = create_passport(passport_info)
        passport_info = []
        passports.append(passport_info_list)
    else: 
        part = line.split(' ')
        passport_info.append(part)
    
passport_info_list = create_passport(passport_info)
passports.append(passport_info_list)

valid_passports = 0
valid_passport_list = []
for passport in passports:
    if passport.has_all_required_fields:
        valid_passports += 1
        valid_passport_list.append(passport)

print(f"Part 1 - Result: {valid_passports}")

valid_passports = 0
for passport in passports: 
    if passport.all_values_meet_criteria:
        valid_passports += 1

print(f"Part 2 - Result: {valid_passports}")