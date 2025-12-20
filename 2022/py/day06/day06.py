example = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
example1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
example2 = "nppdvjthqldpwncqszvftbrmjlhg"
example3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
example4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

with open('2022/py/day06/day06.txt') as f:
    lines = f.read()

data = example
data = lines


ans1 = None
for i in range(len(data)-4):
    if len(set(data[i:i+4])) == 4:
        ans1 = i+4
        break

assert ans1 != None
print(ans1)