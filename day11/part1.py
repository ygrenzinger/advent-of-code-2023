from itertools import combinations


def get_galaxy_postions(space_map):
    galaxy_positions = []
    for y, line in enumerate(space_map):
        for x, symbol in enumerate(line):
            if symbol == '#':
                galaxy_positions.append((x, y))

    return galaxy_positions


def get_expanded_galaxies(matrix, galaxies):
    # Empty rows
    empty_rows_indexs = [i for i, row in enumerate(matrix) if all(
        element == "." for element in row)]

    # Empty cols
    empty_cols_indexs = []
    for col in range(len(matrix[0])):
        column_elements = [matrix[row][col] for row in range(len(matrix))]
        if all(element == "." for element in column_elements):
            empty_cols_indexs.append(col)

    extended_galaxies = set()

    for galaxy in galaxies:
        x, y = galaxy

        nx = len([index for index in empty_cols_indexs if index < x])
        x += (1_000_000 - 1) * nx

        ny = len([index for index in empty_rows_indexs if index < y])
        y += (1_000_000 - 1) * ny

        extended_galaxies.add((x, y))

    return extended_galaxies


def compute_manhattan_distance(galaxy1, galaxy2):
    x1, y1 = galaxy1
    x2, y2 = galaxy2
    return abs(x2 - x1) + abs(y2 - y1)


# Input data
sample_input = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#....."
]


with open("sample.txt", 'r') as f:
    file = f.read()
lines = file.split('\n')
image = [list(word) for word in lines]
galaxy_positions = get_galaxy_postions(image)
expanded_galaxies = get_expanded_galaxies(image, galaxy_positions)
galaxies_pairs = list(combinations(expanded_galaxies, 2))
sum_distances = sum(
    [compute_manhattan_distance(g1, g2) for g1, g2 in galaxies_pairs]
)
print(sum_distances)
