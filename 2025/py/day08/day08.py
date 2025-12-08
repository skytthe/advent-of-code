import numpy as np
import networkx as nx

example = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""".split("\n")

with open('2025/py/day08/day08.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

grid = np.array([list(map(int, line.split(","))) for line in data])

distances = []
for i in range(grid.shape[0]-1):
    for j in range(i+1,grid.shape[0]):
        d = np.linalg.norm(grid[i]-grid[j])
        distances.append((d, grid[i], grid[j]))

distances.sort(key=(lambda x : x[0]))

G = nx.Graph()
for point in grid:
    G.add_node(tuple(point))

for d,n1,n2 in distances[:1000]:
    G.add_edge(tuple(n1),tuple(n2))

cc = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
print(np.array(cc[:3]).prod())

for d,n1,n2 in distances[1000:10000]:
    G.add_edge(tuple(n1),tuple(n2))
    cc = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    if len(cc) == 1:
        print(n1[0]*n2[0])
        break
