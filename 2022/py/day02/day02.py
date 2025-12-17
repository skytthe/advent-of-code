import sys

example = """A Y
B X
C Z""".split("\n")

with open('2022/py/day02/day02.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

data = [l.split() for l in data]

shapes = {"X" : 1,"Y" : 2,"Z" : 3}
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
outcomes = {
    "AX" : 3,
    "AY" : 6,
    "AZ" : 0,
    "BX" : 0,
    "BY" : 3,
    "BZ" : 6,
    "CX" : 6,
    "CY" : 0,
    "CZ" : 3,
}
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
strategy = {
    "AX" : "Z",
    "AY" : "X",
    "AZ" : "Y",
    "BX" : "X",
    "BY" : "Y",
    "BZ" : "Z",
    "CX" : "Y",
    "CY" : "Z",
    "CZ" : "X",
}

ans1 = 0
ans2 = 0
for p1,p2 in data:
    ans1 += shapes[p2] + outcomes[p1+p2]
    ans2 += shapes[strategy[p1+p2]] + outcomes[p1+strategy[p1+p2]]

print(ans1)
# print(ans2)
print(sum([shapes[strategy[p1+p2]] + outcomes[p1+strategy[p1+p2]] for p1,p2 in data]))
