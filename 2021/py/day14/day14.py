import numpy as np
from collections import defaultdict, Counter
from pprint import pprint
from functools import cache

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

# scores = sorted(Counter(polymerTemplate).values(),reverse=True)
# print(scores[0]-scores[-1])


@cache
def constructPolymer(polymerTemplate : str, depth : int) -> Counter:
    if depth == 0:
        return Counter(polymerTemplate)
    elif len(polymerTemplate) == 2:
        tmp = polymerTemplate[0] + pairInsertionRules[polymerTemplate] + polymerTemplate[1]
        return constructPolymer(tmp, depth-1)
    else:
        count = constructPolymer(polymerTemplate[:2], depth) + constructPolymer(polymerTemplate[1:], depth)
        count[polymerTemplate[1]] -= 1
        return count


scores1 = sorted(constructPolymer(data[0],steps).values(),reverse=True)
print(scores1[0]-scores1[-1])

scores2 = sorted(constructPolymer(data[0],40).values(),reverse=True)
print(scores2[0]-scores2[-1])
