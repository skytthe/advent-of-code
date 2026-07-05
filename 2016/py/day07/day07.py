import re
import numpy as np
from collections import defaultdict, Counter

example = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn""".splitlines()

example2 = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb""".splitlines()


with open('2016/py/day07/day07.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example2
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


ans2 = 0
for line in data:
    aba = set()
    bab = []
    hypernet = False
    idx = 0
    for n in range(len(line)-2):
        if line[n] == "[":
            hypernet = True
            idx = n+1
            continue
        if line[n] == "]":
            hypernet = False
            bab.append(line[idx:n])
            continue
        if not hypernet:
            if line[n] != line[n+1] and line[n] == line[n+2]:
                aba.add(line[n:n+3])

    flag = False
    for s in aba:
        tmp = s[1]+s[0]+s[1]
        for hn in bab:
            if hn.count(tmp) > 0:
                flag = True
    if flag:
        ans2 += 1

print(ans2)
