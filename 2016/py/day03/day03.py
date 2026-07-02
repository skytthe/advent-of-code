import re
import numpy as np

example = """5 10 25""".splitlines()


with open('2016/py/day03/day03.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

count = 0
for line in data:
    tmp = re.findall(r'\d+', line)
    tmp = list(map(int,tmp))
    if tmp[0] + tmp[1] > tmp[2] and tmp[0] + tmp[2] > tmp[1] and tmp[1] + tmp[2] > tmp[0]:
        count += 1

print(count)


data2 = np.array([re.findall(r'\d+', line) for line in data],dtype=int).T.reshape(-1,3)

count2 = 0
for tmp in data2:
    if tmp[0] + tmp[1] > tmp[2] and tmp[0] + tmp[2] > tmp[1] and tmp[1] + tmp[2] > tmp[0]:
        count2 += 1

print(count2)
