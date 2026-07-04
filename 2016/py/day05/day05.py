import hashlib

example = """abc"""

with open('2016/py/day05/day05.txt') as f:
    lines = f.read()

data = example
data = lines

pw = ""
idx = 0
while len(pw) < 8:
    tmp = hashlib.md5((data + str(idx)).encode()).hexdigest()
    idx += 1
    if tmp[:5] == "00000":
        pw = pw + tmp[5]


print(pw)