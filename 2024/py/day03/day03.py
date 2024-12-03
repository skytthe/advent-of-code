import sys
import re


example1 = """xmul(2,4)%
&mul[3,7]!@^do_not_mul(5,5)
+mul(32,64]th
en(mul(11,8)mul(8,5))""".split("\n")

example2 = [
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

with open('2024/py/day03/day03.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example1
data = example2
data = lines

reg = r'(do\(\))|(don\'t\(\))|(mul\(\d+,\d+\))'
ll = []
for l in data:
    ll += re.findall(reg, l)

ans1 = 0
ans2 = 0

flag = True
reg = r'\d+'
for l in ll:
    if l[0] != '':
        flag = True
    elif l[1] != '':
        flag = False
    elif l[2] != '':
        tmp = re.findall(reg, l[2])
        ans1 += int(tmp[0]) * int(tmp[1])
        if flag:
            ans2 += int(tmp[0]) * int(tmp[1])


print(ans1)
print(ans2)
