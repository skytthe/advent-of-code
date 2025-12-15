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

ans1 = max([sum(list(map(int,l.split("\n")))) for l in data.split("\n\n")])

print(ans1)