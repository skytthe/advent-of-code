import re
import numpy as np
from collections import defaultdict, Counter

example = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]""".splitlines()

example = """qzmt-zixmtkozy-ivhz-343[decoy]""".splitlines()

with open('2016/py/day04/day04.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines


ans = 0
ans2 = 0
for line in data:
    first, last = line.rsplit("-",1)
    id = int(re.search(r"\d+", last).group())
    cs = last[last.index("[")+1:last.index("]")]

    count = [[n, ch] for ch, n in Counter(first.replace("-","")).items()]

    res = sorted(count, key=lambda x : (-x[0],x[1]))
    top5 = "".join(np.array(res)[:5, 1])

    if top5 == cs:
        ans += id

    decoded = ""
    for ch in first:
        if ch == "-":
            decoded += " "
            continue

        decoded += chr((((ord(ch) - 97)+id)%26)+97)

        if decoded == "northpole object storage":
            ans2 = id

print(ans)
print(ans2)

