
example = """3,4,3,1,2""".split(",")

with open("2021/py/day06/day06.txt") as f:
    lines = f.read().split(",")

data = example
data = lines

data = list(map(int, data))

days = 80
fishs = data
for i in range(days):
    new = []
    for fish in fishs:
        if fish == 0:
            new.append(6)
            new.append(8)
        else:
            new.append(fish-1)
    fishs = new

print(len(fishs))


