from pprint import pprint 
import math

example = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

with open('2025/py/day12/day12.txt') as f:
    lines = f.read()

data = example
data = lines

data = data.split("\n\n")

shapes = data[:-1]
regions = [[
    list(map(int,line.split(": ")[0].split("x"))), 
    list(map(int,line.split(": ")[1].split(" ")))] 
        for line in data[-1].split("\n")
]

shapeArea = [l.count("#") for l in shapes]

space = []
for r, s in regions:
    area = math.prod(r)
    tmp = sum([x*y for x,y in zip(s,shapeArea)])
    # print(f"{area} - {tmp} = {area-tmp}")
    space.append(area-tmp)

ans1 = sum([1 if i > 0 else 0 for i in space])
print(ans1)