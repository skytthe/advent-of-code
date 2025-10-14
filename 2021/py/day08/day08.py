from collections import Counter, defaultdict

example = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".split("\n")

with open("2021/py/day08/day08.txt") as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

data = [[part.split() for part in line.split(" | ")] for line in data]


right = Counter([len(item) for line in data for item in line[1]])
print(right[2] + right[3] + right[4] + right[7])

rightDisplay = [item[1] for item in data]
valueSets = [set(''.join(sorted(v)) for sublist in line for v in sublist) for line in data]
valueSets = [set(frozenset(v) for sublist in line for v in sublist) for line in data]

total = 0
for idx,i in enumerate(valueSets):
    lenDict = defaultdict(list)
    valueDict = {}

    for j in i:
        lenDict[len(j)].append(j)

    valueDict[lenDict[2][0]] = 1
    valueDict[lenDict[3][0]] = 7
    valueDict[lenDict[4][0]] = 4
    valueDict[lenDict[7][0]] = 8

    # 9
    for i,s in enumerate(lenDict[6]):
        if lenDict[4][0].issubset(s):
            valueDict[s] = 9
            lenDict[6].pop(i)
            break

    # 0
    for i,s in enumerate(lenDict[6]):
        if lenDict[3][0].issubset(s):
            valueDict[s] = 0
            lenDict[6].pop(i)
            break

    # 6
    valueDict[lenDict[6][0]] = 6

    # 3
    for i,s in enumerate(lenDict[5]):
        if lenDict[3][0].issubset(s):
            valueDict[s] = 3
            lenDict[5].pop(i)
            break
    # 5
    for i,s in enumerate(lenDict[5]):
        if s.issubset(lenDict[6][0]):
            valueDict[s] = 5
            lenDict[5].pop(i)
            break

    # 2
    valueDict[lenDict[5][0]] = 2

    res = ""
    for digit in rightDisplay[idx]:
        res += str(valueDict[frozenset(list(digit))])

    # print(res)

    total += int(res)

print(total)
