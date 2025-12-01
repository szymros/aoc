from itertools import product

with open("./07/test.txt") as f:
    lines = f.readlines()
    print(lines)
    sum = 0
    for line in lines:
        check_sum, values = map(str.strip, line.split(":"))
        check_sum = int(check_sum)
        values = list(map(int, values.split()))
        operators = list(product(["*", "+", "||"], repeat=len(values) - 1))
        accum = values[0]
        for ops in operators:
            for i in range(1, len(values)):
                match ops[i - 1]:
                    case "+":
                        accum = accum + values[i]
                    case "*":
                        accum = accum * values[i]
                    case "||":
                        accum = int(str(accum) + str(values[i]))
            if accum == int(check_sum):
                sum += accum
                break
            accum = values[0]
        print(sum)
