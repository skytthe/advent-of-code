import math

example = """30373
25512
65332
33549
35390""".splitlines()

with open('2022/py/day08/day08.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

grid = [list(map(int, line)) for line in data]
R = len(grid)
C = len(grid[0])

visible = set()

for r in range(R):
    visible.add((0,r))
    prev = grid[r][0]
    for c in range(1,C):
        cur = grid[r][c]
        if cur > prev:
            visible.add((c,r))
            prev = cur

for r in range(R):
    visible.add((C-1,r))
    prev = grid[r][C-1]
    for c in range(C-2,0,-1):
        cur = grid[r][c]
        if cur > prev:
            visible.add((c,r))
            prev = cur

for c in range(C):
    visible.add((c,0))
    prev = grid[0][c]
    for r in range(1,R):
        cur = grid[r][c]
        if cur > prev:
            visible.add((c,r))
            prev = cur

for c in range(C):
    visible.add((c,R-1))
    prev = grid[R-1][c]
    for r in range(R-2,0,-1):
        cur = grid[r][c]
        if cur > prev:
            visible.add((c,r))
            prev = cur

print(len(visible))


def scan2(x, y, dx, dy, grid, R, C):
    height = grid[y][x]
    cx,cy = x+dx,y+dy
    score = 0
    while 0 <= cy < R and 0 <= cx < C:
        score += 1
        if grid[cy][cx] >= height:
            break
        cx,cy = cx+dx,cy+dy
    return score

neighbors = [(1,0),(-1,0),(0,1),(0,-1)]

ans2 = 0
for x,y in visible:
    scenicScore = []
    for dx,dy in neighbors:
        scenicScore.append(scan2(x, y, dx, dy, grid, R, C))
    tmp = math.prod(scenicScore)
    if tmp > ans2:
        ans2 = tmp

print(ans2)
