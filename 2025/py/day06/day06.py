import sys
import numpy as np

example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +""".split("\n")

with open('2025/py/day06/day06.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

grid =[list(int(n) for n in line.split()) for line in data[:-1]] 
grid = np.array(grid).T
opr = data[-1].split()



ans1 = 0
for op, vec in zip(opr, grid):
    tmp = 0
    if op == "+":
        tmp += np.sum(vec)
    elif op == "*":
        tmp += np.prod(vec)
    ans1 += tmp

print(ans1)






