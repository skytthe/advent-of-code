
example = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".split("\n")

with open('2021/py/day02/day02.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines 

data = [x.split(" ") for x in data]


x,y,y2 = 0,0,0

for c,l in data:
    l = int(l)
    if c == "forward":
        x += l
        y2 += l*y
    if c == "up":
        y -= l
    if c == "down":
        y += l


print(x*y)
print(x*y2)