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
data = lines

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
    size: int = 0
    def calcSize(self):
        self.size = sum([f.size for f in self.files])
        self.size += sum([f.calcSize() for f in self.subfolders])
        return self.size
    def getFolder(self, fname : str):
        for f in self.subfolders:
            if fname == f.name:
                return f

pointer = None
folders = []

while data:
    cmds = data.popleft().split(" ")
    if cmds[0] == "$":
        if cmds[1] == "cd":
            if cmds[2] == "..":
                pointer = pointer.parent
            else:
                folderName = cmds[2]
                if pointer == None:
                    newFolder = Folder(folderName)
                    folders.append(newFolder)
                    pointer = newFolder
                else:
                    pointer = pointer.getFolder(folderName)
            pass
        elif cmds[1] == "ls":
            continue
        else:
            assert False
    else:
        if cmds[0] == "dir":
            folderName = cmds[1]
            newFolder = Folder(folderName,pointer)
            folders.append(newFolder)
            pointer.subfolders.append(newFolder)
        else:
            assert cmds[0].isdigit()

            filesize = int(cmds[0])
            filename = cmds[1]
            newFile = File(filename,filesize)
            pointer.files.append(newFile)
else:
    diskUsage = folders[0].calcSize()


ans1 = 0
for f in folders:
    if f.size <= 100000:
        ans1 += f.size

print(ans1)
