# Given a ship's loading status of crates and movement instructions, find the final state of the ship.
# Find the top crate of each stack.
# Part one: the crane moves one crate at a time.
# Part two: the crane moves two crates at a time.

# e.g.

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

# results in:

#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3

# So we output CMZ.

import re

# Moves n arrays
def move_multiple(moves):
    count = moves[0]
    src = moves[1] - 1
    dest = moves[2] - 1
    temp = []
    for i in range(count):
        temp.append(stacks_2[src][i])
    stacks_2[dest] = temp + stacks_2[dest]
    del stacks_2[src][:count]

# Runs a given move on the stacks.
def move(moves):
    count = moves[0]
    src = moves[1] - 1
    dest = moves[2] - 1
    for i in range(count):
        block = stacks_1[src][0]
        stacks_1[dest].insert(0, block)
        del stacks_1[src][0]

# Given a layer, add any blocks to that layer.
def add_layer(stacks, line):
    idx = 1
    col = 0
    length = int(len(line))
    while idx < length:
        if line[idx] != " " and not(line[idx].isnumeric()):
            stacks[col].append(line[idx])
        idx += 4
        col += 1
        
with open('Day 5\input.txt') as f:
    
    # Create right number of lists to store each stack.
    
    line = f.readline().replace("\n", "")
    while True:
        line = f.readline().replace("\n", "")
        cols = [int(i) for i in re.findall(r'\d+', line)]
        if len(cols) != 0:
            break
    length = len(cols)
    stacks_1 = [[] for _ in range(length)]
    stacks_2 = [[] for _ in range(length)]
    f.seek(0)
    # Build list
    while True:
        line = f.readline().replace("\n", "")
        add_layer(stacks_1, line)
        add_layer(stacks_2, line)
        if line == "":
            break
    # Do moves
    for line in f:
        moves = [int(i) for i in re.findall(r'\d+', line)]
        move(moves)
        move_multiple(moves)
    f.close()
    
print("The top of each stack if we move one crate at a time is: ")
for i in stacks_1:
    print(i[0])
    
print("The top of each stack if we move multiple crates at once is: ")
for i in stacks_2:
    print(i[0])