import sys
from functools import cache

example = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

with open('2024/py/day19/day19.txt') as f:
    s = f.read().strip()

data = example
data = s


a, b = data.split("\n\n")


towelPatterns = set(a.split(', '))
designs = b.split()


@cache
def possible(pattern):
    if len(pattern) == 0:
        return 1
    flag = 0
    for p in towelPatterns:
        if pattern.startswith(p):
            flag += possible(pattern[len(p):])
    return flag


ans1 = 0
ans2 = 0

for design in designs:
    tmp = possible(design)
    if tmp > 0:
        ans1 += 1
    ans2 += tmp

print(ans1)
print(ans2)
