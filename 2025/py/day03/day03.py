import sys
from collections import Counter

example = """987654321111111
811111111111119
234234234234278
818181911112111""".split("\n")

with open('2025/py/day03/day03.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

ans = 0
for line in data:
    first = '0'
    last = '0'
    idx = None
    for n in  range(len(line)-1):
        if line[n] > first:
            first = line[n]
            idx = n
    for n in range(idx+1,len(line)):
        if line[n] > last:
            last = line[n]
    ans += int(first+last)

print(ans)