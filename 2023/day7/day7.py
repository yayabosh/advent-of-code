from collections import Counter
from functools import cmp_to_key

# Input is in the form of:
# Hand Bid
# 32T3K 765
with open("input.txt") as f:
    # We want to store each line as a tuple of (hand, bid)
    hands = []
    for line in f:
        hand, bid = line.split()
        hands.append((hand, int(bid)))

# Hand type constants
HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_OF_A_KIND = 3
FULL_HOUSE = 4
FOUR_OF_A_KIND = 5
FIVE_OF_A_KIND = 6


# Returns the type of hand as an integer (defined above)
def get_hand_type(hand: str) -> int:
    # Count the number of distinct cards in the hand
    card_counts = Counter(hand)
    num_distinct_cards = len(card_counts)

    match num_distinct_cards:
        # Check for five of a kind
        case 1:
            # Only one key means all cards are the same
            return FIVE_OF_A_KIND

        # Check for four of a kind or full house
        case 2:
            # If there's a Joker, we have one card repeated X times and a Joker
            # repeated 5 - X times. But the Joker can be any card, so we have
            # five of a kind
            if "J" in card_counts:
                return FIVE_OF_A_KIND

            # Only two keys means either one card is repeated 4 times and the other
            # is repeated once or one card is repeated 3 times and the other is
            # repeated twice
            elif 4 in card_counts.values():
                return FOUR_OF_A_KIND
            else:
                return FULL_HOUSE

        # Check for three of a kind or two pair
        case 3:
            # Three keys means either one card is repeated 3 times and the other
            # two are repeated once or two cards are repeated twice and the other
            # is repeated once
            if 3 in card_counts.values():
                # We have one card repeated 3 times, another card repeated once,
                # and a Joker repeated once. But the Joker can be any card,
                # so we have four of a kind
                if "J" in card_counts:
                    return FOUR_OF_A_KIND

                return THREE_OF_A_KIND
            else:
                # We have two cards repeated twice and once card repeated once.
                if "J" in card_counts:
                    # Case 1: Joker is the card repeated once. The Joker becomes
                    # one of the other two cards repeated twice, so we have a
                    # full house
                    if card_counts["J"] == 1:
                        return FULL_HOUSE
                    # Case 2: Joker is one of the cards repeated twice. The Joker
                    # becomes the card repeated twice, so we have a four of a kind
                    elif card_counts["J"] == 2:
                        return FOUR_OF_A_KIND

                return TWO_PAIR

        # Check for one pair
        case 4:
            # We have one card repeated twice and the other three are repeated once.
            if "J" in card_counts:
                # Case 1: Joker is one of the cards repeated once. The Joker becomes
                # the card repeated twice, so we have a three of a kind

                # Case 2: Joker is one of the cards repeated twice. The Joker becomes
                # a card repeated once, so we have a three of a kind

                # In either case, we have a three of a kind
                return THREE_OF_A_KIND

            # Four keys means one card is repeated twice and the other three are
            # repeated once
            return ONE_PAIR

        # Check for high card. This is the only case left
        case _:
            if "J" in card_counts:
                # We have a Joker and four distinct cards. The Joker can be any
                # card, so we have a one pair
                return ONE_PAIR

            return HIGH_CARD


# Now we have Jokers in Part Two.
# The "J" card represents a Joker and can be any card when determining the hand
# type, but for breaking ties within a hand type it is the lowest card.
CARD_STRENGTH = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


# Returns the higher hand of the two as an integer
# 1 if hand1 is higher, -1 if hand2 is lower, 0 if they are equal
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
rank = 1
for hand_type in hand_types:
    for hand, bid in hand_type:
        winnings = rank * bid
        total_winnings += winnings
        rank += 1

print(total_winnings)
