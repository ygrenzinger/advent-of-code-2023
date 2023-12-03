def is_game_possible(game_data, bag_capacity):
    """
    Check if a game is possible given the bag's capacity.

    :param game_data: A list of tuples where each tuple represents a color and the number of cubes of that color.
    :param bag_capacity: A dictionary with the capacity of the bag for each color.
    :return: True if the game is possible, False otherwise.
    """
    for color, number in game_data:
        print(color, number)
        if number > bag_capacity[color]:
            return False
    return True


def possible_games_sum(games, bag_capacity):
    """
    Determine the sum of the IDs of games that are possible given the bag's capacity.

    :param games: A dictionary where keys are game IDs and values are lists of tuples (color, number).
    :param bag_capacity: A dictionary with the capacity of the bag for each color.
    :return: The sum of the IDs of the games that are possible.
    """
    return sum(game_id for game_id, game_data in games.items() if is_game_possible(game_data, bag_capacity))


bag_capacity = {"red": 12, "green": 13, "blue": 14}

# Transforming the games input to the specified format


def parse_game_data(game_str):
    """
    Parse a game string into a list of tuples representing the color and number of cubes.

    :param game_str: A string representing the subsets of cubes in a game.
    :return: A list of tuples where each tuple represents a color and the number of cubes of that color.
    """
    game_data = []
    subsets = game_str.replace("\n", "").split('; ')
    for subset in subsets:
        cubes = subset.split(', ')
        for cube in cubes:
            parts = cube.split(' ')
            if len(parts) == 2:
                number, color = int(parts[0]), parts[1]
                game_data.append((color, number))
    return game_data


file = open('part1.txt', 'r')
lines = file.readlines()

# Parsing the input
games = {}
for line in lines:
    parts = line.split(': ')
    game_id = int(parts[0].split(' ')[1])
    games[game_id] = parse_game_data(parts[1])

print(possible_games_sum(games, bag_capacity))
