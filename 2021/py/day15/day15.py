import heapq

example = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".split("\n")

with open("2021/py/day15/day15.txt") as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

grid = [list(map(int, line)) for line in data]
R = len(grid)
C = len(grid[0])
grid2 = [[0]*C*5 for _ in range(R*5)]
for yy in range(5):
    for xx in range(5):
        for y in range(R):
            for x in range(C):
                grid2[yy*R+y][xx*C+x] = (grid[y][x] + yy + xx - 1) % 9 + 1

def fincPath(grid):
    R = len(grid)
    C = len(grid[0])

    moves = ((1,0),(-1,0),(0,1),(0,-1))

    start = (0,0)
    goal = (C-1,R-1)

    visited = set()

    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, xy = heapq.heappop(q)
        
        if xy in visited:
            continue
        visited.add(xy)

        if xy == goal:
            return cost

        x,y = xy
        for dx,dy in moves:
            nx,ny = x+dx, y+dy
            if (nx,ny) not in visited and 0 <= nx < C and 0 <= ny < R:
                heapq.heappush(q, (cost+grid[ny][nx], (nx,ny)))


print(fincPath(grid))
print(fincPath(grid2))