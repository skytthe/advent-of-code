import sys

example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".split()

with open('2023/py/day01/input.txt') as f:
    lines = f.readlines()

data = example
data = lines

sum = 0

for line in data:
    firstDigit = None
    lastDigit = None

    for ch in line:
        if ch.isdigit():
            if firstDigit == None:
                firstDigit = ch
            lastDigit = ch
    sum = sum + int(firstDigit+lastDigit)

print(sum)
