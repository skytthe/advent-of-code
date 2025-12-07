from collections import Counter
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

start1 = data[0].find("S")
beams1 = [{start1}]
splits = 0

for row in grid:
    newBeams = set()
    for b in beams1[-1]:
        if row[b] == "^":
            splits += 1
            newBeams.add(b-1)
            newBeams.add(b+1)
        else:
            newBeams.add(b)
    beams1.append(newBeams)

print(splits)


start2 = data[0].find("S")
beams2 = [Counter([start2])]

for i, row in enumerate(grid):
    newBeams2 = Counter()
    for b, count in beams2[-1].items():
        if row[b] == "^":
            newBeams2[b-1] += count
            newBeams2[b+1] += count
        else:
            newBeams2[b] += count
    beams2.append(newBeams2)

print(sum(beams2[-1].values()))
