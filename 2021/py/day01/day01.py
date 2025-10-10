example = """199
200
208
210
200
207
240
269
260
263""".split("\n")

with open("2021/py/day01/day01.txt") as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

data = list(map(int, data))

print(sum(b > a for a,b in zip(data[:-1],data[1:])))

count = 0
for i in range(len(data)-3):
    if sum(data[i:i+3]) < sum(data[i+1:i+4]):
        count += 1
print(count)

