import sys
import pprint

example = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""".split("\n")

with open('2025/py/day07/day07.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

grid = [list(line) for line in data[1:]]

start = data[0].find("S")
beams = [{start}]
splits = 0

for row in grid:
    newBeams = set()
    for b in beams[-1]:
        if row[b] == "^":
            splits += 1
            newBeams.add(b-1)
            newBeams.add(b+1)
        else:
            newBeams.add(b)
    beams.append(newBeams)


print(splits)
