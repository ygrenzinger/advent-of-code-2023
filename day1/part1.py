def extract_calibration_value(line):
    # Extract all digits from the line
    digits = [int(d) for d in line if d.isdigit()]

    # Return None if there are no digits in the line
    if not digits:
        return None

    # If only one digit is present, duplicate it
    if len(digits) == 1:
        return digits[0] * 11

    # Return the two-digit number formed by the first and last digit
    return digits[0] * 10 + digits[-1]


def sum_calibration_values(lines):
    total = 0
    for line in lines:
        value = extract_calibration_value(line)
        if value is not None:
            total += value
    return total


file = open('sample.txt', 'r')
lines = file.readlines()

result = sum_calibration_values(lines)
print(f"The total sum of calibration values is: {result}")
