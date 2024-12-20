import sys
from collections import defaultdict
from itertools import combinations

example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".split("\n")

with open('2024/py/day08/day08.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

ans1 = 0
ans2 = 0

row = len(data)
col = len(data[0])

antennas = defaultdict(list)
antinodes1 = set()
antinodes2 = set()

for y, l in enumerate(data):
    for x, e in enumerate(l):
        if e != '.':
            antennas[e].append((x, y))

for k in antennas:
    for a, b in combinations(antennas[k], 2):
        dx, dy = b[0]-a[0], b[1]-a[1]
        antinodes1.add((a[0]-dx, a[1]-dy))
        antinodes1.add((b[0]+dx, b[1]+dy))
        for i in range(-50, 50):
            antinodes2.add((a[0]-(dx*i), a[1]-(dy*i)))
            antinodes2.add((b[0]+(dx*i), b[1]+(dy*i)))

for x, y in antinodes1:
    if x >= 0 and y >= 0 and x < col and y < row:
        ans1 += 1

for x, y in antinodes2:
    if x >= 0 and y >= 0 and x < col and y < row:
        ans2 += 1

print(ans1)
print(ans2)
