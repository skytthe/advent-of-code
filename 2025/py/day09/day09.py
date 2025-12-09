import sys

example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".split("\n")

with open('2025/py/day09/day09.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

data = [list(map(int, line.split(","))) for line in data]

biggest = 0
for i in range(len(data)-1):
    for j in range(i,len(data)):
        area = abs(data[i][0]-data[j][0]+1)*abs(data[i][1]-data[j][1]+1)
        if area > biggest:
            biggest = area

print(biggest)