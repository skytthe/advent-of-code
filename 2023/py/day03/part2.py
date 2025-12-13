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

example2 = """..........
..........
..........
....*.....
.234.123..
..........
..........""".split("\n")

with open('2023/py/day03/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = example2
data = lines

height = len(data)
width = len(data[0])

schematic = [['.' for _ in range(width + 2)] for _ in range(height + 2)]

for y, line in enumerate(data):
    for x, ch in enumerate(line):
        schematic[y+1][x+1] = ch

sum = 0

for y, line in enumerate(schematic):
    for x, ch in enumerate(line):
        if ch == "*":
            gears = []

            # above
            if schematic[y-1][x].isdigit():
                number = schematic[y-1][x]
                idx = 1
                while schematic[y-1][x+idx].isdigit():
                    number += schematic[y-1][x+idx]
                    idx += 1
                idx = 1
                while schematic[y-1][x-idx].isdigit():
                    number = schematic[y-1][x-idx] + number
                    idx += 1
                gears.append(int(number))
            else:
                if schematic[y-1][x-1].isdigit():
                    number = schematic[y-1][x-1]
                    idx = 1
                    while schematic[y-1][x-idx-1].isdigit():
                        number = schematic[y-1][x-idx-1] + number
                        idx += 1
                    gears.append(int(number))
                if schematic[y-1][x+1].isdigit():
                    number = schematic[y-1][x+1]
                    idx = 1
                    while schematic[y-1][x+idx+1].isdigit():
                        number += schematic[y-1][x+idx+1]
                        idx += 1
                    gears.append(int(number))
            # left
            if schematic[y][x-1].isdigit():
                number = schematic[y][x-1]
                idx = 1
                while schematic[y][x-idx-1].isdigit():
                    number = schematic[y][x-idx-1] + number
                    idx += 1
                gears.append(int(number))
            # right
            if schematic[y][x+1].isdigit():
                number = schematic[y][x+1]
                idx = 1
                while schematic[y][x+idx+1].isdigit():
                    number = number + schematic[y][x+idx+1]
                    idx += 1
                gears.append(int(number))
            # below
            if schematic[y+1][x].isdigit():
                number = schematic[y+1][x]
                idx = 1
                while schematic[y+1][x+idx].isdigit():
                    number += schematic[y+1][x+idx]
                    idx += 1
                idx = 1
                while schematic[y+1][x-idx].isdigit():
                    number = schematic[y+1][x-idx] + number
                    idx += 1
                gears.append(int(number))
            else:
                if schematic[y+1][x-1].isdigit():
                    number = schematic[y+1][x-1]
                    idx = 1
                    while schematic[y+1][x-idx-1].isdigit():
                        number = schematic[y+1][x-idx-1] + number
                        idx += 1
                    gears.append(int(number))
                if schematic[y+1][x+1].isdigit():
                    number = schematic[y+1][x+1]
                    idx = 1
                    while schematic[y+1][x+idx+1].isdigit():
                        number += schematic[y+1][x+idx+1]
                        idx += 1
                    gears.append(int(number))

            if len(gears) == 2:
                sum += gears[0] * gears[1]

print(sum)
