import numpy as np
import matplotlib.pyplot as plt

example = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

with open("2021/py/day13/day13.txt") as f:
    lines = f.read()

data = example
data = lines

data = data.split("\n\n")

dots = np.array([line.split(",") for line in data[0].split("\n")], dtype=int)
folds =  [item.split("=") for item in [line.split()[-1] for line in data[1].split("\n")]]

width, height = np.max(dots, axis=0) + 1
grid = np.zeros((height, width), dtype=int)

for x,y in dots:
    grid[y,x] = 1

for stp, fold in enumerate(folds):
    dir, pos = fold
    pos = int(pos)

    if dir == "y":
        H, W = grid.shape

        top = grid[:pos, :]
        bottom = np.flip(grid[pos+1:, :], axis=0)

        h = max(top.shape[0], bottom.shape[0])
        newGrid = np.zeros((h, W), dtype=int)

        newGrid[-top.shape[0]:, :] += top
        newGrid[-bottom.shape[0]:, :] += bottom

    else:
        assert dir == "x"
        H, W = grid.shape

        left = grid[:, :pos]
        right = np.flip(grid[:, pos+1:], axis=1)

        w = max(left.shape[1], right.shape[1])
        newGrid = np.zeros((H, w), dtype=int)

        newGrid[:, -left.shape[1]:] += left
        newGrid[:, -right.shape[1]:] += right

    newGrid[newGrid >= 1] = 1

    if stp == 0:
        print(np.sum(newGrid[newGrid >= 1]))
        print()
    if stp == len(folds)-1:
        for line in newGrid:
            s = ""
            for n in line:
                s += "#" if n > 0 else " "
            print(s)
    grid = newGrid

    # plt.imshow(grid)
    # plt.xticks([])
    # plt.yticks([])
    # plt.title(f"Shape: {grid.shape}")
    # plt.show()
