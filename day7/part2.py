from collections import Counter
import functools

card_ranks = {
    'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14
}


def parse_hand(hand_string):
    """Parses the hand string and returns the hand and the bid."""
    parts = hand_string.split()
    return parts[0], int(parts[1])


def hand_rank(hand):
    counts = Counter(hand)
    number_of_jacks = counts['J']
    if number_of_jacks == 5:
        return 7
    del counts['J']
    sorted_counts = sorted(
        counts.values(), reverse=True
    )
    sorted_counts[0] = sorted_counts[0] + number_of_jacks

    if sorted_counts == [5]:
        return 7
    elif sorted_counts == [4, 1]:
        return 6
    elif sorted_counts == [3, 2]:
        return 5
    elif sorted_counts == [3, 1, 1]:
        return 4
    elif sorted_counts == [2, 2, 1]:
        return 3
    elif sorted_counts == [2, 1, 1, 1]:
        return 2
    else:
        return 1


def compare_hands(hand1, hand2):
    rank1 = hand1[0]
    rank2 = hand2[0]
    diff = rank1 - rank2
    if rank1 < rank2:
        return -1
    elif rank1 > rank2:
        return 1
    else:
        for card1, card2 in zip(hand1[1], hand2[1]):
            diff = card_ranks[card1] - card_ranks[card2]
            if diff != 0:
                return diff


def calculate_winnings(hands):
    parsed_hands = [parse_hand(hand) for hand in hands]
    ranked_hands = [
        (hand_rank(hand[0]), hand[0], hand[1]) for hand in parsed_hands
    ]
    sorted_hands = sorted(
        ranked_hands, key=functools.cmp_to_key(compare_hands))

    total_winnings = 0
    for rank, hand in enumerate(sorted_hands, 1):
        total_winnings += rank * hand[2]

    return total_winnings


# Example input
sample_input = [
    "32T3K 765",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
    "T55J5 684"
]

file = open('sample.txt', 'r')
input = file.readlines()

print(calculate_winnings(input))
