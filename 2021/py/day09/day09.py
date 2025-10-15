from pprint import pprint
import numpy as np
from queue import Queue
import math

example = """2199943210
3987894921
9856789892
8767896789
9899965678""".split("\n")

with open("2021/py/day09/day09.txt") as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

grid = np.array([list(map(int,list(line))) for line in data], dtype=int)
grid = np.pad(grid, pad_width=1, mode='constant', constant_values=9)

fourNeighbors = [(1,0),(-1,0),(0,1),(0,-1),]

rows, cols = grid.shape
lowPoints = []
for r in range(1,rows-1):
    for c in range(1,cols-1):
        value = grid[r,c]
        flag = True
        for dr,dc in fourNeighbors:
            if grid[r+dr,c+dc] <= value:
                flag = False
                break
        if flag:
            lowPoints.append(value)

print(sum(lowPoints)+len(lowPoints))


visited = set()
basins = []
for r in range(1,rows-1):
    for c in range(1,cols-1):
        if grid[r,c] == 9:
            continue
        if (r,c) not in visited:
            visited.add((r,c))
            basin = []
            q = Queue()
            q.put((r,c))
            while not q.empty():
                cr,cc = q.get()    
                basin.append((cr,cc))  
                for dr,dc in fourNeighbors:
                    if (cr+dr,cc+dc) not in visited and grid[cr+dr,cc+dc] != 9:
                        q.put((cr+dr,cc+dc))
                        visited.add((cr+dr,cc+dc))
            basins.append(basin)


# print(sorted([len(basin) for basin in basins],reverse=True))
print(math.prod(sorted([len(basin) for basin in basins],reverse=True)[:3]))
