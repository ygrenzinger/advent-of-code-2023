

def parse_input(input_text):
    # Split the input into sections
    sections = input_text.split('\n\n')

    # Extract seed numbers
    seeds_section = sections[0]
    seed_numbers = [int(num) for num in seeds_section.split(': ')[1].split()]
    seed_ranges = [
        (seed_numbers[i], seed_numbers[i] + (seed_numbers[i+1] - 1)) for i in range(0, len(seed_numbers), 2)
    ]

    # Function to parse map sections
    def parse_map_section(section):
        lines = section.split('\n')[1:]  # Skip the title line
        return [tuple(map(int, line.split())) for line in lines]

    # Parse each map section
    mappings = [parse_map_section(section) for section in sections[1:]]

    return seed_ranges, mappings


sample_input = """
seeds: 82 1

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


# file = open('sample.txt', 'r')
# input = file.read()


# Parse the input
seed_ranges, mappings = parse_input(sample_input)

# The seed_numbers list and mapping_data list are now ready to be used in the algorithm
print("Seed ranges:", seed_ranges)
print("Mappings data:", mappings)


def process_mapping(range_input, range_mapping):
    start, end = range_input
    destination, source, source_range = range_mapping
    shift = (destination - source)
    if start >= source and end < source + source_range:
        return (start + shift, end + shift)
    if end <= source:
        return (end + shift, end + shift)
    if start >= source + source_range:
        return (start + shift, start + shift)
    if start < source:
        return (source + shift, source + (source_range - 1) + shift)
    if end > source + source_range:
        return (start + shift, source + (source_range - 1) + shift)


def process_mappings(range_input, mappings):
    start, _ = range_input
    if mappings == []:
        return start
    else:
        result = []
        for range_mapping in mappings[0]:
            r = process_mapping(range_input, range_mapping)
            result.append(process_mappings(r, mappings[1:]))
        return min(result)


lowest_values = [process_mappings(r, mappings) for r in seed_ranges]

print("lowest values", lowest_values)


# Find the lowest location number
# lowest_location = find_location_number(seed_numbers, mappings)
# print(lowest_location)
