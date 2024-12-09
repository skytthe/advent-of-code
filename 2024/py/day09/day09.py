import sys

example = """2333133121414131402""".split("\n")

with open('2024/py/day09/day09.txt') as f:
    lines = [line.strip() for line in f.readlines()]


example = [int(x) for x in example[0]]
lines = [int(x) for x in lines[0]]


def printMem(mem):
    s = ""
    for m in mem:
        if m == -1:
            s += '.'
        else:
            s += str(m)
    print(s)


def printMem2(mem):
    s = ""
    for m in mem:
        if m[1] == -1:
            s += '.' * m[0]
        else:
            s += str(m[1]) * m[0]
    print(s)


data = example
data = lines

m1 = [-1] * sum(data)
m2 = []

id = 0
idx = 0
for i, d in enumerate(data):
    if i % 2 == 0:
        m1[idx:(idx+d)] = [id] * d
        idx += d
        m2.append([d, id])
        id += 1
    else:
        idx += d
        m2.append([d, -1])


i1 = 0
i2 = len(m1)-1
# printMem(m1)
while True:
    while (m1[i1] != -1):
        i1 += 1
    if i1 >= i2:
        break
    m1[i1], m1[i2] = m1[i2], m1[i1]
    while (m1[i2] == -1):
        i2 -= 1

    # printMem(m1)

ans1 = 0
for i, e in enumerate(m1):
    if e != -1:
        ans1 += i*e

print(ans1)

# printMem2(m2)
for i in reversed(range(len(m2))):
    if m2[i][1] == -1:
        continue
    for j in range(i):
        if m2[j][1] == -1:
            if m2[j][0] == m2[i][0]:
                m2[j], m2[i] = m2[i], m2[j]

                # printMem2(m2)
                break
            elif m2[j][0] > m2[i][0]:
                tmp = m2[i]
                m2[i] = [m2[i][0], -1]
                padding = [(m2[j][0]-m2[i][0]), -1]
                m2[j] = tmp
                m2.insert((j+1), padding)

                # printMem2(m2)
                break

ans2 = 0
itr = 0
for e in m2:
    for j in range(e[0]):
        if e[1] != -1:
            ans2 += itr*e[1]
        itr += 1

print(ans2)
