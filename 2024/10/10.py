with open("./10/input.txt") as f:
    lines = list(map(str.strip, f.readlines()))

zeros = []
for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c == "0":
            zeros.append((int(x), int(y)))

moves = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]


def step(node):
    head_x, head_y = node
    moved = [
        (head_x + move[0], head_y + move[1])
        for move in moves
        if 0 <= (head_x + move[0]) < len(lines[0])
        and 0 <= (head_y + move[1]) < len(lines)
    ]
    check_moved = [
        int(lines[m[1]][m[0]]) == int(lines[head_y][head_x]) + 1 for m in moved
    ]
    print([m for m in moved if check_moved[moved.index(m)]])
    return [m for m in moved if check_moved[moved.index(m)]]


nodes = zeros
counter = 0
for node in nodes:
    queue = [node]
    visited = set()
    while len(queue) > 0:
        current = queue.pop(0)
        # uncomment the if below to solve part 1 and leave commented for part 2
        # "|" show what should be in the if block
        # if current not in visited:                 #|
        queue.extend(step(current))  # |
        visited.add(current)  # |
        if lines[current[1]][current[0]] == "9":  # |
            counter += 1  # |

print(counter)
