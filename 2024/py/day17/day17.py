import re

with open('2024/py/day17/day17.txt') as f:
    s = f.read().strip()

reg, prog = s.split("\n\n")

regA, regB, regC = map(int, re.findall(r"\d+", reg))
program = list(map(int, re.findall(r"\d+", prog)))


output = []

pointer = 0
while pointer < len(program):
    opcode = program[pointer]
    operand = program[pointer+1]

    comboOperand = operand
    if operand == 4:
        comboOperand = regA
    elif operand == 5:
        comboOperand = regB
    elif operand == 6:
        comboOperand = regC
    else:
        pass

    if opcode == 0:
        tmp = regA // (2**comboOperand)
        regA = int(tmp)
        pointer += 2
    if opcode == 1:
        tmp = regB ^ operand
        regB = tmp
        pointer += 2
    if opcode == 2:
        tmp = comboOperand % 8
        regB = tmp
        pointer += 2
    if opcode == 3:
        if regA == 0:
            pointer += 2
        else:
            pointer = operand
    if opcode == 4:
        tmp = regB ^ regC
        regB = tmp
        pointer += 2
    if opcode == 5:
        tmp = comboOperand % 8
        stmp = str(tmp)
        for s in stmp:
            output.append(s)
        pointer += 2
    if opcode == 6:
        tmp = regA // (2**comboOperand)
        regB = tmp
        pointer += 2
    if opcode == 7:
        tmp = regA // (2**comboOperand)
        regC = tmp
        pointer += 2

    if (len(output) > len(program)):
        break

print(",".join(map(str, output)))
