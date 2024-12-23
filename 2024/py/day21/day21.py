import networkx as nx
import sys
import pprint
import queue
import itertools


example1 = """029A""".split("\n")

example2 = """029A
980A
179A
456A
379A""".split("\n")

with open('2024/py/day21/day21.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example1
data = example2
data = lines

codes = [list(x) for x in data]


keypadGridString = \
    "#####\n" \
    "#789#\n" \
    "#456#\n" \
    "#123#\n" \
    "##0A#\n" \
    "#####" \

arrowpadGridString = \
    "#####\n" \
    "##^A#\n" \
    "#<v>#\n" \
    "#####" \

keypadGrid = [list(x) for x in keypadGridString.split()]
arrowpadGrid = [list(x) for x in arrowpadGridString.split()]

adj22 = [(0, -2, '^^'),  (-2, 0, '<<'), (0, 2, 'vv'), (2, 0, '>>')]

adj4 = [(0, -1, '^'), (1, 0, '>'),  (-1, 0, '<'), (0, 1, 'v')]
adj4Cmd = {(1, 0): '>',
           (0, 1): '^',
           (-1, 0): '<',
           (0, -1): 'v'}


def findPaths(grid, steps):
    row = len(grid)
    col = len(grid[0])
    all_paths = dict()
    for y in range(row):
        for x in range(col):
            ch = grid[y][x]
            if ch != '#':
                paths = dict()
                paths[ch] = ['A']
                seen = set()
                seen.add(ch)
                q = queue.Queue()
                q.put((x, y, []))
                while not q.empty():
                    cx, cy, path = q.get()
                    for dx, dy, cmd in steps:
                        nx, ny = cx+dx, cy+dy
                        if 0 <= nx < col and 0 <= ny < row:
                            nch = grid[ny][nx]
                            if nch != '#' and nch not in seen:
                                seen.add(nch)
                                np = path+list(cmd)
                                paths[nch] = np + ['A']
                                q.put((nx, ny, np))
                all_paths[ch] = paths
    return all_paths


# arrowpadPaths = findPaths(arrowpadGrid)
# pprint.pp(arrowpadPaths)

# keypadPaths = findPaths(keypadGrid)
# pprint.pp(keypadPaths)

ans1 = 0

adj22 = [(0, -2, '^^'),  (-2, 0, '<<'), (0, 2, 'vv'), (2, 0, '>>')]

adj4 = [(0, -1, '^'), (1, 0, '>'),  (-1, 0, '<'), (0, 1, 'v')]


for code in codes:
    min = 1000000
    print(code)
    for perm in itertools.permutations(adj22+adj4):
        stp = list(perm)
        arrowpadPaths = findPaths(arrowpadGrid, stp)
        keypadPaths = findPaths(keypadGrid, stp)

        robot1 = []
        robot2 = []
        robot3 = []
        prev1 = 'A'
        prev2 = 'A'
        prev3 = 'A'
        for char in code:
            # print(f"  {keypadPaths[prev1][char]}")
            for i in keypadPaths[prev1][char]:
                robot1.append(i)
                # print(f"    {arrowpadPaths[prev2][i]}")
                for j in arrowpadPaths[prev2][i]:
                    robot2.append(j)
                    # print(f"      {arrowpadPaths[prev3][j]}")
                    for k in arrowpadPaths[prev3][j]:
                        robot3.append(k)
                    prev3 = j
                prev2 = i
            prev1 = char
        # print(f"{''.join(code)}: {len(robot3)} * {(int(''.join(code)[:-1]))}")
        # print(*robot3, sep='')
        # print(f"   {len(robot3)}")
        if len(robot3) < min:
            min = len(robot3)
    ans1 += min * int(''.join(code)[:-1])

print(ans1)
