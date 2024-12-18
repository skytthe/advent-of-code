import sys
import pprint
import queue

example = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""".split("\n")

with open('2024/py/day18/day18.txt') as f:
    # s = f.read().strip()
    s = [line.strip() for line in f.readlines()]

data = example
data = s

col = row = 7
gx = gy = 6
col = row = 71
gx = gy = 70


def findPath():
    x = y = 0
    pq = queue.PriorityQueue()
    pq.put((gx + gy, 0, x, y))
    visited = set()
    visited.add((x, y))

    adj4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while not pq.empty():
        h, cost, x, y, = pq.get()
        # print(f"{h} {cost}, {x}, {y}")
        if x == gx and y == gy:
            # print(cost)
            return cost
        for d in adj4:
            dx, dy = d
            nx = x+dx
            ny = y+dy
            if nx >= 0 and ny >= 0 and nx < row and ny < row:
                if grid[ny][nx] == '.':
                    if (nx, ny) not in visited:
                        pq.put((cost+1+((gx-nx)+(gy-ny)), cost+1, nx, ny))
                        visited.add((nx, ny))
    return None


for maxi in range(1024, len(data)):
    x = y = 0
    grid = [['.']*col for i in range(row)]
    # pprint.pp(grid)
    s = ""
    for i, l in enumerate(data):
        if i >= maxi:
            break
        ix, iy = map(int, l.split(','))
        s = f"{ix},{iy}"
        grid[iy][ix] = '#'
    if maxi == 1024:
        print(findPath())
    if findPath() == None:
        print(s)
        break
