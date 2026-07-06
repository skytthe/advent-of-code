import re
import numpy as np
from collections import defaultdict, Counter

example = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1""".splitlines()


with open('2016/py/day08/day08.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

def printGrid(grid):
    h,w = grid.shape
    s = ""
    for y in range(h):
        for  x in range(w):
            if grid[y,x] > 0:
                s += "#"
            else:
                s += " "
        if y < h-1:
            s += "\n"            
    print(s)

# grid = np.zeros((3,7),dtype=int)
grid = np.zeros((6,50),dtype=int)

for line in data:
    ss = line.split(" ")
    nbrs = list(map(int,re.findall(r"\d+",line)))
    if ss[0] == "rect":
        for y in range(nbrs[1]):
            for  x in range(nbrs[0]):
                grid[y,x] = 1

    elif ss[1] == "column":
        grid[:,nbrs[0]] = np.roll(grid[:,nbrs[0]], nbrs[1])

    elif ss[1] == "row":
        grid[nbrs[0]] = np.roll(grid[nbrs[0]], nbrs[1])
    
    # printGrid(grid)


print(np.sum(grid))

printGrid(grid)
ans2 = "EOARGPHYAO"