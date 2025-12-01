from functools import reduce

with open("./01/input.txt") as f:
    # part 1
    a = f.read().split()
    even = list(map(int, a[::2]))
    odd = list(map(int, a[1::2]))
    print(
        sum(
            map(
                (lambda x: reduce(lambda lhs, rhs: abs(lhs - rhs), list(x))),
                zip(sorted(even), sorted(odd)),
            )
        )
    )

    # part 2
    print(sum([e * odd.count(e) for e in even]))
