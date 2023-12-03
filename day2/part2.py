from functools import reduce


def minimum_cubes_for_games(games):
    """
    Determine the minimum number of cubes of each color needed for each game.

    :param games: A dictionary where keys are game IDs and values are lists of tuples (color, number).
    :return: A dictionary where keys are game IDs and values are dictionaries with the minimum number of cubes for each color.
    """
    min_cubes_per_game = {}

    for game_id, game_data in games.items():
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}

        for color, number in game_data:
            min_cubes[color] = max(min_cubes[color], number)

        min_cubes_per_game[game_id] = min_cubes

    return min_cubes_per_game


def sum_of_minimum_cubes_powers(min_cubes_per_game: dict[str, dict[str, int]]) -> int:
    """
    Determine the sum of the powers of the minimum number of cubes for each game.

    :param min_cubes_per_game: A dictionary where keys are game IDs and values are dictionaries with the minimum number of cubes for each color.
    :return: The sum of the powers of the minimum number of cubes for each game.
    """
    return sum(reduce(lambda a, b: a * b, list(min_cubes.values())) for min_cubes in min_cubes_per_game.values())


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

print(sum_of_minimum_cubes_powers(minimum_cubes_for_games(games)))
