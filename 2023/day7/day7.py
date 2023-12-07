from collections import defaultdict
from functools import cmp_to_key

# Part One
# Input is in the form of:
# Hand Bid
# 32T3K 765
with open("input.txt") as f:
    # We want to store each line as a tuple of (hand, bid)
    hands = []
    for line in f:
        hand, bid = line.split()
        hands.append((hand, int(bid)))

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


# Returns a dictionary of the counts of each card in the hand
def get_card_counts(hand: str) -> dict:
    card_counts = defaultdict(int)
    for card in hand:
        card_counts[card] += 1

    return card_counts


# Returns the type of hand as an integer (defined above)
def get_hand_type(hand: str) -> int:
    card_counts = get_card_counts(hand)
    num_distinct_cards = len(card_counts)

    match num_distinct_cards:
        # Check for five of a kind
        case 1:
            # Only one key means all cards are the same
            return FIVE_OF_A_KIND

        # Check for four of a kind or full house
        case 2:
            # Only two keys means either one card is repeated 4 times and the other
            # is repeated once or one card is repeated 3 times and the other is
            # repeated twice
            if 4 in card_counts.values():
                return FOUR_OF_A_KIND
            else:
                return FULL_HOUSE

        # Check for three of a kind or two pair
        case 3:
            # Three keys means either one card is repeated 3 times and the other
            # two are repeated once or two cards are repeated twice and the other
            # is repeated once
            if 3 in card_counts.values():
                return THREE_OF_A_KIND
            else:
                return TWO_PAIR

        # Check for one pair
        case 4:
            # Four keys means one card is repeated twice and the other three are
            # repeated once
            return ONE_PAIR

        # Check for high card. This is the only case left
        case _:
            return HIGH_CARD


CARD_STRENGTH = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


# Returns the higher hand of the two as an integer
# 1 if hand1 is higher, -1 if hand2 is higher, 0 if they are equal
def compare_hands(hand_bid_1: str, hand_bid_2: str) -> int:
    hand1, bid1 = hand_bid_1
    hand2, bid2 = hand_bid_2

    cards1 = [CARD_STRENGTH[card] for card in hand1]
    cards2 = [CARD_STRENGTH[card] for card in hand2]

    for card1, card2 in zip(cards1, cards2):
        if card1 > card2:
            return 1
        elif card2 > card1:
            return -1

    return 0


# Will contain a list of hands for each hand type (defined above)
hand_types = [[] for _ in range(7)]
# Sort each hand into its hand type
for hand, bid in hands:
    hand_type = get_hand_type(hand)
    hand_types[hand_type].append((hand, bid))

# Sort each hand type by rank in descending order
for hand_type in hand_types:
    hand_type.sort(key=cmp_to_key(compare_hands))

total_winnings = 0
i = 1
for hand_type in hand_types:
    for hand, bid in hand_type:
        rank = i
        winnings = rank * bid
        total_winnings += winnings
        i += 1

print(total_winnings)
