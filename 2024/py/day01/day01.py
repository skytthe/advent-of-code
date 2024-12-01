import sys

example = """3   4
4   3
2   5
1   3
3   9
3   3""".split("\n")

with open('2024/py/day01/day01.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

left = []
right = []

for l in data:
    a, b = l.split("   ")
    left.append(int(a))
    right.append(int(b))

left.sort()
right.sort()

sum = 0
for i in range(len(left)):
    sum += abs(left[i] - right[i])

print("Part 1:")
print(sum)

sum2 = 0
for e in left:
    tmp = right.count(e)
    sum2 += tmp * e

print("Part 2:")
print(sum2)
