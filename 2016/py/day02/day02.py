import numpy as np

example = """ULL
RRDDD
LURDL
UUUUD""".split()


with open('2016/py/day02/day02.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

data = [[ch for ch in line] for line in data]

keypad = [[3*i + j + 1 for j in range(3)] for i in range(3)]

moves = {"U" : np.array([0,-1],dtype=int),
         "D" : np.array([0,1],dtype=int),
         "L" : np.array([-1,0],dtype=int),
         "R" : np.array([1,0],dtype=int),}
pw = ""
pos = np.array([1,1])
for line in data:
    for move in line:
        tmp = pos + moves[move]
        if np.all((tmp >= 0) & (tmp <= 2)):
            pos = tmp
    pw += str(keypad[pos[1]][pos[0]])

print(pw)
