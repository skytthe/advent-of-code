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

data1 = np.array([[int(i) for i in line] for line in data])

mean = np.mean(data1, axis=0)
gamma = int(''.join(map(str, np.rint(mean).astype(int))),2)
epsilon = ~gamma & ((1 << len(mean)) - 1)

print(gamma*epsilon)


data = data1.copy()

for idx in range(len(data[0])):
    ones = np.sum(data[:,idx])
    zeros = data.shape[0] - ones

    most_common_value = 1 if ones >= zeros else 0

    new = []
    for row in data:
        if row[idx] == most_common_value:
            new.append(row)
    
    data = np.array(new)
    if data.shape[0] == 1:
        break
oxygen = int(''.join(map(str,data[0])),2)


data = data1.copy()

for idx in range(len(data[0])):
    ones = np.sum(data[:,idx])
    zeros = data.shape[0] - ones

    least_common_value = 0 if ones >= zeros else 1

    new = []
    for row in data:
        if row[idx] == least_common_value:
            new.append(row)
    
    data = np.array(new)
    if data.shape[0] == 1:
        break
co2 = int(''.join(map(str,data[0])),2)


print(oxygen*co2)
