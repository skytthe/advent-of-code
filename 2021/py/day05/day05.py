import numpy as np

example = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split("\n")

with open('2021/py/day05/day05.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

data = [list(map(int,line.replace(" -> ",",").split(","))) for line in data]

maxValue = max(max(line) for line in data) + 1

grid1 = np.zeros((maxValue,maxValue), dtype=int)
grid2 = np.zeros((maxValue,maxValue), dtype=int)

for x1,y1,x2,y2 in data:
    if x1 == x2:
        y1,y2 = sorted([y1,y2])
        grid1[y1:y2+1,x1] += 1
        grid2[y1:y2+1,x1] += 1
    elif y1 == y2:
        x1,x2 = sorted([x1,x2])
        grid1[y1,x1:x2+1] += 1
        grid2[y1,x1:x2+1] += 1
    else:
        assert abs(x2-x1) == abs(y2-y1)

        if x2 < x1:
            x1,y1,x2,y2 = x2,y2,x1,y1

        for i in range(x2-x1+1):
            if y1 < y2:
                grid2[y1+i,x1+i] += 1
            else:
                grid2[y1-i,x1+i] += 1


print(np.sum(grid1 > 1))
print(np.sum(grid2 > 1))


