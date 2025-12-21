
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
