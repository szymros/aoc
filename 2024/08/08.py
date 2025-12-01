with open("./08/input.txt") as f:
    lines = list(map(str.strip, f.readlines()))

    antennas = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))

    anti_nodes = []
    anti_nodes_part_2 = []

    for antenna in antennas:
        antenna = antennas[antenna]

        for idx in range(len(antenna)):
            current = antenna[idx]
            rest = antenna[:idx] + antenna[idx + 1 :]

            for r in rest:
                dx = r[0] - current[0]
                dy = r[1] - current[1]

                anti_node1 = (
                    r[0] + dx,
                    r[1] + dy,
                )
                anti_node2 = (
                    current[0] - dx,
                    current[1] - dy,
                )

                if 0 <= anti_node1[0] < len(lines[0]) and 0 <= anti_node1[1] < len(
                    lines
                ):
                    anti_nodes.append(anti_node1)
                if 0 <= anti_node2[0] < len(lines[0]) and 0 <= anti_node2[1] < len(
                    lines
                ):
                    anti_nodes.append(anti_node2)

                x, y = current[0], current[1]
                while 0 <= x < len(lines[0]) and 0 <= y < len(lines):
                    anti_nodes_part_2.append((x, y))
                    x, y = x + dx, y + dy

    print(len(set(anti_nodes)))
    print(len(set(anti_nodes_part_2)))
