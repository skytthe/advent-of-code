import sys

example = """
""".split("\n")

with open('2024/py/day15/day15.txt') as f:
    s = f.read().strip()
    # s = [line.strip() for line in f.readlines()]

data = example
data = s

grid, moves = data.split("\n\n")

grid = [list(x) for x in grid.split()]
moves = list(moves.replace("\n", ""))

row = len(grid)
col = len(grid[0])

x, y = next((j, i) for j in range(col)
            for i in range(row) if grid[i][j] == '@')
grid[y][x] = '.'


dir = {'>': (1, 0),
       '<': (-1, 0),
       '^': (0, -1),
       'v': (0, 1), }


def printGrid(grid, px, py):
    for yy, l in enumerate(grid):
        s = ""
        for xx, ch in enumerate(l):
            if px == xx and py == yy:
                s += '@'
            else:
                s += ch
        print(s)
    print()


# print("Initial state:")
# printGrid(grid, x, y)
for m in moves:
    dx, dy = dir[m]
    if grid[y+dy][x+dx] == '#':
        pass
    elif grid[y+dy][x+dx] == '.':
        y, x = y+dy, x+dx
    elif grid[y+dy][x+dx] == 'O':
        stp = 1
        st = ""
        while True:
            stp += 1
            if grid[y+dy*stp][x+dx*stp] != 'O':
                break
        if grid[y+dy*stp][x+dx*stp] == '#':
            pass
        elif grid[y+dy*stp][x+dx*stp] == '.':
            grid[y+dy][x+dx] = '.'
            grid[y+dy*stp][x+dx*stp] = 'O'
            y, x = y+dy, x+dx
    # print(f"Move {m}: {dx},{dy}")
    # printGrid(grid, x, y)


ans1 = 0

for y, l in enumerate(grid):
    for x, ch in enumerate(l):
        if ch == "O":
            ans1 += 100 * y + x

print(ans1)
