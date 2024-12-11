from collections import Counter
from functools import lru_cache


example = """125 17""".strip()

with open('2024/py/day11/day11.txt') as f:
    s = f.read().strip()
    # s = [line.strip() for line in f.readlines()]

data = example
data = s

data = [int(x) for x in data.split()]


def blink(count):
    newCount = Counter()
    for stone, n in count.items():
        if stone == 0:
            newCount[1] += n
        else:
            s = str(stone)
            if len(s) % 2 == 0:
                idx = len(s)//2
                newCount[int(s[:idx])] += n
                newCount[int(s[idx:])] += n
            else:
                newCount[stone * 2024] += n
    return newCount


count = Counter(data)
ans1 = 0
for i in range(75):
    if i == 25:
        ans1 = sum(count.values())
    count = blink(count)

print(ans1)
print(sum(count.values()))
