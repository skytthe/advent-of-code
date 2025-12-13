import sys

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split("\n")

with open('2023/py/day03/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

height = len(data)
width = len(data[0])

schematic = [['.' for _ in range(width + 2)] for _ in range(height + 2)]

symbols = set()

for y, line in enumerate(data):
    for x, ch in enumerate(line):
        schematic[y+1][x+1] = ch
        if not (ch == "." or ch.isdigit()):
            symbols.add(ch)

sum = 0

for y, line in enumerate(schematic):
    number = ""
    for x, ch in enumerate(line):
        if ch.isdigit():
            number = number + ch
        if number != "" and (ch == "." or ch in symbols):
            tmp = schematic[y-1][x-len(number)-1:x+1]
            tmp += schematic[y][x - len(number)-1:x+1]
            tmp += schematic[y+1][x-len(number)-1:x+1]

            adjacent = any(k in symbols for k in tmp)

            if adjacent:
                sum += int(number)

            number = ""

print(sum)
