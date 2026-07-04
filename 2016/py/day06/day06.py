import re
import numpy as np
from collections import defaultdict, Counter

example = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""".splitlines()

with open('2016/py/day06/day06.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

counters = [Counter() for _ in range(len(data[0]))]

for line in data:
    for n, ch in enumerate(line):
        counters[n].update(ch)

ans = ""
ans2 = ""
for c in counters:
    ans += c.most_common()[0][0]
    ans2 += c.most_common()[-1][0]

print(ans)
print(ans2)
