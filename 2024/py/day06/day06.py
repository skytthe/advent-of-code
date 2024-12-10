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

example2 = """#..#...
.......
.......
...^...
#......
..#..#.
.#.....""".split("\n")


example3 = """....
#...
.^#.
.#..""".split("\n")

with open('2024/py/day06/day06.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = example2
data = example3
data = lines

grid = []

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
    res = ""
    for i, l in enumerate(g):
        s = ""
        for j, e in enumerate(l):
            if j == px and i == py:
                s += "@"
            else:
                s += e
        res += s + "\n"
    return res


dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def guardPatrolling(ix, iy, dp, grid):
    x = ix
    y = iy
    dir_pointer = dp
    route = []
    visited = set()

    while (x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)):
        route.append((x, y, dir_pointer))
        if (x, y, dir_pointer) in visited:
            return []
        visited.add((x, y, dir_pointer))

        if ((x+dir[dir_pointer][0]) >= 0 and (y+dir[dir_pointer][1]) >= 0 and (x+dir[dir_pointer][0]) < len(grid[0]) and (y+dir[dir_pointer][1]) < len(grid)):
            if (grid[(y+dir[dir_pointer][1])][(x+dir[dir_pointer][0])] == '#'):
                dir_pointer = (dir_pointer + 1) % 4
            else:
                x += dir[dir_pointer][0]
                y += dir[dir_pointer][1]
        else:
            break

    return route


route = guardPatrolling(x, y, 0, grid)

visited1 = set([(e[0], e[1]) for e in route])

print(len(visited1))

# part 2
obstacles = set()
newGrid = grid
for step in set(route[:-1]):
    cx, cy, cd = step
    if newGrid[(cy+dir[cd][1])][(cx+dir[cd][0])] == '#' or (x == (cx+dir[cd][0]) and y == (cy+dir[cd][1])):
        continue
    newGrid[(cy+dir[cd][1])][(cx+dir[cd][0])] = '#'
    newRoute = guardPatrolling(x, y, 0, newGrid)
    if not newRoute:
        obstacles.add(((cy+dir[cd][1]), (cx+dir[cd][0])))
    newGrid[(cy+dir[cd][1])][(cx+dir[cd][0])] = '.'

print(len(obstacles))
