import sys
import queue
import pprint


example = """
""".split("\n")

with open('2024/py/day16/day16.txt') as f:
    # s = f.read().strip()
    s = [line.strip() for line in f.readlines()]

data = example
data = s

grid = [list(x) for x in data]

row = len(grid)
col = len(grid[0])

x, y = next((j, i) for j in range(col)
            for i in range(row) if grid[i][j] == 'S')
dir = 0
gx, gy = next((j, i) for j in range(col)
              for i in range(row) if grid[i][j] == 'E')

adj4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# print(f", {x}, {y}, {dir}")
# print(f", {gx}, {gy}, {dir}")

grid[y][x] = '.'
grid[gy][gx] = '.'

pq = queue.PriorityQueue()

abc = frozenset([(x, y)])

pq.put((0, x, y, 0, abc))

visited = set()


sdf = []


mincost = -1
while not pq.empty():
    cost, x, y, dir, count = pq.get()
    visited.add((x, y, dir))
    bbb = count | frozenset([(x, y)])
    if mincost != -1 and mincost < cost:
        break
    # print(bbb)
    # print(f"{cost}, {x}, {y}, {dir}")
    if x == gx and y == gy:
        # print(f"cost {cost}")
        # print(f"cc {len(bbb)}")
        # print()
        if mincost == -1:
            mincost = cost
        if mincost == cost:
            sdf.append(bbb)
    dx, dy = adj4[dir]
    if grid[y+dy][x+dx] == '.':
        if (x+dx, y+dy, dir) not in visited:
            pq.put((cost+1, x+dx, y+dy, dir, bbb))
    dx, dy = adj4[(dir-1) % 4]
    if grid[y+dy][x+dx] == '.':
        if (x, y, (dir-1) % 4) not in visited:
            pq.put((cost+1000, x, y, (dir-1) % 4, bbb))
    dx, dy = adj4[(dir+1) % 4]
    if grid[y+dy][x+dx] == '.':
        if (x, y, (dir+1) % 4) not in visited:
            pq.put((cost+1000, x, y, (dir+1) % 4, bbb))


haha = frozenset()
for x in sdf:
    # print(f"sdf : {x}")
    haha = haha | x

print(f"part 1\n{mincost}")
print(f"part 2\n{len(haha)}")
# print(len(sdf))
