import sys

example = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

with open('2025/py/day02/day02.txt') as f:
    lines = f.read()

data = example
data = lines

data = [list(map(int, i.split("-"))) for i in data.split(",")]

invalids1 = 0
invalids2 = 0
for rl,ru in data:
    for i in range(rl,ru+1):
        tmp = str(i)
        # part 1
        if len(tmp) % 2 == 0:
            if tmp[len(tmp)//2:] == tmp[:len(tmp)//2]:
                invalids1 += i
        # part 2
        for l in range(1,len(tmp)//2+1):
            pattern = tmp[:l]
            count = tmp.count(pattern)
            if l*count == len(tmp):
                invalids2 += i
                break

print(invalids1)
print(invalids2)
