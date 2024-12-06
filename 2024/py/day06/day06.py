import sys

example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split("\n")

with open('2024/py/day06/day06.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

grid = []

visited = set()

x = 0
y = 0

for i, l in enumerate(data):
    tmp = l.find('^')
    if (tmp > -1):
        y = i
        x = tmp
    grid.append(list(l))

grid[y][x] = '.'


def printGrid(g, px, py):
    for i, l in enumerate(g):
        s = ""
        for j, e in enumerate(l):
            if j == px and i == py:
                s += "@"
            else:
                s += e
        print(s)
    print()


dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir_point = 0

while (x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)):
    visited.add((x, y))

    try:
        if (grid[(y+dir[dir_point][1])][(x+dir[dir_point][0])] == '#'):
            dir_point = (dir_point + 1) % 4
    except:
        break

    x += dir[dir_point][0]
    y += dir[dir_point][1]


print(len(visited))
