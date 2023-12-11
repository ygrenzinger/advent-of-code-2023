neighbours = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
]


def is_out_of_bounds(grid, pos):
    x, y = pos
    if y < 0 or y >= len(grid):
        return True
    if x < 0 or x >= len(grid[y]):
        return True
    return False


def fill(grid, visited, pos):
    for neighbour in neighbours:
        x, y = pos
        dx, dy = neighbour
        if is_out_of_bounds(grid, (x + dx, y + dy)):
            visited[pos] = 'outside'
            return
        if (x + dx, y + dy) in visited:
            continue
        visited.add((x + dx, y + dy))
        if grid[y + dy][x + dx] == '.':
            fill(grid, visited, (x + dx, y + dy))


def find_enclosing_nest(grid):
    visited = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x, y) in visited:
                continue
