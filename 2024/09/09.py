with open("./09/input.txt") as f:
    data = f.read().strip()

# part 1
memory = []
counter = 0
for idx, lenght in enumerate(data):
    char = ""
    if idx % 2 == 1:
        char = "."
    else:
        char = str(counter)
        counter += 1
    for i in range(int(lenght)):
        memory.append(char)

bot_idx = 0
top_idx = len(memory) - 1
while bot_idx < top_idx:
    if memory[bot_idx] != ".":
        bot_idx += 1
        continue
    if memory[top_idx] != ".":
        memory[bot_idx] = memory[top_idx]
        memory[top_idx] = "."
        bot_idx += 1
    else:
        top_idx -= 1


product = 0

for idx, val in enumerate(memory):
    if val.isdigit():
        product += idx * int(val)

print(product)

# part 2

memory = []
counter = 0

for idx, lenght in enumerate(data):
    char = ""
    if idx % 2 == 1:
        char = "."
    else:
        char = str(counter)
        counter += 1
    memory.append((char, lenght))

bot_idx = 0
while bot_idx < len(memory) - 1:
    bot_char, bot_len = memory[bot_idx]
    if bot_char != ".":
        bot_idx += 1
        continue
    for top_idx in range(len(memory) - 1, bot_idx, -1):
        top_char, top_len = memory[top_idx]
        if top_char != ".":
            if int(bot_len) >= int(top_len):
                memory[bot_idx] = (top_char, top_len)
                memory[top_idx] = (bot_char, top_len)
                diff = int(bot_len) - int(top_len)
                if diff > 0:
                    memory.insert(bot_idx + 1, (bot_char, diff))
                break
    bot_idx += 1

product = 0
index = 0
for i in memory:
    char, len = i
    if char.isdigit():
        product += sum([int(char) * (int(x) + index) for x in range(int(len))])
    index += int(len)

print(product)
