import numpy as np

example = """R2, L3"""
example1 = """R2, R2, R2"""
example2 = """R5, L5, R5, R3"""
example3 = """R8, R4, R4, R8"""

with open('2016/py/day01/day01.txt') as f:
    lines = f.read()

data = example3
data = lines

data = data.split(", ")
data = [[n[0],int(str(n[1:]))] for n in data]

headings = np.array([[1,0],[0,1],[-1,0],[0,-1]])
pos = np.zeros(2,dtype=int)
heading = 0
ans2 = None
visited = set()
for dir,n in data:
    if dir == "R":
        heading = (heading + 1) % 4
    elif dir == "L":
        heading = (heading - 1) % 4

    for _ in range(n):
        pos = pos + headings[heading]
        if tuple(pos.tolist()) in visited and ans2 is None:
            ans2 = pos
        else:
            visited.add(tuple(pos.tolist()))

print(np.sum(abs(pos)))

print(np.sum(abs(ans2)))
