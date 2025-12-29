import sys
from pprint import pprint
from dataclasses import dataclass, field
from typing import List, Optional

example = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

with open('2022/py/day11/day11.txt') as f:
    lines = f.read()

data = example
data = lines

data = [s.splitlines() for s in data.split("\n\n")]

@dataclass
class Monkey():
    id: int
    items: List[int] = field(default_factory=list)
    opr: str
    test: int
    ifTrue: int
    ifFalse: int
    

pprint(data)


