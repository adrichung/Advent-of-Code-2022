# Given a list of terminal commands and files with their sizes, determine the sum of all directories with less than 100000 in size.
# Also find the smallest directory such that if it was deleted, it would result in free space of 30000000 if the total disk space available is 70000000

# e.g.

# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# 
#  Graphically, maps to:
# 
#  / (dir)
#  - a (dir)
#    - e (dir)
#      - i (file, size=584)
#    - f (file, size=29116)
#    - g (file, size=2557)
#    - h.lst (file, size=62596)
#  - b.txt (file, size=14848514)
#  - c.dat (file, size=8504156)
#  - d (dir)
#    - j (file, size=4060174)
#    - d.log (file, size=8033020)
#    - d.ext (file, size=5626152)
#    - k (file, size=7214296)

# The directories with at most 100000 in size are a and e, the total is thus 955437.
# The smallest directory to delete to free enough space is d.

from pathlib import Path

# From the commands read, make the tree.
def make_tree(commands):
    level = Path("")
    tree = {}
    for cmd in commands:
        if "dir" in cmd:
            _, name = cmd.split(" ")
            tree[level].append(level / name)
        elif "$ cd" in cmd:
            if ".." in cmd:
                level = level.parent
            else:
                name = cmd[5:]
                level = level / name
                if level not in tree:
                    tree[level] = []
        elif cmd[0].isnumeric():
            size, name = cmd.split(" ")
            tree[level].append((name, int(size)))
    return tree

# Calculates the size of each directory in the tree.
def directory_size(path):
    total_size = 0
    for child in tree[path]:
        if isinstance(child, tuple):
            total_size += child[1]
        elif isinstance(child, Path):
            total_size += directory_size(child)
    return total_size

with open('Day 7\input.txt') as f:
    commands = [line.strip() for line in f.readlines()]
    f.close()
    
tree = make_tree(commands)
size_dict = {dir: directory_size(dir) for dir in tree}

# Determines the size of all directories if the size is less than 100,000
total_under_100000 = sum(size_dict for size_dict in size_dict.values() if size_dict <= 100000)

# Find the smallest directory such that it frees enough space if deleted.
clearable_space = 30000000 - (70000000 - size_dict[Path("/")])
min_removeable_dir = (70000000, Path("Random/Path"))
for dir in size_dict:
    if size_dict[dir] >= clearable_space:
        if size_dict[dir] < min_removeable_dir[0]:
            min_removeable_dir = (size_dict[dir], dir)

print("The total size of all directories under 100,000 in size is: " + str(total_under_100000))
print("The size of the smallest directory deletable to free enough space is: " + str(min_removeable_dir[0]))