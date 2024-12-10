import re

example = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".split("\n")

with open('2020/py/day02/day02.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

ans1 = 0
for l in data:
    tmp = l.split(" ")
    a, b, c, p = (*map(int, re.findall(r'\d+', tmp[0])),
                  tmp[1][0], tmp[2])

    if a <= p.count(c) <= b:
        ans1 += 1

print(ans1)
