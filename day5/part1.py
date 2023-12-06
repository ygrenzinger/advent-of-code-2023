

def parse_input(input_text):
    # Split the input into sections
    sections = input_text.split('\n\n')

    # Extract seed numbers
    seeds_section = sections[0]
    seed_numbers = [int(num) for num in seeds_section.split(': ')[1].split()]

    # Function to parse map sections
    def parse_map_section(section):
        lines = section.split('\n')[1:]  # Skip the title line
        return [tuple(map(int, line.split())) for line in lines]

    # Parse each map section
    mappings = [parse_map_section(section) for section in sections[1:]]

    return seed_numbers, mappings


def source_to_destination(number, mapping):
    for mapping in mapping:
        destination, source, number_range = mapping
        if number in range(source, source + number_range):
            return number + (destination - source)
    return number


def seed_to_location(seed, mappings):
    current = seed
    for mapping in mappings:
        current = source_to_destination(current, mapping)
    return current


def find_location_number(seed_numbers, mappings):
    locations = [seed_to_location(seed, mappings) for seed in seed_numbers]
    print(locations)
    return min(locations)


sample_input = """
seeds: 79 14 55 13

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


file = open('sample.txt', 'r')
input = file.read()


# Parse the input
seed_numbers, mappings = parse_input(input)

# The seed_numbers list and mapping_data list are now ready to be used in the algorithm
print("Seed Numbers:", seed_numbers)
print("Mapping Data:", mappings)

# Find the lowest location number
lowest_location = find_location_number(seed_numbers, mappings)
print(lowest_location)
