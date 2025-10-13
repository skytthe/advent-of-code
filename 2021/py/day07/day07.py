from collections import defaultdict, Counter

example = """16,1,2,0,4,2,7,1,2,14""".split(",")

with open("2021/py/day07/day07.txt") as f:
    lines = f.read().split(",")

data = example
data = lines


data = list(map(int, data))

maxValue = max(data)
crabs = defaultdict(int,Counter(data))

minCost1 = maxValue * sum(crabs.values())
minCost2 = maxValue * int((sum(crabs.values())*(sum(crabs.values())+1))/2)

for p in range(maxValue+1):
    cost1 = 0
    cost2 = 0

    for k,v in crabs.items():
        cost1 += v * abs(k-p)
        t = abs(k-p)
        cost2 += v *int((t*(t+1))/2)

    minCost1 = min(minCost1, cost1)
    minCost2 = min(minCost2, cost2)

print(minCost1)
print(minCost2)
