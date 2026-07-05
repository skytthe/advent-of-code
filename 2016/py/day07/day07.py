import re
import numpy as np
from collections import defaultdict, Counter

example = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn""".splitlines()

with open('2016/py/day07/day07.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

ans = 0
for line in data:
    abba = False
    hypernet = False
    for n in range(len(line)-3):
        if line[n] == "[":
            hypernet = True
            continue
        if line[n] == "]":
            hypernet = False
            continue
        if line[n] != line[n+1] and (line[n] == line[n+3] and line[n+1] == line[n+2]):
            if hypernet:
                abba = False
                break
            else:
                abba = True

    if abba:
        ans += 1

print(ans)