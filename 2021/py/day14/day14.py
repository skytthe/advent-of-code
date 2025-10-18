import numpy as np
from collections import defaultdict, Counter
from pprint import pprint

example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

with open("2021/py/day14/day14.txt") as f:
    lines = f.read()

data = example
data = lines

data = data.split("\n\n")


polymerTemplate = list(data[0])
pairInsertionRules = {i : o for i,o in (line.split(" -> ") for line in data[1].split("\n"))}

steps = 10
for i in range(steps):
    new = []
    for a,b in zip(polymerTemplate[:-1],polymerTemplate[1:]):
        new += [a] + [pairInsertionRules[a+b]]
    new.append(polymerTemplate[-1])
    polymerTemplate = new


scores = sorted(Counter(polymerTemplate).values(),reverse=True)
print(scores[0]-scores[-1])

