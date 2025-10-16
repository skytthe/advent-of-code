import numpy as np

example = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split("\n")

with open("2021/py/day11/day11.txt") as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

grid = np.array([list(line) for line in data], dtype=int)

neighbors = ((1,0),
             (-1,0),
             (0,1),
             (0,-1),
             (1,1),
             (-1,-1),
             (-1,1),
             (1,-1),)

flashes = 0
steps = 100
rows, cols = grid.shape
# for _ in range(steps):
step = 0
while True:
    step += 1
    grid[::] += 1
    flag = True
    visited = set()
    while flag:
        flag = False
        for r in range(rows):
            for c in range(cols):
                if grid[r,c] > 9 and (r,c) not in visited:
                    visited.add((r,c))
                    for dr,dc in neighbors:
                        nr,nc = r+dr, c+dc
                        if nr < rows and nr >= 0 and nc < cols and nc >= 0:
                            grid[nr,nc] += 1
                            flag = True
    tmp = np.sum(grid > 9)
    flashes += tmp
    if step == steps:
        print(flashes)
    grid[grid > 9] = 0

    if tmp == rows*cols:
        print(step)
        break
