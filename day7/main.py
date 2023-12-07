from collections import Counter

cards_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def is_five_of_a_kind(hand):
    return len(set(hand)) == 1

def is_four_of_a_kind(hand):
    counts = {card: hand.count(card) for card in set(hand)}
    return 4 in counts.values()

def is_full_house(hand):
    counts = {card: hand.count(card) for card in set(hand)}
    return 3 in counts.values() and 2 in counts.values()

def is_three_of_a_kind(hand):
    counts = {card: hand.count(card) for card in set(hand)}
    return 3 in counts.values()

def count_pairs(hand):
    counts = Counter(hand)
    pairs = [card for card, count in counts.items() if count == 2]
    return len(pairs)

def classify_hand(line):
    hand = line.strip().split(' ')[0]
    bid = line.strip().split(' ')[1]
    print('hand:', hand)
    
    if is_five_of_a_kind(hand):
        return {hand: [9, bid]}
    elif is_four_of_a_kind(hand):
        return {hand: [8, bid]}
    elif is_full_house(hand):
        return {hand: [7, bid]}
    elif is_three_of_a_kind(hand):
        return {hand: [6, bid]}
    elif count_pairs(hand) == 2:
        return {hand: [5, bid]}
    elif count_pairs(hand) == 1:
        return {hand: [4, bid]}
    
    return {hand: [3, bid]}

def sort_key(hand):
    key, value = next(iter(hand.items()))
    return (-value[0], [cards_order.index(card) for card in key])

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    all_hands = [classify_hand(line) for line in lines]
    sorted_hands = sorted(all_hands, key=sort_key, reverse=True)
    print('sorted_hands:', sorted_hands)
    result = [{k: v[1]} for hand in sorted_hands for k, v in hand.items()]
    print('result:', result)
    
    print('PART 1 :')