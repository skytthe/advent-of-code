import sys
import math

example = """1
10
100
2024""".split("\n")

with open('2024/py/day22/day22.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
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

for sn in initialSecretNumbers:
    secretNumber = sn
    for _ in range(2000):
        secretNumber = nextSecretNumber(secretNumber)
    ans1 += secretNumber

print(ans1)
