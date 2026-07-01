import numpy as np

example = """R2, L3"""
example1 = """R2, R2, R2"""
example2 = """R5, L5, R5, R3"""

with open('2016/py/day01/day01.txt') as f:
    lines = f.read()

data = example2
data = lines

data = data.split(", ")
data = [[n[0],int(str(n[1:]))] for n in data]

headings = np.array([[1,0],[0,1],[-1,0],[0,-1]])
pos = np.array([0,0])
heading = 0
for dir,n in data:
    if dir == "R":
        heading = (heading + 1) % 4
    elif dir == "L":
        heading = (heading - 1) % 4
    pos = pos + headings[heading]*n

print(np.sum(abs(pos)))
