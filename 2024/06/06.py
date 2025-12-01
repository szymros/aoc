with open("./06/input.txt") as f:
    lines = list(map(str.strip, f.readlines()))

    # take into account that the lines are read form top to bottom
    directions = {
        "^": (0, -1),
        ">": (1, 0),
        "<": (-1, 0),
        "v": (0, 1),
    }

    rotations = {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^",
    }

    start = []
    for y, line in enumerate(lines):
        x = [x for x in enumerate(line) if x[1] in directions]
        if len(x) > 0:
            start = [x[0], y]
            break

    x, current_dir = start[0]
    y = start[1]

    # part 1
    positions = []
    step_x, step_y = directions[current_dir]
    visited = [(x + step_x, y + step_y, current_dir)]
    while 0 <= x < len(lines[0]) and 0 <= y < len(lines):
        char = lines[y][x]
        if (x, y) not in positions:
            positions.append((x, y))
        step_x, step_y = directions[current_dir]
        next_x, next_y = x + step_x, y + step_y
        try:
            if lines[next_y][next_x] == "#":
                current_dir = rotations[current_dir]
                visited.append((x, y, current_dir))
            else:
                x, y = next_x, next_y
        except:
            break

    print(len(positions))

    # part 2
    # works on test data but doesn't on the actual input :/
    fixes = []
    for idx in range(len(visited)):
        x, y, direction = visited[idx]
        step_x, step_y = directions[direction]
        next_x, next_y, next_dir = 0, 0, ""
        if idx < len(visited) - 1:
            next_x, next_y, next_dir = visited[idx + 1]
        else:
            next_x, next_y, next_dir = (
                x if step_x == 0 else 0 if step_x < 0 else len(lines[0]),
                y if step_y == 0 else 0 if step_y < 0 else len(lines),
                rotations[direction],
            )

        for _ in range(abs(next_x - x) + abs(next_y - y)):
            rotated_step_x, rotated_step_y = directions[next_dir]
            test_x, test_y = x, y
            while 0 <= test_x < len(lines[0]) and 0 <= test_y < len(lines):
                tmp_x, tmp_y = test_x + rotated_step_x, test_y + rotated_step_y
                if (test_x, test_y, rotations[next_dir]) in visited[1:]:
                    fixes.append((tmp_x, tmp_y))
                test_x, test_y = tmp_x, tmp_y
            x, y = x + step_x, y + step_y

    print(len(set(fixes)))
