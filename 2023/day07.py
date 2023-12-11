# Advent of Code - 2023
## Day 7

with open('puzzle_input', 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

NUMBER_TO_CARD_MAPPING = {14: 'A', 13: 'K', 12: 'Q', 11: 'J', 10: 'T',
          9: '9', 8: '8', 7: '7', 6: '6', 5: '5', 4: '4',
          3: '3', 2: '2'}
CARD_TO_NUMBER_MAPPING = {v: k for k, v in NUMBER_TO_CARD_MAPPING.items()}

def card_to_number(hand, part2=False):
    """
    Changes representation of string to a list of numbers
    (their card value) based on CARD_TO_NUMBER_MAPPING
    If part2 is True -> J is replaced with 1 instead of 11.
    :param hand: string of 5 characters 
    :param part2: boolean, whether or not part2 is considered
    :return: list of 5 integers 
    """
    new_hand = []
    for h in hand:
        if part2 and h == 'J':
            new_hand.append(1)
        else:
            new_hand.append(CARD_TO_NUMBER_MAPPING[h])
    return new_hand


def number_to_card(hand):
    """
    Changes representation of list of numbers to a string
    (their card value) based on NUMBER_TO_CARD_MAPPING
    :param hand: list of 5 integers
    :return: string of 5 characters
    """
    new_hand = []
    for h in hand: 
        if h == 1: 
            new_hand.append("J")
        else:
            new_hand.append(NUMBER_TO_CARD_MAPPING[h])
    new_hand = "".join(new_hand)
    return new_hand

def find_type(hand):
    """
    Determines what kind of hand was dealt. 
    Can be one of 7 types:
    high card < one pair < two pair < three of a kind
    < four of a kind < full house < five of a kind
    :param hand: iterator (either list or string)
    :return: integer
    """
    type = 0 # high card
    unique_cards = set(hand)
    amount_of_unique_cards = len(unique_cards)
    if amount_of_unique_cards == 1: 
        # all cards are the same
        type = 6 # five of a kind
    elif amount_of_unique_cards == 2: 
        # only two different cards: either full hand or four of a kind
        if hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
            type = 5 # four of a kind
        elif hand.count(hand[0]) == 2 or hand.count(hand[0]) == 3: 
            type = 4 # full house
    elif amount_of_unique_cards == 3: 
        # three different cards, either 3 of a kind or two pairs
        for letter in unique_cards: 
            if hand.count(letter) > 2:
                type = 3 # three of a kind
                break
        else:
            type = 2 # two pairs
    elif amount_of_unique_cards == 4: 
        type = 1 # one pair 
    return type


def find_best_J(hand):
    """
    Replace all Js in a hand with the best possible 
    card to get the best type.
    :param hand: string of 5 characters
    :return: integer (between 0 and 7, see find_type)
    """
    if "J" not in hand: 
        return find_type(hand)
    
    best_j = 0
    for i in range(2, 15):
        temporary_hand = hand.replace('J', NUMBER_TO_CARD_MAPPING[i])
        new_j = find_type(temporary_hand)
        if new_j > best_j:
            best_j = new_j
    return best_j


def get_hands_and_types(lines, part2=False):
    """
    Create two dictionaries with all hands and their bids,
    and all types and their hands.
    If part2 is true, J is treated as the best possible candidate,
    instead of being a J itself.
    :param lines: input - list of strings
    :param part2: boolean
    :return 2 dictionaries: {hand: bid}, {type: [hands]}
    """
    hands = {}
    types = {}
    for line in lines: 
        hand, bid = line.split(' ')
        sorted_hand = card_to_number(hand, part2=part2)
        if part2: 
            found_type = find_best_J(hand)
        else:
            found_type = find_type(sorted_hand)
        hands[hand] = int(bid)
        if not found_type in types: 
            types[found_type] = [sorted_hand] 
        else: 
            types[found_type].append(sorted_hand)
    return hands, types


def find_rank_and_add_up(hands, types):
    """
    Sort all hands in their type by their value.
    Iterate over all hands, assign a rank and calculate the result
    by multiplying the bid of each hand with their rank and adding it up.
    :param hands: dictionary {hand: bid}
    :param types: dictionary {type: [hands]}
    :return: integer
    """
    sorted_types = dict(sorted(types.items()))
    rank = 1
    result = 0
    for current_hands in sorted_types.values():
        for hand in sorted(current_hands):
            string_rep = number_to_card(hand)
            bid = hands[string_rep] 
            result += rank * bid
            rank += 1
    return result

hands, types = get_hands_and_types(lines)
part1 = find_rank_and_add_up(hands, types)
hands, types = get_hands_and_types(lines, part2=True)
part2 = find_rank_and_add_up(hands, types)

print("- -      -     -   *  -    -     -      -  *  *  - -   ")
print("*   -    .   .    .       *     .  .   .    *       -  ")
print(f"{'Advent of Code 2023 - Day 7':^55}")
print(".       .      *      -        -     *     .     .    .")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(f"Part 1: {part1:^55}")
print(f"Part 2: {part2:^55}")
print("    -      .    -  *    -    -    *    .  .  .    *   -")
print(".       .      *      -        -     *     .     .    .")