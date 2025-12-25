import sys

example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()

example2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".splitlines()

with open('2022/py/day09/day09.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = example2
data = lines

data = [[a,int(b)] for a,b in (line.split() for line in data)]

moves = {
    "U" : (0,1),
    "D" : (0,-1),
    "R" : (1,0),
    "L" : (-1,0),
}


def run(knots, data):

    rope = [[0,0] for _ in range(knots)]

    visited = set()
    visited.add((0,0))

    for dir, n in data:
        dx, dy = moves[dir]
        for _ in range(n):
            rope[0][0] += dx
            rope[0][1] += dy

            for knot in range(1,knots):
                if abs(rope[knot-1][0]-rope[knot][0]) > 1 and rope[knot-1][1] == rope[knot][1]:
                    rope[knot][0] = rope[knot-1][0] + (rope[knot][0] > rope[knot-1][0]) - (rope[knot][0] < rope[knot-1][0])
                elif abs(rope[knot-1][1]-rope[knot][1]) > 1 and rope[knot-1][0] == rope[knot][0]:
                    rope[knot][1] = rope[knot-1][1] + (rope[knot][1] > rope[knot-1][1]) - (rope[knot][1] < rope[knot-1][1])
                elif abs(rope[knot-1][0]-rope[knot][0]) > 1 and abs(rope[knot-1][1]-rope[knot][1]) == 1:
                    rope[knot][0] = rope[knot-1][0] + (rope[knot][0] > rope[knot-1][0]) - (rope[knot][0] < rope[knot-1][0])
                    rope[knot][1] = rope[knot-1][1]
                elif abs(rope[knot-1][0]-rope[knot][0]) == 1 and abs(rope[knot-1][1]-rope[knot][1]) > 1:
                    rope[knot][0] = rope[knot-1][0]
                    rope[knot][1] = rope[knot-1][1] + (rope[knot][1] > rope[knot-1][1]) - (rope[knot][1] < rope[knot-1][1])
                elif abs(rope[knot-1][0]-rope[knot][0]) > 1 and abs(rope[knot-1][1]-rope[knot][1]) > 1:
                    rope[knot][0] = rope[knot-1][0] + (rope[knot][0] > rope[knot-1][0]) - (rope[knot][0] < rope[knot-1][0])
                    rope[knot][1] = rope[knot-1][1] + (rope[knot][1] > rope[knot-1][1]) - (rope[knot][1] < rope[knot-1][1])
            
            visited.add((rope[-1][0],rope[-1][1]))

    return len(visited)

print(run(2, data))
print(run(10, data))
