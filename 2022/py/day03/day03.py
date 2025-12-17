import sys

example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")

with open('2022/py/day03/day03.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines


data = [[line[len(line)//2:],line[:len(line)//2]] for line in data]

ans1 = 0
for r1,r2 in data:
    s1 = set(r1)
    s2 = set(r2)
    intersect = list(s1.intersection(s2))[0]
    ans1 += ord(intersect)-65+27 if intersect.isupper() else ord(intersect)-96
    
print(ans1)


ans2 = 0
for i in range(len(data)//3):
    s1 = set(data[i*3+0][0]).union(data[i*3+0][1])
    s2 = set(data[i*3+1][0]).union(data[i*3+1][1])
    s3 = set(data[i*3+2][0]).union(data[i*3+2][1])
    intersect = list(s1.intersection(s2.intersection(s3)))[0]
    ans2 += ord(intersect)-65+27 if intersect.isupper() else ord(intersect)-96

print(ans2)