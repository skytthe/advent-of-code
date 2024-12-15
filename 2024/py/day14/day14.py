import sys
import re
import pprint
from PIL import Image

example = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".split("\n")


# example = """p=2,4 v=2,-3""".split("\n")

with open('2024/py/day14/day14.txt') as f:
    s = [line.strip() for line in f.readlines()]

data = example
row = 7
col = 11
data = s
row = 103
col = 101


robots = [[int(num) for num in re.findall(r"-?\d+", x)] for x in data]

# print(robots)

grid = [[0 for x in range(col)]for y in range(row)]

s = 100

grid = [[0 for x in range(col)]for y in range(row)]
for r in robots:
    x = (r[0] + s * r[2]) % col
    y = (r[1] + s * r[3]) % row
    grid[y][x] += 1
# pprint.pp(grid)
# print()


q1 = [row[:col//2] for row in grid[:row//2]]
q2 = [row[col//2+1:] for row in grid[:row//2]]
q3 = [row[:col//2] for row in grid[row//2+1:]]
q4 = [row[col//2+1:] for row in grid[row//2+1:]]


# pprint.pprint(q1)
# pprint.pprint(q2)
# pprint.pprint(q3)
# pprint.pprint(q4)


ans1 = sum(sum(row) for row in q1) * sum(sum(row) for row in q2) * \
    sum(sum(row) for row in q3) * sum(sum(row) for row in q4)


print(ans1)


def grid_to_image(grid, s, cell_size=1):
    rows = len(grid)
    cols = len(grid[0])

    img = Image.new('L', (cols * cell_size, rows * cell_size), color=255)
    pixels = img.load()

    for row in range(rows):
        for col in range(cols):
            color = 0 if grid[row][col] == 0 else 255
            for x in range(cell_size):
                for y in range(cell_size):
                    pixels[col * cell_size + x, row * cell_size + y] = color

    output_path = f"image/img{s}.png"
    img.save(output_path)


s = 0
qq = (float('inf'), -1)
for s in range(col*row):
    grid = [[0 for x in range(col)]for y in range(row)]
    for r in robots:
        x = (r[0] + s * r[2]) % col
        y = (r[1] + s * r[3]) % row
        grid[y][x] += 1
    # these images have much less randomness
    # see image 7051, repeat agian in image 17454
    if (s-47) % 103 == 0 or (s-82) % 101 == 0:
        pass
        # grid_to_image(grid, s)
    flag = True
    for y in range(row):
        for x in range(col):
            if grid[y][x] > 1:
                flag = False
    if flag:
        print(f"flag> {s}")

    q1 = [row[:col//2] for row in grid[:row//2]]
    q2 = [row[col//2+1:] for row in grid[:row//2]]
    q3 = [row[:col//2] for row in grid[row//2+1:]]
    q4 = [row[col//2+1:] for row in grid[row//2+1:]]

    # pprint.pprint(q1)
    # pprint.pprint(q2)
    # pprint.pprint(q3)
    # pprint.pprint(q4)

    qsum = sum(sum(row) for row in q1) * sum(sum(row) for row in q2) * \
        sum(sum(row) for row in q3) * sum(sum(row) for row in q4)

    if qsum < qq[0]:
        qq = (qsum, s)


print(qq)
