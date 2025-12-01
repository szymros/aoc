from collections import defaultdict

with open("./13/input.txt") as f:
    lines = list(map(str.strip, f.readlines()))

a_token_mult = 3
b_token_mult = 1
parsed = defaultdict(list)

case_number = 0
for line in lines:
    if line == "":
        case_number += 1
        continue
    x = line[line.find("X") + 2 : line.find(",")]
    y = line[line.find("Y") + 2 :]
    if "Prize" in line:
        x = int(x) + 10000000000000
        y = int(y) + 10000000000000
    parsed[case_number].append((int(x), int(y)))

accum = 0
# make a set of 2 linear equations with 2 variables
# solve using determinants
for _, values in parsed.items():
    ax, ay = values[0]
    bx, by = values[1]
    cx, cy = values[2]
    w = (ax * by) - (ay * bx)
    wa = (cx * by) - (cy * bx)
    wb = (ax * cy) - (cx * ay)
    a = wa / w
    b = wb / w
    if int(a) == a and int(b) == b:
        accum += a * a_token_mult + b * b_token_mult

print(accum)
