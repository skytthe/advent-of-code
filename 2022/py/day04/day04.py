import sys
from pprint import pprint

example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split("\n")

with open('2022/py/day04/day04.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

data = [sorted([list(map(int, secs.split("-"))) for secs in line.split(",")], key=lambda x : (x[0],-x[1])) for line in data]

ans1 = 0
for p1, p2 in data:
    ans1 += 1 if p1[0] <= p2[0] and p1[1] >= p2[1] else 0
        
print(ans1)
