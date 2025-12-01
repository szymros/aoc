from functools import reduce
import operator


def check_rules(line):
    pairs = list(zip(line[0:], line[1:]))
    diffs = list(
        map(
            lambda x: reduce(operator.sub, map(int, x)),
            pairs,
        )
    )

    return (
        all(map(lambda x: abs(x) == x, diffs)) or all(map(lambda x: abs(x) != x, diffs))
    ) and all(map(lambda x: 1 <= abs(x) <= 3, diffs))


with open("./02/input.txt") as f:
    lines = list(map(str.split, f.readlines()))
    correct_count_p1 = 0
    correct_count_p2 = 0
    for line in lines:
        if check_rules(line):
            correct_count_p1 += 1
            correct_count_p2 += 1
            continue

        if any([check_rules(line[:idx] + line[idx + 1 :]) for idx in range(len(line))]):
            correct_count_p2 += 1
    print(correct_count_p1)
    print(correct_count_p2)
