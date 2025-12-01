from collections import defaultdict

with open("./12/input.txt") as f:
    lines = list(map(str.strip, f.readlines()))

directions = [
    (1, 0, "E"),
    (-1, 0, "W"),
    (0, 1, "N"),
    (0, -1, "S"),
]

# part 1
areas = defaultdict(list)
walls = defaultdict(list)
outside = defaultdict(list)
visited = set()
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if (x, y) in visited:
            continue
        area = [(x, y)]
        queue = [(x, y)]
        current_outside = set()
        visited.add((x, y))
        walls_accum = 0
        while len(queue) > 0:
            current_x, current_y = queue.pop(0)
            current_walls = 4
            for dir in directions:
                dy = dir[1] + current_y
                dx = dir[0] + current_x
                if dy > len(lines) - 1 or dy < 0 or dx > len(lines[0]) - 1 or dx < 0:
                    current_outside.add((dx, dy, dir[2]))
                    continue
                if lines[dy][dx] == char:
                    current_walls -= 1
                    if (dx, dy) not in visited:
                        area.append((dx, dy))
                        queue.append((dx, dy))
                        visited.add((dx, dy))
                else:
                    current_outside.add((dx, dy, dir[2]))
            walls_accum += current_walls
        outside[char].append(current_outside)
        walls[char].append(walls_accum)
        areas[char].append(area)

accum = 0
for char in areas:
    accum += sum([z[0] * z[1] for z in zip(map(len, areas[char]), walls[char])])
print(accum)

# part 2
# this is awful and i hate this
sides = defaultdict(list)

for char, vals in outside.items():
    for side in vals:
        n = list(filter(lambda x: x[2] == "N", side))
        s = list(filter(lambda x: x[2] == "S", side))
        w = list(filter(lambda x: x[2] == "W", side))
        e = list(filter(lambda x: x[2] == "E", side))
        sides[char].append([n, s, w, e])

side_counter = defaultdict(list)
for char, vals in sides.items():
    for side in vals:
        sum_sides = 0
        for side_from_dir in side:
            visited = set()
            current_area = []
            for point in side_from_dir:
                if point in visited:
                    continue
                x, y, dir = point
                queue = [point]
                area = [point]
                visited.add(point)
                while len(queue) > 0:
                    current_x, current_y, current_dir = queue.pop(0)
                    for dir in directions:
                        dy = dir[1] + current_y
                        dx = dir[0] + current_x
                        if (dx, dy, current_dir) in side_from_dir:
                            if (dx, dy, current_dir) not in visited:
                                area.append((dx, dy, current_dir))
                                queue.append((dx, dy, current_dir))
                                visited.add((dx, dy, current_dir))
                current_area.append(area)
            sum_sides += len(current_area)
        side_counter[char].append(sum_sides)

accum = 0
for char in areas:
    accum += sum([z[0] * z[1] for z in zip(map(len, areas[char]), side_counter[char])])
print(accum)
