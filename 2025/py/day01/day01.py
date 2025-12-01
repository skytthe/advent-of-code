import sys

example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".split("\n")

with open('2025/py/day01/day01.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

password = 0

dialPosistion = 50
for l in data:
    dir, n = l[0], int(l[1:])

    if dir =="L":
        dialPosistion -= n
    if dir =="R":
        dialPosistion += n

    dialPosistion = dialPosistion % 100
    if dialPosistion == 0:
        password += 1 

print(password)