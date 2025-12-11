import sys
from collections import deque, defaultdict

example = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""".split("\n")

with open('2025/py/day11/day11.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines


graph = defaultdict(list)

for line in data:
    node, edges = line.split(": ")
    edges = edges.split()
    for e in edges:
        graph[node].append(e)

paths = 0
q = deque()
q.append("you")
while q:
    node = q.popleft()
    for e in graph[node]:
        if e == "out":
            paths += 1
        else:
            q.append(e)


print(paths)