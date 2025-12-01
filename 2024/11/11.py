from collections import defaultdict

with open("./11/input.txt") as f:
    line = f.readline().strip().split()
    print(line)

# part 1
current = line
for _ in range(25):
    new = []
    for i in current:
        if int(i) == 0:
            new.append("1")
        elif len(i) % 2 == 0:
            mid = int(len(i) / 2)
            new.extend([(str(int(i[:mid]))), str(int(i[mid:]))])
        else:
            new.append(str(int(i) * 2024))
    current = new

print(len(current))


# part 2
memo = {key: 1 for key in line}
for _ in range(75):
    new_memo = defaultdict(int)
    for num in list(memo):
        count = memo[num] if memo[num] > 0 else 1
        new = []
        if int(num) == 0:
            new_memo["1"] += count
        elif len(num) % 2 == 0:
            mid = int(len(num) / 2)
            new_memo[str(int(num[:mid]))] += count
            new_memo[str(int(num[mid:]))] += count
        else:
            new_memo[str(int(num) * 2024)] += count
    memo = new_memo

print(sum(memo.values()))
