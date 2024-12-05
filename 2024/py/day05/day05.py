import sys
from collections import defaultdict

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

for a in (int(l[int(len(l)/2)]) for l in ll):
    ans1 += a

print(ans1)
