import sys

example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split("\n")

with open('2024/py/day07/day07.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

ans1 = 0


def calc(goal, input):
    if len(input) == 1:
        return (goal == input[0])
    else:
        i = input[0]
        tmpAdd = input[1:]
        tmpAdd[0] = tmpAdd[0] + i
        tmpMul = input[1:]
        tmpMul[0] = tmpMul[0] * i
        return calc(goal, tmpAdd) or calc(goal, tmpMul)


for l in data:
    goal, input = l.split(':')
    goal = int(goal)
    input = input.strip().split()
    input = [int(x) for x in input]
    if calc(goal, input):
        ans1 += goal


print(ans1)
