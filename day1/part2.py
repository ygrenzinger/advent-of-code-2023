from typing import Optional


def extract_number(word: str) -> Optional[int]:
    """Convert spelled-out number to digit."""
    number_map = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0
    }
    for key in number_map.keys():
        if word.startswith(key):
            return number_map[key]
    return None


def test_extract_number():
    assert extract_number('one') == 1
    assert extract_number('two') == 2
    assert extract_number('three') == 3
    assert extract_number('four') == 4
    assert extract_number('five') == 5
    assert extract_number('six') == 6
    assert extract_number('seven') == 7
    assert extract_number('eight') == 8
    assert extract_number('nine') == 9


def find_first(line: str) -> Optional[int]:
    for i in range(len(line)):
        if line[i].isdigit():
            return int(line[i])
        number = extract_number(line[i:])
        if number is not None:
            return number
    return None


def test_find_first():
    assert find_first('two1nine') == 2
    assert find_first('eightwothree') == 8
    assert find_first('abcone2threexyz') == 1
    assert find_first('xtwone3four') == 2
    assert find_first('4nineeightseven2') == 4
    assert find_first('zoneight234') == 1
    assert find_first('7pqrstsixteen') == 7


def find_last(line: str) -> Optional[int]:
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return int(line[i])
        number = extract_number(line[i:])
        if number is not None:
            return number
    return None


def test_find_last():
    assert find_last('two1nine') == 9
    assert find_last('eightwothree') == 3
    assert find_last('abcone2threexyz') == 3
    assert find_last('xtwone3four') == 4
    assert find_last('4nineeightseven2') == 2
    assert find_last('zoneight234') == 4
    assert find_last('7pqrstsixteen') == 6


def extract_calibration_value(s: str) -> Optional[int]:
    first_digit = find_first(s)
    last_digit = find_last(s)

    if first_digit is None or last_digit is None:
        return None

    return first_digit * 10 + last_digit


def sum_calibration_values(lines):
    total = 0
    for line in lines:
        value = extract_calibration_value(line)
        if value is not None:
            total += value
    return total


file = open('part2.txt', 'r')
lines = file.readlines()

result = sum_calibration_values(lines)
print(f"The total sum of calibration values is: {result}")


# Example usage
lines = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

print(sum_calibration_values(lines))
