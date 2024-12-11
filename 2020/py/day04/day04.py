
import sys
import re

example = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""".strip()

with open('2020/py/day04/day04.txt') as f:
    s = f.read().strip()
    # s = [line.strip() for line in f.readlines()]

data = example
data = s

data = [x.split() for x in data.split("\n\n")]

passports = [{k: v for k, v in (pair.split(':')
                                for pair in x) if k != "cid"} for x in data]

keywords = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}

ans11 = 0
for p in passports:
    if keywords == set(p.keys()):
        ans11 += 1

ans12 = sum(keywords == set(p.keys()) for p in passports)

assert ans11 == ans12

print(ans11)

# part 2

ans2 = 0
for p in passports:
    if keywords == set(p.keys()):
        if ((1920 <= int(p["byr"]) <= 2002) and
                (2010 <= int(p["iyr"]) <= 2020) and
                (2020 <= int(p["eyr"]) <= 2030) and
                ((p["hgt"][-2:] == "cm" and (150 <= int(p["hgt"][:-2]) <= 193)) or (p["hgt"][-2:] == "in" and (59 <= int(p["hgt"][:-2]) <= 76))) and
                (re.fullmatch(r"#([a-f]|\d){6}", p["hcl"])) and
                (p["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}) and
                (re.fullmatch(r"\d{9}", p["pid"]))):

            ans2 += 1

print(ans2)
