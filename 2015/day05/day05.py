# Advent of Code - 2015
## Day 5

LIST_OF_BAD_WORDS = ['ab', 'cd', 'pq', 'xy']
LIST_OF_VOWELS = ['a', 'e', 'i', 'o', 'u']
    
class Word:
    """ Naughty or Nice word """
    
    def __init__(self, word) -> None:
        self.word = word
        self.naughty = self.determine_naughtiness()
        self.nice = self.determine_niceness()

    def remove_naughty_words(self):
        for bad_word in LIST_OF_BAD_WORDS:
            if bad_word in self.word:
                return True
        return False

    def remove_words_with_less_than_three_vowels(self):
        vowelcount = 0
        for nice_word in LIST_OF_VOWELS:
            vowelcount += self.word.count(nice_word)
            if vowelcount >= 3:
                return False
        return True

    def remove_words_without_double_letters(self):
        for i in range(len(self.word)):
            if i > 0:
                if self.word[i] == self.word[i-1]:
                    return False
        return True

    def separate(self):
        initial_dictionary = {}
        for index, letter in enumerate(self.word):
            if not index == 15:
                initial_dictionary[index] = letter + self.word[index+1]
        flipped_dictionary = {}
        for key, value in initial_dictionary.items():
            if value not in flipped_dictionary:
                flipped_dictionary[value] = [key]
            else:
                if flipped_dictionary[value][0]+1 == key:
                    flipped_dictionary[value].append(key)
                    continue
                else:  
                    return True
        return False

    def find_spaced_by_one(self):
        for index, letter in enumerate(self.word):
            if index >1 and letter == self.word[index-2]:
                return True
            else:
                continue
        return False

    def determine_naughtiness(self):
        naughty = self.remove_naughty_words()
        if not naughty:
            naughty = self.remove_words_with_less_than_three_vowels()
        if not naughty:
            naughty = self.remove_words_without_double_letters()
        return naughty

    def determine_niceness(self):
        nice = self.find_spaced_by_one()
        if nice: 
            nice = self.separate()
        return nice

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [Word(line.rstrip()) for line in lines]

nice_strings = [x for x in lines if not x.naughty]

print(f"Part 1: {len(nice_strings)}")

nice_strings_for_part2 = [x for x in lines if x.nice]

print(f"Part 2: {len(nice_strings_for_part2)}")
