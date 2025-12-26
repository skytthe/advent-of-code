import sys

example = """noop
addx 3
addx -5""".splitlines()

example2 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()


with open('2022/py/day10/day10.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = example2
data = lines

X = 1   
cycles = 0

hist = []

for cmd in data:
    if cmd == "noop":
        hist.append(X)
        pass
    else:
        n = int(cmd.split()[1])
        hist.append(X)
        hist.append(X)
        X += n


ans1 = 0
idx = 20
while idx < len(hist):
    ans1 += hist[idx-1] * idx
    idx += 40

print(ans1)


grid = [[" "]*40 for _ in range(6)]
for i in range(240):
    x = i % 40
    y = i // 40
    if x-1 <= hist[i] <= x+1:
        grid[y][x] = "#"

print("\n".join(["".join(line) for line in grid]))