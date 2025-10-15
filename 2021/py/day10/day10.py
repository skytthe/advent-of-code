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

cost1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

cost2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


errors = []
scores = []
for line in data:
    stack = []
    flag = True
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
                flag = False
                break
    if flag:
        score = 0
        for ch in reversed(stack):
            try:
                score = score * 5 + cost2[chr(ord(ch)+1)]
            except:
                score = score * 5 + cost2[chr(ord(ch)+2)]
        scores.append(score)


total = sum([cost1[i] for i in errors])
print(total)

scores.sort()
print(scores[len(scores)//2])


# print(ord("{"))
# print(chr(ord("(")+1))
# print(chr(ord("[")+2))
# print(chr(ord("{")+2))
# print(chr(ord("<")+2))