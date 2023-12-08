def parse_input(input_string):
    lines = input_string.split('\n')  # Split the input into lines

    # Extract the instructions (assumed to be the first line)
    instructions = lines[0]

    # Initialize a dictionary for the network
    network = {}

    # Process each line to build the network
    for line in lines[1:]:
        if line.strip() == '':  # Skip empty lines
            continue

        # Split the node and its connections
        node, connections = line.split('=')
        node = node.strip()
        left, right = connections.strip().strip('()').split(', ')

        # Add the node and its connections to the network dictionary
        network[node] = (left, right)

    return instructions, network


# Example usage
input_string = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""


file = open('sample.txt', 'r')
input = file.read()

instructions, network = parse_input(input)
# print(f"Instructions: {instructions}")
# print(f"Network: {network}")


def navigate_network(instructions, network):
    # Start at node AAA
    current_node = 'AAA'
    step_count = 0

    # Repeat the instructions until we reach ZZZ
    while current_node != 'ZZZ':
        for instruction in instructions:
            if current_node == 'ZZZ':
                return step_count

            # Navigate based on the instruction
            if instruction == 'L':
                # Move to the left node
                current_node = network[current_node][0]
            elif instruction == 'R':
                # Move to the right node
                current_node = network[current_node][1]

            step_count += 1

    return step_count


steps_to_reach_ZZZ = navigate_network(instructions, network)
print(f"Steps to reach ZZZ: {steps_to_reach_ZZZ}")
