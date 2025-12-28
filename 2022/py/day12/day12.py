import math
from collections import deque

example = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()

with open('2022/py/day12/day12.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

grid = [list(map(ord, line)) for line in data]
R = len(grid)
C = len(grid[0])

start = next((x, y) for y in range(R) for x in range(C) if grid[y][x] == 83)
end = next((x,y) for y in range(R) for x in range(C) if grid[y][x] == 69)
grid[start[1]][start[0]] = ord("a")
grid[end[1]][end[0]] = ord("z")

moves = [(1,0),(-1,0),(0,1),(0,-1)]

visited = {start}

q = deque()
q.append((start, 0))
while q:
    pos, cost = q.popleft()
    if pos == end:
        print(cost)
        break
    for dx,dy in moves:
        nx,ny = pos[0]+dx, pos[1]+dy
        if 0 <= nx < C and 0 <= ny < R:
            if grid[ny][nx] <= grid[pos[1]][pos[0]]+1:
                if (nx,ny) not in visited:
                    q.append(((nx,ny), cost+1))
                    visited.add((nx,ny))

