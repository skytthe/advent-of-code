from collections import defaultdict, Counter

example = """16,1,2,0,4,2,7,1,2,14""".split(",")

with open("2021/py/day07/day07.txt") as f:
    lines = f.read().split(",")

data = example
data = lines


data = list(map(int, data))

maxValue = max(data)
crabs = defaultdict(int,Counter(data))

minCost = maxValue * sum(crabs.values())
for p in range(maxValue+1):
    cost = 0

    for k,v in crabs.items():
        cost += v * abs(k-p)

    if cost < minCost:
        minCost = cost

print(minCost)
