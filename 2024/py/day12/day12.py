import sys
from collections import defaultdict

example = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".split("\n")

with open('2024/py/day12/day12.txt') as f:
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

clusterMap = [[None for _ in range(col)] for _ in range(row)]

ajd4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]

clusters = defaultdict(list)


def step(x, y, ch, id):
    perimeter = 4
    for n in ajd4:
        nx, ny = x+n[1], y+n[0]
        if grid[ny][nx] == ch:
            perimeter += -1
            if clusterMap[ny][nx] is None:
                clusterMap[ny][nx] = id
                step(nx, ny, ch, id)
    clusters[id].append(perimeter)


id = 0
for y in range(1, row-1):
    for x in range(1, col-1):
        ch = grid[y][x]
        if clusterMap[y][x] is None:
            clusterMap[y][x] = id
            step(x, y, ch, id)
            id += 1


ans1 = 0
for id, l in clusters.items():
    ans1 += len(l) * sum(l)

print(ans1)
