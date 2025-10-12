import numpy as np

example = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split("\n\n")

with open('2021/py/day04/day04.txt') as f:
    lines = f.read()

data = example
data = lines.split("\n\n")

numbers = list(map(int, data[0].split(',')))

boards = []

for board in data[1:]:
    new = np.array([[int(n) for n in line.split()] for line in board.strip().split("\n")])
    boards.append(new)

firstWinnerBoard = None
firstWinnerNumber = None

lastWinnerBoard = None
lastWinnerNumber = None

for number in numbers:
    l = []
    for i,board in enumerate(boards):
        board[board == number] = -1

        if np.any(np.sum(board, axis=0) == -5) or np.any(np.sum(board, axis=1) == -5):
            if firstWinnerNumber == None:
                firstWinnerBoard = board
                firstWinnerNumber = number

            lastWinnerBoard = board
            lastWinnerNumber = number
            
            l.append(i)

    for i in reversed(l):
        boards.pop(i)

firstWinnerBoard[firstWinnerBoard == -1] = 0
print(np.sum(firstWinnerBoard)*firstWinnerNumber)

lastWinnerBoard[lastWinnerBoard == -1] = 0
print(np.sum(lastWinnerBoard)*lastWinnerNumber)
