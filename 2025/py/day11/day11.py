import sys
from collections import deque, defaultdict
from functools import cache

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

example2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""".split("\n")

with open('2025/py/day11/day11.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = example2
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


@cache
def travelGraph(node, dac, fft):
    global graph
    sum = 0
    for e in graph[node]:
        if e == "out":
            if dac and fft:
                return 1
            else: 
                return 0
        else:
            if e == "dac":
                sum += travelGraph(e, True, fft)
            elif e == "fft":
                sum += travelGraph(e, dac, True)
            else:               
                sum += travelGraph(e, dac, fft)
    return sum

print(travelGraph("svr", False, False))