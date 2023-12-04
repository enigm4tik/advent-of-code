# Advent of Code - 2015
## Day 4
import hashlib

# stringtohash = "abcdef"
# stringtohash = "pqrstuv"
stringtohash = "yzbqklnj" # len = 8

i = 0
part1_satisfied = False
while True:
    string_i = str(i)
    stringtohash += string_i
    result = hashlib.md5(stringtohash.encode())
    hex_result = result.hexdigest()
    stringtohash = stringtohash[:-len(string_i)]
    if hex_result.startswith('00000') and not part1_satisfied:
        print(f"Part 1 - Result: {i}")
        part1_satisfied = True
        continue
    if hex_result.startswith('000000'):
        print(f"Part 2 - Result: {i}")
        break
    i += 1

