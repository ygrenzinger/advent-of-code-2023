import re


def calculate_ways_to_win(duration, record):
    # Function to calculate the number of ways to win for a given race
    ways_to_win = 0
    for time_holding_button in range(duration):
        speed = time_holding_button
        distance_covered = speed * (duration - time_holding_button)
        if distance_covered > record:
            ways_to_win += 1
    return ways_to_win


def total_ways_to_win_all_races(races):
    # Function to calculate the total ways to win across all races
    total_ways = 1
    for duration, record in races:
        ways_to_win = calculate_ways_to_win(duration, record)
        total_ways *= ways_to_win
    return total_ways


def parse_input(lines):
    times = re.findall(r"\d+", lines[0])
    distances = re.findall(r"\d+", lines[1])
    return [(int(time), int(distance)) for time, distance in zip(times, distances)]


sample_races = [
    "Time:      7  15   30",
    "Distance:  9  40  200"
]

# Example races
races = [
    "Time:        41     66     72     66",
    "Distance:   244   1047   1228   1040"
]

parsed_races = parse_input(sample_races)
print(parsed_races)

# Calculate total ways to win all races
result = total_ways_to_win_all_races(parsed_races)
print(f"Total ways to win all races: {result}")
