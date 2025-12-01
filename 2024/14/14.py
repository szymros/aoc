with open("./14/input.txt") as f:
    lines = list(map(str.strip, f.readlines()))

width = 101
height = 103
delta_time = 100

robots = []
for line in lines:
    splits = line.split(" ")
    p = list(map(int, splits[0][splits[0].find("=") + 1 :].split(",")))
    v = list(map(int, splits[1][splits[1].find("=") + 1 :].split(",")))
    robots.append((p, v))

# part 1
new_robots = []

for robot in robots:
    x, y = robot[0]
    v_x, v_y = robot[1]
    x += v_x * 100
    y += v_y * 100
    x = x % width
    y = y % height
    new_robots.append((x, y))

quads = [0, 0, 0, 0]

for robot in new_robots:
    half_width = int(width / 2)
    half_height = int(height / 2)
    x, y = robot
    if x < half_width and y < half_height:
        quads[0] += 1
    elif x > half_width and y < half_height:
        quads[1] += 1
    elif x > half_width and y > half_height:
        quads[2] += 1
    elif x < half_width and y > half_height:
        quads[3] += 1

result = 1
for quad in quads:
    result *= quad
print(result)
