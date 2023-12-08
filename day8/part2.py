from itertools import cycle
import math


def parse_network(input_string):
    lines = input_string.split('\n')
    instructions = lines[0].strip()
    network = {}

    for line in lines[1:]:
        if line.strip() == '':
            continue

        node, connections = line.split('=')
        node = node.strip()
        left, right = connections.strip().strip('()').split(', ')
        network[node] = (left, right)

    return instructions, network


def navigate_network_with_lcm(instructions, network):
    pos = 'AAA'
    nodes = [n for n in network.keys() if n.endswith('A')]
    steps = [0] * len(nodes)
    for d in cycle(instructions):
        pos = network[pos][0] if d == 'L' else network[pos][1]
        if pos == 'ZZZ':
            break
    for i, n in enumerate(nodes):
        pos = n
        for d in cycle(instructions):
            pos = network[pos][0] if d == "L" else network[pos][1]
            steps[i] += 1
            if pos.endswith("Z"):
                break

    return math.lcm(*steps)


# Example usage
input_string = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


file = open('sample.txt', 'r')
input = file.read()

instructions, network = parse_network(input)
steps_to_end = navigate_network_with_lcm(instructions, network)
print(f"Steps to end: {steps_to_end}")
