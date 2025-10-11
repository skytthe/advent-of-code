import numpy as np

example = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split("\n")

with open('2021/py/day03/day03.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

data = np.array([[int(i) for i in line] for line in data])

mean = np.mean(data, axis=0)
gamma = int(''.join(map(str, np.rint(mean).astype(int))),2)
epsilon = ~gamma & ((1 << len(mean)) - 1)

print(gamma*epsilon)

 