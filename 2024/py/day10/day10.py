import sys

example = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split("\n")

with open('2024/py/day10/day10.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

row = len(data)+2
col = len(data[0])+2

grid = []
p = ['.' for _ in range(len(data[0])+2)]
grid.append(p)
for l in data:
    grid.append(['.']+list(l)+['.'])
grid.append(p)


def walk(x, y, h):
    if h == '9':
        s = set()
        s.add((x, y))
        return s
    else:
        res = set()
        if grid[y+1][x] == str(int(h)+1):
            res = res | walk(x, y+1, str(int(h)+1))
        if grid[y-1][x] == str(int(h)+1):
            res = res | walk(x, y-1, str(int(h)+1))
        if grid[y][x+1] == str(int(h)+1):
            res = res | walk(x+1, y, str(int(h)+1))
        if grid[y][x-1] == str(int(h)+1):
            res = res | walk(x-1, y, str(int(h)+1))
        return res


ans1 = 0
for y in range(row):
    for x in range(col):
        if grid[y][x] == '0':
            ans1 += len(walk(x, y, '0'))

print(ans1)


def walk2(x, y, h):
    if h == '9':
        return 1
    else:
        res = 0
        if grid[y+1][x] == str(int(h)+1):
            res += walk2(x, y+1, str(int(h)+1))
        if grid[y-1][x] == str(int(h)+1):
            res += walk2(x, y-1, str(int(h)+1))
        if grid[y][x+1] == str(int(h)+1):
            res += walk2(x+1, y, str(int(h)+1))
        if grid[y][x-1] == str(int(h)+1):
            res += walk2(x-1, y, str(int(h)+1))
        return res


ans2 = 0
for y in range(row):
    for x in range(col):
        if grid[y][x] == '0':
            ans2 += walk2(x, y, '0')

print(ans2)
