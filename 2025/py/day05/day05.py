import sys

example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

with open('2025/py/day05/day05.txt') as f:
    lines = f.read()

data = example
data = lines

segments, ingredients = data.split("\n\n")
segments = [list(map(int,s.split("-"))) for s in segments.split()]
ingredients = [int(s) for s in ingredients.split()]

fresh1 = 0
for i in ingredients:
    for l,u in segments:
        if int(l)<=i<=int(u):
            fresh1 += 1
            break

print(fresh1)


segments.sort(key=lambda x : x[0])

fresh2 = 0
index = 0
for l,u in segments:
    if l > index:
        index = l
    if u >= index:
        fresh2 += u-index+1
        index = u+1

print(fresh2)
