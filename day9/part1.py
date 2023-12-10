def calculate_next_value(history):
    """Calculates the next value of a given history sequence using the difference method."""
    # Create a list of lists to hold the sequences of differences
    sequences = [history]

    # Generate sequences of differences until all values in the last sequence are zero
    while sequences[-1].count(sequences[-1][0]) != len(sequences[-1]):
        new_sequence = [sequences[-1][i+1] - sequences[-1][i]
                        for i in range(len(sequences[-1])-1)]
        sequences.append(new_sequence)

    # Calculate the next value by working backwards from the zero sequence
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i+1][-1])

    return sequences[0][-1]


# Example histories
sample_histories = [
    [0, 3, 6, 9, 12, 15],
    [1, 3, 6, 10, 15, 21],
    [10, 13, 16, 21, 30, 45]
]


file = open('sample.txt', 'r')
input = file.readlines()

histories = [
    [int(number) for number in line.replace('\n', '').split(' ')] for line in input
]

# Calculate the next values and their sum
next_values = [calculate_next_value(history) for history in histories]
total_sum = sum(next_values)
print(f"Next values: {next_values}")
print(f"Sum: {total_sum}")
