import sys
import re


example = """xmul(2,4)%
&mul[3,7]!@^do_not_mul(5,5)
+mul(32,64]th
en(mul(11,8)mul(8,5))""".split("\n")

with open('2024/py/day03/day03.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

reg = r'mul\(\d+,\d+\)'
ll = []
for l in data:
    ll += re.findall(reg, l)

reg = r'\d+'
lm = []
for l in ll:
    lm += [re.findall(reg, l)]

ans1 = 0
for l in lm:
    print(l)
    ans1 += int(l[0]) * int(l[1])

print(ans1)
