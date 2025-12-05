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
segments = [s for s in segments.split()]
ingredients = [int(s) for s in ingredients.split()]

fresh = 0
for i in ingredients:
    for s in segments:
        l,u = s.split("-")
        if int(l)<=i<=int(u):
            fresh += 1
            break

print(fresh)