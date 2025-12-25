import sys

example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()

with open('2022/py/day09/day09.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

data = [[a,int(b)] for a,b in (line.split() for line in data)]

moves = {
    "U" : (0,1),
    "D" : (0,-1),
    "R" : (1,0),
    "L" : (-1,0),
}

Hx = 0
Hy = 0
Tx = 0
Ty = 0

visited = set()
visited.add((Tx,Ty))

for dir, n in data:
    dx, dy = moves[dir]
    for _ in range(n):
        Hx += dx
        Hy += dy

        if abs(Hx-Tx) > 1 and Hy == Ty:
            Tx = Hx + (Tx > Hx) - (Tx < Hx)
        if abs(Hy-Ty) > 1 and Hx == Tx:
            Ty = Hy + (Ty > Hy) - (Ty < Hy)
        if abs(Hx-Tx) > 1 and abs(Hy-Ty) == 1:
            Tx = Hx + (Tx > Hx) - (Tx < Hx)
            Ty = Hy
        if abs(Hx-Tx) == 1 and abs(Hy-Ty) > 1:
            Tx = Hx
            Ty = Hy + (Ty > Hy) - (Ty < Hy)
        
        visited.add((Tx,Ty))

print(len(visited))
