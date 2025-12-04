import sys
from pprint import pprint

example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".split("\n")

with open('2025/py/day04/day04.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

grid0 = [list(ch) for ch in data]

grid = [list(ch) for ch in data]
gridx = [list(ch) for ch in data]


ans1 = 0
flag1 = True


for _ in range(50):
    for y in range(len(gridx)):
        for x in range(len(gridx[y])):
            gridx[y][x] = grid[y][x]     

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                neighbors = 0
                gridx[y][x] = "@"
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        if not (dx == 0 and dy == 0):
                            ny,nx = dy+y, dx + x
                            if ny >= 0 and ny < len(grid) and nx >= 0 and nx < len(grid[y]):
                                if grid[ny][nx] == "@":
                                    neighbors += 1
                                    
                if neighbors < 4:
                    if flag1:
                        ans1 += 1
                    gridx[y][x] = "."
    grid = gridx
    flag1 = False


before, after = 0, 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid0[y][x] == "@":
            before += 1
        if grid[y][x] == "@":
            after += 1
ans2 = before - after

print(ans1)
print(ans2)

