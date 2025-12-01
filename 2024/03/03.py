import re

with open("./03/input.txt") as f:
    input = f.read()
    memory = input
    sum = 0

    # part 1
    matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", memory)
    for match in matches:
        splits = match[len("mul(") :].split(",")
        sum += int(splits[0]) * int(splits[1][:-1])

    print(sum)

    # part 2
    sum = 0
    current = True
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", memory)
    for match in matches:
        if match.startswith("mul"):
            splits = match[len("mul(") :].split(",")
            if current:
                sum += int(splits[0]) * int(splits[1][:-1])
        elif match == "do()":
            current = True
        elif match == "don't()":
            current = False
    print(sum)
