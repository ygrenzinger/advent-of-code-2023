def count_matches(winning_numbers, your_numbers):
    """Count the number of matching numbers."""
    return len(set(winning_numbers) & set(your_numbers))


def process_scratchcards(cards):
    total_cards = len(cards)  # Start with the original number of cards
    card_copies = [0] * len(cards)  # Track the number of copies for each card

    # Process each original card
    for i, card in enumerate(cards):
        matches = count_matches(card["winning"], card["numbers"])
        # For each match, add a copy of each subsequent card
        for j in range(1, matches + 1):
            if i + j < len(cards):
                card_copies[i + j] += 1

    # Process the copies
    for i, copies in enumerate(card_copies):
        while copies > 0:
            matches = count_matches(cards[i]["winning"], cards[i]["numbers"])
            total_cards += 1  # Add the processed copy
            copies -= 1  # Reduce the number of copies to process

            # Add new copies based on this copy's matches
            for j in range(1, matches + 1):
                if i + j < len(cards):
                    card_copies[i + j] += 1

    return total_cards


def parse_cards(raw_text):
    cards = []

    # Split the text into lines, each line representing a card
    lines = raw_text.strip().split('\n')

    for line in lines:
        _, line = line.split(':')
        # Split each line at the '|' character
        winning, numbers = line.split('|')

        # Convert the number strings to integers
        winning_numbers = [int(n) for n in winning.split()]
        your_numbers = [int(n) for n in numbers.split()]

        # Add the card to the list
        cards.append({"winning": winning_numbers, "numbers": your_numbers})

    return cards


def total_scratchcards(input):
    cards = parse_cards(input)
    return process_scratchcards(cards)


# Example scratchcards data
sample_input = raw_text = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

file = open('sample.txt', 'r')
input = file.read()

# Calculate the total points
print(total_scratchcards(input))
