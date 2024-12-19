import sys

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


def possible(pattern):
    if pattern in towelPatterns:
        return True
    flag = False
    for p in towelPatterns:
        if pattern.startswith(p):
            flag = flag or possible(pattern[len(p):])
    return flag


ans1 = 0

for design in designs:
    # print(design)
    if possible(design):
        ans1 += 1

print(ans1)
