from collections import Counter

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
beams = [Counter([start])]
splits = 0

for row in grid:
    newBeams = Counter()
    for b, count in beams[-1].items():
        if row[b] == "^":
            splits += 1
            newBeams[b-1] += count
            newBeams[b+1] += count
        else:
            newBeams[b] += count
    beams.append(newBeams)

print(splits)
print(sum(beams[-1].values()))
