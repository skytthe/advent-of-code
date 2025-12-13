import sys

example = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split()

with open('2023/py/day01/input.txt') as f:
    lines = f.readlines()

data = example
data = lines

numbers = ["one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]

sum = 0

for line in data:
    firstDigit = None
    lastDigit = None

    for i, ch in enumerate(line):
        digit = None

        for j, num in enumerate(numbers):
            if line[i:].startswith(num):
                digit = str(j+1)

        if ch.isdigit():
            digit = ch

        if digit != None:
            if firstDigit == None:
                firstDigit = digit
            lastDigit = digit

    sum = sum + int(firstDigit+lastDigit)

print(sum)
