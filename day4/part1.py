def calculate_points(winning_numbers, your_numbers):
    # Find the intersection of winning numbers and your numbers
    matches = set(winning_numbers) & set(your_numbers)

    # Calculate points based on the number of matches
    # If there are matches, the points are 2^(number of matches - 1)
    # If no matches, the card is worth 0 points
    return 2 ** (len(matches) - 1) if matches else 0


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


def total_points(input):
    cards = parse_cards(input)
    # Initialize total points
    total = 0

    # Iterate over each card
    for card in cards:
        # Add the points from each card to the total
        total += calculate_points(card["winning"], card["numbers"])

    return total


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
print(total_points(input))
