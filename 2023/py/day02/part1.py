import sys

example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split("\n")

with open('2023/py/day02/input.txt') as f:
    lines = f.readlines()

games = example
games = lines

bag = {"red": 12, "green": 13, "blue": 14}

l = list(range(1, len(games) + 1))

for idx, game in enumerate(games):
    turns = game.split(":")[1].split(";")
    for turn in turns:
        draws = turn.split(",")
        for draw in draws:
            tmp = draw.strip().split(" ")
            number = tmp[0]
            color = tmp[1]
            if int(number) > bag[color]:
                l[idx] = 0

print(sum(l))
