import sys
from itertools import combinations
import math

example = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split("\n")

with open('2020/py/day03/day03.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

grid = [list(x) for x in data]
row, col = len(grid), len(grid[0])

x = y = 0

ans11 = 0
while y < row:
    if grid[y][x % col] == '#':
        ans11 += 1
    x += 3
    y += 1

ans12 = sum(grid[i*1][i*3 % col] == '#' for i in range(row))

assert ans11 == ans12

print(ans11)
