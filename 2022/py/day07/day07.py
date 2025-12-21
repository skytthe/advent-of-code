from dataclasses import dataclass, field
from collections import defaultdict, deque
from typing import List, Optional

example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()

with open('2022/py/day07/day07.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
# data = lines

data = deque(data)

@dataclass
class File():
    name: str
    size: int

@dataclass
class Folder:
    name: str
    parent: Optional[Folder] = None
    files: List[File] = field(default_factory=list)
    subfolders: List[Folder] = field(default_factory=list)


def calcSize():
    pass

pointer = ""
files = dict()
folders = dict()

while data:
    print(data.popleft())
else:
    print("Done")
