with open("./15/input.txt") as f:
    lines = list(map(str.strip, f.readlines()))
    split = lines.index("")
    moves = "".join(lines[split + 1 :])
    room_map = list(map(list, lines[:split]))

moves_mapping = {
    "^": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
    "v": (0, 1),
}


# part 1
robot_pos = (0, 0)
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "@":
            robot_pos = (x, y)

current_pos = robot_pos
for move in moves:
    d_x, d_y = moves_mapping[move]
    accum = []
    st_x, st_y = current_pos[0], current_pos[1]
    next_x, next_y = current_pos[0] + d_x, current_pos[1] + d_y
    sx, sy = next_x, next_y
    while 0 <= next_x < len(room_map[0]) and 0 <= next_y < len(room_map):
        char = room_map[next_y][next_x]
        if char == ".":
            if len(accum):
                room_map[accum[0][1]][accum[0][0]] = "."
                for s in accum:
                    room_map[s[1]][s[0]] = "O"
                room_map[next_y][next_x] = "O"
            room_map[sy][sx] = "@"
            room_map[st_y][st_x] = "."
            current_pos = (sx, sy)
            break
        elif char == "O":
            accum.append((next_x, next_y))
            current_pos = (next_x, next_y)
            next_x, next_y = current_pos[0] + d_x, current_pos[1] + d_y
        elif char == "#":
            current_pos = st_x, st_y
            break

accum = 0
for y, line in enumerate(room_map):
    for x, char in enumerate(line):
        if room_map[y][x] == "O":
            accum += x + 100 * y
print(accum)

# part 2
doubled_room = []
for line in lines:
    new_line = []
    for char in line:
        match char:
            case ".":
                new_line.extend([".", "."])
            case "O":
                new_line.extend(["[", "]"])
            case "@":
                new_line.extend(["@", "."])
            case "#":
                new_line.extend(["#", "#"])
    if new_line:
        doubled_room.append(new_line)

robot_pos = (0, 0)
for y, line in enumerate(doubled_room):
    for x, char in enumerate(line):
        if char == "@":
            robot_pos = (x, y)

current_pos = robot_pos
for move in moves:
    d_x, d_y = moves_mapping[move]
    next_x, next_y = (current_pos[0] + d_x, current_pos[1] + d_y)
    if (
        0 > next_x
        or next_x > len(doubled_room[0])
        or next_y < 0
        or next_y > len(doubled_room)
    ):
        continue
    char = doubled_room[next_y][next_x]
    sx, sy = next_x, next_y
    if move in [">", "<"]:
        accum = []
        while char != "#":
            if char == ".":
                if len(accum):
                    for s in map(lambda x: (x[0] + d_x, x[1] + d_y, x[2]), accum):
                        doubled_room[s[1]][s[0]] = s[2]
                doubled_room[sy][sx] = "@"
                doubled_room[current_pos[1]][current_pos[0]] = "."
                break
            elif char in ["[", "]"]:
                accum.append((next_x, next_y, char))
            next_x, next_y = next_x + d_x, next_y + d_y
            char = doubled_room[next_y][next_x]
        if char != "#":
            current_pos = sx, sy
    else:
        broke = False
        queue = [(next_x, next_y)]
        visited = set()
        while len(queue) > 0:
            current_x, current_y = queue.pop(0)
            current_char = doubled_room[current_y][current_x]
            if current_char == "[":
                queue.append((current_x + 1 + d_x, current_y + d_y))
                visited.add((current_x + 1, current_y, "]"))
            elif current_char == "]":
                queue.append((current_x - 1 + d_x, current_y + d_y))
                visited.add((current_x - 1, current_y, "["))
            elif current_char == ".":
                continue
            elif current_char == "#":
                broke = True
                break
            queue.append((current_x + d_x, current_y + d_y))
            visited.add((current_x, current_y, current_char))
        if len(queue) == 0 and not broke:
            for vx, vy, _ in visited:
                doubled_room[vy][vx] = "."
            for vx, vy, vchar in map(lambda x: (x[0] + d_x, x[1] + d_y, x[2]), visited):
                doubled_room[vy][vx] = vchar
            doubled_room[sy][sx] = "@"
            doubled_room[current_pos[1]][current_pos[0]] = "."
            current_pos = next_x, next_y

accum = 0
for y, line in enumerate(doubled_room):
    for x, char in enumerate(line):
        if doubled_room[y][x] == "[":
            accum += x + 100 * y
print(accum)
