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

# brute force
ans11 = 0
for g in games:
    x1, y1, x2, y2, gx, gy = g
    res = float('inf')
    for a in range(101):
        for b in range(101):
            if a * x1 + b * x2 == gx and a * y1 + b * y2 == gy:
                res = min(res, 3*a + b)
    if res != float('inf'):
        ans11 += res


# Analytic
"""
    Solve:
    a * x1 + b * x2 == gx,
    a * y1 + b * y2 == gy
=>
    a = -((-gy * x2 + gx * y2)/(x2 * y1 - x1 * y2))
    b = -(( gy * x1 - gx * y1)/(x2 * y1 - x1 * y2))
"""


def getAnalyticSolution(x1, y1, x2, y2, gx, gy):
    a = -((-gy * x2 + gx * y2)/(x2 * y1 - x1 * y2))
    b = -((gy * x1 - gx * y1)/(x2 * y1 - x1 * y2))
    return (a, b)


ans12 = 0
for g in games:
    x1, y1, x2, y2, gx, gy = g
    a, b = getAnalyticSolution(x1, y1, x2, y2, gx, gy)
    if a % 1 == 0 and a <= 100 and b % 1 == 0 and b <= 100:
        ans12 += 3 * a + b


# LP
ans13 = 0

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
        ans13 += int(result.fun)

assert ans11 == ans12
assert ans11 == ans13

print(ans13)

# brute force
# - not viable

# Analytic
ans22 = 0
for g in games:
    x1, y1, x2, y2, gx, gy = g
    gx, gy = 10000000000000+gx, 10000000000000+gy
    a, b = getAnalyticSolution(x1, y1, x2, y2, gx, gy)
    if a % 1 == 0 and b % 1 == 0:
        ans22 += 3 * a + b

# LP
ans23 = []

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
            ans23.append(round(result.fun))


assert ans22 == sum(ans23)

# print(len(games))
# print(len(ans2))
print(sum(ans23))
