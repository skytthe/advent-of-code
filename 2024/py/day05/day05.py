import sys
from collections import defaultdict
from functools import cmp_to_key

example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".strip().split("\n")

with open('2024/py/day05/day05.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

ans1 = 0
ans2 = 0

pairs = defaultdict(list)
ll = []
ee = []

for l in data:
    if l.count('|') > 0:
        a, b = l.split('|')
        pairs[a].append(b)

    if l.count(',') > 0:
        tmp = l.split(',')
        s = set()
        flag = True
        for e in tmp:
            for x in pairs[e]:
                if x in s:
                    flag = False
            s.add(e)

        if flag:
            ll.append(tmp)
        else:
            ee.append(tmp)


def newcompare(a, b):
    if b in pairs[a]:
        return -1
    elif a in pairs[b]:
        return 1
    else:
        return 0


sorted_ee = []
for e in ee:
    sorted_ee.append(sorted(e, key=cmp_to_key(newcompare)))
    print(e)


for a in (int(l[int(len(l)/2)]) for l in ll):
    ans1 += a

for a in (int(l[int(len(l)/2)]) for l in sorted_ee):
    ans2 += a

print(ans1)
print(ans2)
