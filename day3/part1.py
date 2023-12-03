from typing import Callable, Optional

adjacent_checks = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1],
]


def has_adjacent_symbol(schematic: list[str], pos: tuple[int, int]) -> bool:

    for check in adjacent_checks:
        x = pos[0] + check[0]
        y = pos[1] + check[1]
        if 0 <= y < len(schematic) and 0 <= x < len(schematic[y]) \
                and not (schematic[y][x].isdigit() or schematic[y][x] == '\n' or schematic[y][x] == '.'):
            return True
    return False


def build_numbers_with_position(schematic: list[str]) -> list[int]:
    numbers: list[int] = []
    current_number: list[str] = []
    current_has_adjacent_symbol = False
    for y in range(len(schematic)):
        for x in range(len(schematic[y])):
            if schematic[y][x].isdigit():
                current_number.append(schematic[y][x])
                if has_adjacent_symbol(schematic, (x, y)) and not current_has_adjacent_symbol:
                    current_has_adjacent_symbol = True
            else:
                if current_number and current_has_adjacent_symbol:
                    number = int("".join(current_number))
                    numbers.append(number)
                current_number = []
                current_has_adjacent_symbol = False
    if current_number and current_has_adjacent_symbol:
        number = int("".join(current_number))
        numbers.append(number)
    return numbers


def sum_of_all_parts_numbers(schematic: list[str]) -> int:
    numbers = build_numbers_with_position(schematic)
    return sum(numbers)


# Example schematic
test_schematic = [
    "12.......*..",
    "+.........34",
    ".......-12..",
    "..78........",
    "..*....60..4",
    "78..........",
    ".......23...",
    "....90*12...",
    "............",
    "2.2......12.",
    ".*.........*",
    "1.1.......56"
]


def test_build_numbers_with_position():
    assert build_numbers_with_position(test_schematic) == [
        12, 34, 12, 78, 78, 23, 90, 12, 2, 2, 12, 1, 1, 56]


file = open('sample.txt', 'r')
lines = file.readlines()

# Calculating the sum
print(sum_of_all_parts_numbers(lines))
