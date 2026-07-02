import re
import numpy as np

example = """5 10 25""".splitlines()


with open('2016/py/day03/day03.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

print(data)

count = 0
for line in data:
    tmp = re.findall(r'\d+', line)
    tmp = list(map(int,tmp))
    if tmp[0] + tmp[1] > tmp[2] and tmp[0] + tmp[2] > tmp[1] and tmp[1] + tmp[2] > tmp[0]:
        count += 1

print(count)
