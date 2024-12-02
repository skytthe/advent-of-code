import sys

example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".split("\n")

with open('2024/py/day02/day02.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

ans1 = 0
for d in data:
    l = d.split()
    l = [int(x) for x in l]
    
    increasing = True
    decreasing = True
    differ = True
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            decreasing = False
        elif l[i] > l[i+1]:
            increasing = False
        else:
            decreasing = False
            increasing = False
        if abs(l[i] - l[i+1]) > 3 or abs(l[i] - l[i+1]) < 1:
            differ = False
    
    if (increasing or decreasing) and differ:
        ans1 = ans1 + 1

print(ans1)
        
        