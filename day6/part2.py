def calculate_ways_to_win(duration, record):
    """
    Calculate the number of ways to win the race.

    Args:
    duration (int): The duration of the race in milliseconds.
    record (int): The record distance to beat in millimeters.

    Returns:
    int: The number of ways to beat the record.
    """
    ways_to_win = 0
    for time_holding_button in range(duration):
        speed = time_holding_button
        distance_covered = speed * (duration - time_holding_button)
        if distance_covered > record:
            ways_to_win += 1
    return ways_to_win


# Race details: duration and record
duration = 71530  # duration of the race in milliseconds
record = 940200  # record distance to beat in millimeters

# Calculate the number of ways to win
ways_to_win = calculate_ways_to_win(duration, record)
print(f"Number of ways to win the race: {ways_to_win}")

# Calculate the number of ways to win
ways_to_win = calculate_ways_to_win(41667266, 244104712281040)
print(f"Number of ways to win the race: {ways_to_win}")
