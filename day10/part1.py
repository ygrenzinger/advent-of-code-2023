from collections import deque


STARTING_POINT = "S"


def find_starting_point(lines):
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            if character == STARTING_POINT:
                return x, y

    assert False, "No starting point found."


cell_to_direction_mappings = {
    "|": ["n", "s"],
    "-": ["w", "e"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
    STARTING_POINT: ["n", "s", "w", "e"],
}

directions_mapping = {
    "n": (0, -1),
    "s": (0, 1),
    "w": (-1, 0),
    "e": (1, 0),
}


def cell_to_connection(cell):
    if cell not in cell_to_direction_mappings:
        return None
    return [directions_mapping[pd] for pd in cell_to_direction_mappings[cell]]


def retrieve_cell(pos, grid):
    x, y = pos
    if y < 0 or y >= len(grid):
        return None
    if x < 0 or x >= len(grid[y]):
        return None
    cell = grid[y][x]
    if cell == '.':
        return None
    return cell


def build_connections(starting_point, grid):
    connections = {
        (starting_point): [],
    }
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            moves = []
            if cell not in cell_to_direction_mappings:
                continue

            possible_directions = cell_to_connection(cell)
            moves = [(pd[0] + x, pd[1] + y) for pd in possible_directions]

            for move in moves:
                if starting_point == move:
                    connections[starting_point].append((x, y))

            if starting_point != (x, y):
                connections[(x, y)] = moves
    return connections


def max_distance(grid):
    starting_point = find_starting_point(grid)
    connections = build_connections(starting_point, grid)

    dist = {(starting_point): 0}
    queue = deque([starting_point])
    while queue:
        current = queue.popleft()
        for con in connections[current]:
            if con not in dist:
                dist[con] = dist[current] + 1
                queue.append(con)
    print(dist)
    return max(dist.values())


# Example grid
sample_grid_1 = [
    "7-F7-",
    ".FJ|7",
    "SJLL7",
    "|F--J",
    "LJ.LJ"
]

sample_grid_2 = [
    ".....",
    ".S-7.",
    ".|.|.",
    ".L-J.",
    "....."
]


file = open('sample.txt', 'r')
input = file.readlines()

# Apply the new approach to the grid
print(max_distance(sample_grid_2))
