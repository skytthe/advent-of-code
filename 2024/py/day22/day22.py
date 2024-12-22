import sys
import math
from collections import defaultdict
import pprint

example = """1
10
100
2024""".split("\n")

example2 = """1
2
3
2024""".split("\n")

with open('2024/py/day22/day22.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = example2
data = lines

initialSecretNumbers = list(map(int, data))


def nextSecretNumber(n):
    tmp = n * 64
    res = (tmp ^ n) % 16777216

    tmp = res // 32
    res = (tmp ^ res) % 16777216

    tmp = res * 2048
    res = (tmp ^ res) % 16777216

    return res
    # this was slower
    # res = (n ^ (n << 6)) % 16777216
    # res = (res ^ (res >> 5)) % 16777216
    # res = (res ^ res << 11) % 16777216
    # return res


ans1 = 0

sequences = defaultdict(list)

for sn in initialSecretNumbers:
    secretNumber = sn
    seen = set()
    changes = []
    prev = sn % 10
    for _ in range(2000):
        secretNumber = nextSecretNumber(secretNumber)
        banana = secretNumber % 10
        changes.append(banana-prev)
        prev = banana
        if len(changes) >= 4:
            tmp = tuple(changes[-4:])
            if tmp not in seen:
                sequences[tmp].append(banana)
                seen.add(tmp)
    ans1 += secretNumber

ans2 = max([(sum(s)) for _, s in sequences.items()])

print(ans1)
print(ans2)
