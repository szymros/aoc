import re


def transpose(mat):
    transposed = ["" for _ in mat[0]]
    x = 0
    y = 0
    for x in range(len(mat[0])):
        for y in range(len(mat)):
            transposed[x] += mat[y][x]
    return transposed


def part_1(lines):
    count = 0
    rows = len(lines)
    columns = len(lines[0])
    horizontal = ",".join(lines)
    vertical = ",".join(transpose(lines))
    diagnals = []
    antidiagnals = []

    for row in range(rows):
        diagnal = ""
        antidiagnal = ""
        y, x = row, 0
        anti_x = columns - 1
        while y < rows and x < columns:
            diagnal += lines[y][x]
            antidiagnal += lines[y][anti_x]
            y += 1
            x += 1
            anti_x -= 1
        diagnals.append(diagnal)
        antidiagnals.append(antidiagnal)

    for column in range(1, columns):
        diagnal = ""
        antidiagnal = ""
        y, x = 0, column
        anti_x = columns - column - 1
        while y < rows and x < columns:
            diagnal += lines[y][x]
            antidiagnal += lines[y][anti_x]
            y += 1
            x += 1
            anti_x -= 1
        diagnals.append(diagnal)
        antidiagnals.append(antidiagnal)

    diagnals = ",".join(diagnals)
    antidiagnals = ",".join(antidiagnals)

    count += len(re.findall(r"XMAS", horizontal) + re.findall(r"SAMX", horizontal))
    count += len(re.findall(r"XMAS", vertical) + re.findall(r"SAMX", vertical))
    count += len(re.findall(r"XMAS", diagnals) + re.findall(r"SAMX", diagnals))
    count += len(re.findall(r"XMAS", antidiagnals) + re.findall(r"SAMX", antidiagnals))
    print(count)


def part_2(lines):
    count = 0
    rows = len(lines)
    columns = len(lines[0])
    for row in range(1, rows - 1):
        for col in range(1, columns - 1):
            if lines[row][col] == "A":
                diag = (
                    lines[row - 1][col - 1] + lines[row][col] + lines[row + 1][col + 1]
                )
                anti_diag = (
                    lines[row - 1][col + 1] + lines[row][col] + lines[row + 1][col - 1]
                )
                if (diag == "MAS" or diag == "SAM") and (
                    anti_diag == "MAS" or anti_diag == "SAM"
                ):
                    count += 1
    print(count)


with open("./04/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    part_1(lines)
    part_2(lines)
