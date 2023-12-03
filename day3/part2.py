from typing import Callable, Optional

adjacent_checks = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1],
]


def find_adjacent_symbol(schematic: list[str], pos: tuple[int, int]) -> Optional[tuple[int, int]]:
    for check in adjacent_checks:
        x = pos[0] + check[0]
        y = pos[1] + check[1]
        if 0 <= y < len(schematic) and 0 <= x < len(schematic[y]) \
                and not (schematic[y][x].isdigit() or schematic[y][x] == '\n' or schematic[y][x] == '.'):
            return (x, y)
    return None


def build_numbers_with_position(schematic: list[str]) -> dict[tuple[int, int], int]:
    numbers: dict[tuple[int, int], list[int]] = {}
    current_number: list[str] = []
    current_has_adjacent_symbol = None
    for y in range(len(schematic)):
        for x in range(len(schematic[y])):
            if schematic[y][x].isdigit():
                current_number.append(schematic[y][x])
                adjacent_symbol = find_adjacent_symbol(schematic, (x, y))
                if adjacent_symbol != None and current_has_adjacent_symbol == None:
                    current_has_adjacent_symbol = adjacent_symbol
            else:
                if current_number and current_has_adjacent_symbol != None:
                    number = int("".join(current_number))
                    if current_has_adjacent_symbol in numbers:
                        numbers[current_has_adjacent_symbol].append(number)
                    else:
                        numbers[current_has_adjacent_symbol] = [number]
                current_number = []
                current_has_adjacent_symbol = None
    if current_number and current_has_adjacent_symbol != None:
        number = int("".join(current_number))
        numbers.append(number)
    return numbers


def value_of_number(schematic, number):
    pos, numbers = number
    c = schematic[pos[1]][pos[0]]
    if c == '*':
        if len(numbers) == 2:
            return numbers[0] * numbers[1]
    return 0


def sum_of_all_parts_numbers(schematic: list[str]) -> int:
    numbers = build_numbers_with_position(schematic)
    values = [value_of_number(schematic, item) for item in numbers.items()]
    return sum(values)


# Example schematic
test_schematic = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def test_build_numbers_with_position():
    assert sum_of_all_parts_numbers(test_schematic) == 467835


file = open('sample.txt', 'r')
lines = file.readlines()

# Calculating the sum
print(sum_of_all_parts_numbers(lines))
