import sys
from itertools import combinations

example = """1721
979
366
299
675
1456""".split("\n")

with open('2020/py/day01/day01.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines
data = [int(x) for x in data]

ans11 = 0
for a, b in combinations(data, 2):
    if a + b == 2020:
        ans11 = a * b
        break

ans12 = next(a * b for a, b in combinations(data, 2) if a + b == 2020)

assert ans11 == ans12

print(ans11)

# part 2

ans2 = next(a * b * c for a, b, c in combinations(data, 3)
            if a + b + c == 2020)

print(ans2)
