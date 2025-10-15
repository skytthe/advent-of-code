example = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split("\n")

with open("2021/py/day10/day10.txt") as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

cost = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

errors = []
for line in data:
    stack = []
    for ch in line:
        if ch in {'(','[','{','<',}:
            stack.append(ch)
        else:
            if ch == ')' and stack[-1] == '(':
                stack.pop()
            elif ch == ']' and stack[-1] == '[':
                stack.pop()
            elif ch == '}' and stack[-1] == '{':
                stack.pop()
            elif ch == '>' and stack[-1] == '<':
                stack.pop()
            else:
                errors.append(ch)
                break

total = sum([cost[i] for i in errors])
print(total)
