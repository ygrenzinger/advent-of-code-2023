directions = {
    'N': (-1, 0),
    'S': (1, 0),
    'W': (0, -1),
    'E': (0, 1)
}


def find_start(grid):
    """Finds the starting position of the animal."""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                return (i, j)


def recursive_find_max_distance(grid, going_to, position, visited, distance):
    # print("\n")
    # print("position", position)
    # print("going_to", going_to)
    # print("distance", distance)
    y, x = position
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return 0
    cell = grid[y][x]
    # print("cell", cell)
    if cell == 'S':
        return distance
    if position in visited:
        return distance
    """
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

    distance += 1
    visited.add(position)
    if cell == '.':
        return distance
    elif cell == '|' and going_to == 'N':
        return recursive_find_max_distance(grid, 'N', (y-1, x), visited, distance)
    elif cell == '|' and going_to == 'S':
        return recursive_find_max_distance(grid, 'S', (y+1, x), visited, distance)

    elif cell == '-' and going_to == 'E':
        return recursive_find_max_distance(grid, 'E', (y, x+1), visited, distance)
    elif cell == '-' and going_to == 'W':
        return recursive_find_max_distance(grid, 'W', (y, x-1), visited, distance)

    elif cell == 'L' and going_to == 'S':
        return recursive_find_max_distance(grid, 'E', (y, x+1), visited, distance)
    elif cell == 'L' and going_to == 'W':
        return recursive_find_max_distance(grid, 'N', (y-1, x), visited, distance)

    elif cell == 'J' and going_to == 'S':
        return recursive_find_max_distance(grid, 'W', (y, x-1), visited, distance)
    elif cell == 'J' and going_to == 'E':
        return recursive_find_max_distance(grid, 'N', (y-1, x), visited, distance)

    elif cell == '7' and going_to == 'N':
        return recursive_find_max_distance(grid, 'W', (y, x-1), visited, distance)
    elif cell == '7' and going_to == 'E':
        return recursive_find_max_distance(grid, 'S', (y+1, x), visited, distance)

    elif cell == 'F' and going_to == 'N':
        return recursive_find_max_distance(grid, 'E', (y, x+1), visited, distance)
    elif cell == 'F' and going_to == 'W':
        return recursive_find_max_distance(grid, 'S', (y+1, x), visited, distance)

    return 0


def find_max_distance(grid):
    start_position = find_start(grid)
    print("start_position", start_position)
    visited = set()
    ds = [recursive_find_max_distance(
        grid, coming_from, (start_position[0] + dir[0], start_position[1] + dir[1]), visited, 1) for coming_from, dir in directions.items()]
    print("ds", ds)
    return max(ds) // 2


# Example grid
sample_grid_1 = [
    "7-F7-",
    ".FJ|7",
    "SJLL7",
    "|F--J",
    "LJ.LJ"
]

sample_grid_2 = [
    "7....",
    "LS-7.",
    ".|.|.",
    ".L-J.",
    "....."
]


file = open('sample.txt', 'r')
input = file.readlines()

# Apply the new approach to the grid
print(find_max_distance(input))
