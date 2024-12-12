from collections import Counter
from functools import cache


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


calls2 = 0


def blink2(stone, steps):
    global calls2
    calls2 += 1
    if steps == 0:
        return 1
    if stone == 0:
        return blink2(1, steps-1)
    s = str(stone)
    length = len(s)
    if length % 2 == 0:
        return blink2(int(s[length//2:]), steps-1) + blink2(int(s[:length//2]), steps-1)
    else:
        return blink2(stone * 2024, steps-1)


calls3 = 0


@cache
def blink3(stone, steps):
    global calls3
    calls3 += 1
    if steps == 0:
        return 1
    if stone == 0:
        return blink3(1, steps-1)
    s = str(stone)
    length = len(s)
    if length % 2 == 0:
        return blink3(int(s[length//2:]), steps-1) + blink3(int(s[:length//2]), steps-1)
    else:
        return blink3(stone * 2024, steps-1)


count = Counter(data)
ans1 = 0
for i in range(75):
    if i == 25:
        ans1 = sum(count.values())
    count = blink(count)

print(ans1)
print(sum(count.values()))

print()

ans1 = sum([blink2(stone, 25) for stone in data])
ans1 = sum([blink3(stone, 25) for stone in data])

print(f"blink2(25) calls no cache: {calls2}")
print(f"blink3(25) calls w. cache: {calls3}")

ans2 = sum([blink3(stone, 75) for stone in data])

print(f"blink3(75) calls w. cache: {calls3}")

print()
print(ans1)
print(ans2)
