import sys
from pprint import pprint
import re

example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

with open('2022/py/day05/day05.txt') as f:
    lines = f.read()

data = example
data = lines

stacks, commands = data.split("\n\n")

grid = [list(line) for line in stacks.splitlines()]
stackSize = int(grid[-1][-2])
stacks = [[] for _ in range(stackSize)]
for i in range(len(grid)-2,-1,-1):
    for j in range(stackSize):
        ch = grid[i][1+j*4]
        if ch != " ":
            stacks[j].append(ch)

commands = [list(map(int, re.findall(r"\d+", line))) for line in commands.splitlines()]


for n, start, end in commands:
    for i in range(n):
        stacks[end-1].append(stacks[start-1].pop())

ans1 = "".join([s[-1] for s in stacks])
print(ans1)
