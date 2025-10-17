import numpy as np
from collections import defaultdict, Counter
from pprint import pprint

example = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split("\n")

with open("2021/py/day12/day12.txt") as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

graph = defaultdict(list)
for line in data:
    node1, node2 = line.split("-")
    graph[node1].append(node2)
    graph[node2].append(node1)

# pprint(graph)

paths = []

def findPaths(path):
    global paths
    if path[-1] == "end":
        paths.append(path)
        return 
    
    for next in graph[path[-1]]:
        newPath = path.copy()
        if next.isupper() or next not in newPath:
            newPath.append(next)
            findPaths(newPath)

findPaths(["start"])
print(len(paths))


paths = []

def findPaths(path, flag):
    global paths
    if path[-1] == "end":
        paths.append(path)
        return 
    
    for next in graph[path[-1]]:
        if next == "start":
            continue
        newPath = path.copy()
        if next.isupper() or next not in newPath:
        # if next.isupper() or Counter(newPath)[next] < 2:
            newPath.append(next)
            findPaths(newPath, flag)
        elif flag:   
            newPath.append(next)
            findPaths(newPath, False)

findPaths(["start"],True)
print(len(paths))
