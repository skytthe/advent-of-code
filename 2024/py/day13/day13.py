from scipy.optimize import linprog
import math
import sys
import queue
import re

example = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

with open('2024/py/day13/day13.txt') as f:
    s = f.read().strip()
    # s = [line.strip() for line in f.readlines()]

data = example
data = s

data = [[x] for x in data.split("\n\n")]

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


ans2 = []

for g in games:
    x1, y1, x2, y2, gx, gy = g

    c = [3, 1]
    A_eq = [
        [x1, x2],
        [y1, y2],
    ]
    b_eq = [10000000000000+gx, 10000000000000+gy]

    bounds = [(0, None), (0, None)]

    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

    if result.success:
        a, b = result.x
        if (round(a) * x1 + round(b) * x2 == 10000000000000+gx) and (round(a) * y1 + round(b) * y2 == 10000000000000+gy):
            # print(g)
            ans2.append(round(result.fun))

# print(len(games))
# print(len(ans2))
print(sum(ans2))
