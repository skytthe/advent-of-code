from scipy.optimize import linprog
import math
import sys
import queue
import re

example = """
""".split("\n")

with open('2024/py/day13/day13.txt') as f:
    s = f.read().strip()
    # s = [line.strip() for line in f.readlines()]

data = example
data = s

data = [[z] for z in data.split("\n\n")]

games = [[int(num) for num in re.findall(r"\d+", x[0])] for x in data]


ans1 = 0

for g in games:
    x1, y1, x2, y2, gx, gy = g

    c = [3, 1]
    A_eq = [
        [x1, x2],
        [y1, y2],
    ]
    b_eq = [0+gx, 0+gy]

    bounds = [(0, 100), (0, 100)]

    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds,
                     integrality=[1, 1])

    if result.success:
        ans1 += int(result.fun)

print(ans1)
