import sys

example = """2333133121414131402""".split("\n")

with open('2024/py/day09/day09.txt') as f:
    lines = [line.strip() for line in f.readlines()]


example = [int(x) for x in example[0]]
lines = [int(x) for x in lines[0]]

print(example)
print(sum(example))
print(len(example))
print()

print(sum(lines))
print(len(lines))


def printMem(mem):
    s = ""
    for m in mem:
        if m == -1:
            s += '.'
        else:
            s += str(m)
    print(s)


data = example
data = lines

m = [-1] * sum(data)

id = 0
idx = 0
for i, d in enumerate(data):
    if i % 2 == 0:
        m[idx:(idx+d)] = [id] * d
        idx += d
        id += 1
    else:
        idx += d

i1 = 0
i2 = len(m)-1
# printMem(m)
while True:
    while (m[i1] != -1):
        i1 += 1
    if i1 >= i2:
        break
    m[i1], m[i2] = m[i2], m[i1]
    while (m[i2] == -1):
        i2 -= 1

    # printMem(m)

ans1 = 0
for i, e in enumerate(m):
    if e != -1:
        ans1 += i*e

print(ans1)
