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


pw2 = " " * 8
idx = 0
flags = [True]*8
while any(flags):
    tmp = hashlib.md5((data + str(idx)).encode()).hexdigest()
    idx += 1
    if tmp[:5] == "00000" and tmp[5].isdigit():
        i = int(tmp[5])
        if 0 <= i < 8 and flags[i]:
            pw2 = pw2[:i] + tmp[6] + pw2[i+1:]
            # print(pw2)
            flags[i] = False


print(pw2)