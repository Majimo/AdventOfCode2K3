from collections import Counter

cards_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cards_order_part2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

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

def get_highest_card(hand):
    return cards_order_part2[min([cards_order_part2.index(card) for card in hand])]

def classify_hand(line):
    hand = line.strip().split(' ')[0]
    bid = line.strip().split(' ')[1]
    hand_for_counting = hand

    if 'J' in hand:
        counts = Counter(hand)
        card_to_duplicate = [card for card, count in counts.items() if count >= 2 and card != 'J']
        if card_to_duplicate:    
            hand = hand.replace('J', card_to_duplicate[0])
        else:
            hand = hand.replace('J', get_highest_card(hand))
    
    if is_five_of_a_kind(hand):
        return {hand_for_counting: [9, bid]}
    elif is_four_of_a_kind(hand):
        return {hand_for_counting: [8, bid]}
    elif is_full_house(hand):
        return {hand_for_counting: [7, bid]}
    elif is_three_of_a_kind(hand):
        return {hand_for_counting: [6, bid]}
    elif count_pairs(hand) == 2:
        return {hand_for_counting: [5, bid]}
    elif count_pairs(hand) == 1:
        return {hand_for_counting: [4, bid]}
    
    return {hand_for_counting: [3, bid]}

def sort_key_p1(hand):
    key, value = next(iter(hand.items()))
    return (-value[0], [cards_order_part2.index(card) for card in key])

# with open("input.txt") as f:
#     lines = [line.strip() for line in f.readlines()]
#     all_hands = [classify_hand(line) for line in lines]
#     sorted_hands = sorted(all_hands, key=sort_key_p1, reverse=True)
#     sorted_hands_with_bid = [{k: v[1]} for hand in sorted_hands for k, v in hand.items()]

#     total_sum = 0
#     for index, item in enumerate(sorted_hands_with_bid):
#         value = list(item.values())[0]
#         total_sum += int(value) * (index + 1)
    
#     print('PART 1 :', total_sum)

with open("input2.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    all_hands = [classify_hand(line) for line in lines]
    sorted_hands = sorted(all_hands, key=sort_key_p1, reverse=True)
    sorted_hands_with_bid = [{k: v[1]} for hand in sorted_hands for k, v in hand.items()]

    total_sum = 0
    for index, item in enumerate(sorted_hands_with_bid):
        value = list(item.values())[0]
        total_sum += int(value) * (index + 1)
    
    print('PART 2 :', total_sum)

# 246851429 too low