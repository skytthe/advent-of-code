import sys
import networkx as nx
import pprint
import itertools

example = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""".split("\n")

with open('2024/py/day23/day23.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

G = nx.Graph()

tnodes = set()

for l in data:
    a, b = l.split('-')
    G.add_node(a)
    G.add_node(b)
    G.add_edge(a, b)
    if a[0] == 't':
        tnodes.add(a)
    if b[0] == 't':
        tnodes.add(b)

cc = set()
for node in tnodes:
    neighbors = list(G.neighbors(node))
    for pair in itertools.combinations(neighbors, 2):
        if G.has_edge(pair[0], pair[1]):
            tmp = [node] + list(pair)
            tmp.sort()
            cc.add(tuple(tmp))


print(len(cc))
