from pprint import pprint
import re
from collections import deque


example = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".split("\n")

with open('2025/py/day10/day10.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

goals = []
actions = []
jolts = []

for line in data:
    goal = re.findall(r"\[(.*?)\]", line)
    goals.append(goal[0])
    action = re.findall(r"\((.*?)\)", line)
    actions.append([list(map(int,line.split(","))) for line in action])
    jolt = re.findall(r"\{(.*?)\}", line)
    jolts.append(jolt[0])


def doAction(s,action):
    s = list(s)
    for i in action:
        idx = int(i)
        if s[idx] == ".":
            s[idx] = "#"
        elif s[idx] == "#":
            s[idx] = "."
        else:
            assert False
    return "".join(s)


ans1 = 0
for e, g in enumerate(goals):
    start = "."*len(g)
    found = None

    q = deque()
    q.append((1,start))
    while q:
        stp, tmp = q.popleft()
        for a in actions[e]:
            new = doAction(tmp, a)
            if new == g:
                found = stp
                break
            else:
                q.append((stp+1,new))
        if found != None:
            break
    
    ans1 += found

print(ans1)