with open("./05/input.txt") as f:
    lines = list(map(str.strip, f.readlines()))
    orderings = lines[: lines.index("")]
    updates = lines[lines.index("") + 1 :]

    less = {}
    for ordering in orderings:
        left, right = ordering.split("|")
        if int(left) in less:
            less[int(left)].append(int(right))
        else:
            less[int(left)] = [int(right)]
        if int(right) not in less:
            less[int(right)] = []

    # part 1
    sum = 0
    incorrects = []
    for idx, update in enumerate(updates):
        update = list(map(int, update.split(",")))
        correct = True
        i = 0
        while correct and i < len(update):
            tail_check = [k in less[update[i]] for k in update[i + 1 :]]
            if not all(tail_check):
                incorrects.append((update, tail_check))
            correct = all(tail_check)
            i += 1

        if correct:
            sum += update[int(len(update) / 2)]

    print(sum)

    # part 2
    sum = 0

    for incorrect in incorrects:
        update, tail_not_in_order = incorrect
        for tail_len in range(len(tail_not_in_order), -1, -1):
            nibble = update[:-tail_len]
            pivot = len(update) - tail_len
            for i in range(len(nibble) - 1, -1, -1):
                if update[i] in less[update[pivot]]:
                    update[i], update[pivot] = update[pivot], update[i]
                    i, pivot = pivot, i
                else:
                    break
        sum += update[int(len(update) / 2)]

    print(sum)
