import sys

example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split("\n")

with open("2024/py/day04/day04.txt") as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

m = []
p = ['.' for _ in range(len(data[0])+6)]
m.append(p)
m.append(p)
m.append(p)
for d in data:
    m.append([".", ".", "."] + list(d) + [".", ".", "."])
m.append(p)
m.append(p)
m.append(p)


comp = "MAS"
ans1 = 0
for y, r in enumerate(m):
    for x, c in enumerate(r):
        if c == 'X':
            tmp = []
            tmp.append(m[y][x+1]+m[y][x+2]+m[y][x+3])
            tmp.append(m[y][x-1]+m[y][x-2]+m[y][x-3])

            tmp.append(m[y+1][x]+m[y+2][x]+m[y+3][x])
            tmp.append(m[y-1][x]+m[y-2][x]+m[y-3][x])

            tmp.append(m[y+1][x+1]+m[y+2][x+2]+m[y+3][x+3])
            tmp.append(m[y-1][x-1]+m[y-2][x-2]+m[y-3][x-3])

            tmp.append(m[y+1][x-1]+m[y+2][x-2]+m[y+3][x-3])
            tmp.append(m[y-1][x+1]+m[y-2][x+2]+m[y-3][x+3])

            ans1 += tmp.count(comp)


print(ans1)
