import sys
import queue

example = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".split("\n")

with open('2024/py/day20/day20.txt') as f:
    # s = f.read().strip()
    s = [line.strip() for line in f.readlines()]

data = example
data = s

grid = [list(x) for x in data]

row = len(grid)
col = len(grid[0])

x, y = next((j, i) for j in range(col)
            for i in range(row) if grid[i][j] == 'S')

gx, gy = next((j, i) for j in range(col)
              for i in range(row) if grid[i][j] == 'E')

grid[y][x] = '.'
grid[gy][gx] = '.'


for c in grid:
    print(*c)

print(f"x: {x}, y: {y}")
print(f"gx: {gx}, gy: {gy}")

adj4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def findPath(sx, sy, gx, gy, grid):
    pq = queue.PriorityQueue()
    pq.put((abs(gx-sx) + abs(gy-sx), 0, sx, sy))
    visited = set()
    visited.add((sx, sy))

    while not pq.empty():
        h, c, x, y, = pq.get()
        # print(f"{c}, {x}, {y}")
        if x == gx and y == gy:
            # print(c)
            return c
        for d in adj4:
            dx, dy = d
            nx = x+dx
            ny = y+dy
            if nx >= 0 and ny >= 0 and nx < row and ny < row:
                if grid[ny][nx] == '.':
                    if (nx, ny) not in visited:
                        pq.put((c+1+(abs(gx-nx)+abs(gy-ny)), c+1, nx, ny))
                        visited.add((nx, ny))
    return None


cost = findPath(x, y, gx, gy, grid)
print(f"cost> {cost}")

ans1 = 0

cheatTime = 100

for ny in range(1, row-1):
    # print(f"row: {ny}/{row-1}")
    for nx in range(1, col-1):
        if grid[ny][nx] != '#':
            continue
        grid[ny][nx] = '.'
        cc = findPath(x, y, gx, gy, grid)
        if cost >= (cc+cheatTime):
            ans1 += 1
        grid[ny][nx] = '#'

print(ans1)
