import sys

example = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

with open('2022/py/day01/day01.txt') as f:
    lines = f.read()

data = example
data = lines

cals = [sum(list(map(int,l.split("\n")))) for l in data.split("\n\n")]
ans1 = max(cals)
ans2 = sum(sorted(cals, reverse=True)[:3])

print(ans1)
print(ans2)
