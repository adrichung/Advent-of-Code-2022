# Given a patch of trees planted in a grid, determine which trees are visible from outside the grid.
# The trees are visible from the top, left, right, and bottom only.
# The number in the grid represents the tree's height, 0 being shortest and 9 being tallest.
# A tree is only visible from an angle if there are only trees shorter than it to the edge.

# Also calculate the highest scenic score of all the trees.
# The scenic score is determined by the product of the total number of viewable trees from a tree.

# e.g.
# 30373
# 25512
# 65332
# 33549
# 35390

# 21 trees are visible (for example, the top-left 5.)
# The tree with the highest scenic score is the 5 in the 4th row. (2 x 2 x 1 x 2 => 8)

def calc_up(tree):
    index = y
    total_up = 0
    if index == 0:
        return 0
    while True:
        index -= 1
        total_up += 1
        if index == 0 or grid[index][x] >= tree:
            break
    return total_up

def calc_down(tree):
    index = y
    total_down = 0
    if index == col_max:
        return 0
    while True:
        index += 1
        total_down += 1
        if index == col_max or grid[index][x] >= tree:
            break
    return total_down

def calc_left(tree):
    index = x
    total_left = 0
    if index == 0:
        return 0
    while True:
        index -= 1
        total_left += 1
        if index == 0 or grid[y][index] >= tree:
            break
    return total_left

def calc_right(tree):
    index = x
    total_right = 0
    if index == row_max:
        return 0
    while True:
        index += 1
        total_right += 1
        if index == row_max or grid[y][index] >= tree:
            break
    return total_right

def check_right(tree):
    index = x + 1
    while index <= col_max:
        temp = grid[y][index]
        if temp >= tree:
            return False
        index += 1
    return True

def check_left(tree):
    index = x - 1
    while index >= 0:
        temp = grid[y][index]
        if temp >= tree:
            return False
        index -= 1
    return True

def check_up(tree):
    index = y - 1
    while index >= 0:
        temp = grid[index][x]
        if temp >= tree:
            return False
        index -= 1
    return True

def check_down(tree):
    index = y + 1
    while index <= row_max:
        temp = grid[index][x]
        if temp >= tree:
            return False
        index += 1
    return True

grid = []
with open('Day 8\input.txt') as f:
    for line in f:
        row_line = [int(i) for i in list(line.replace("\n", ""))]
        grid.append(row_line)
    f.close()

total_visible, x, y, max_scenic = 0, 0, 0, 0
row_max, col_max = len(grid) - 1, len(grid[0]) - 1

for row in grid:
    for tree in row:
        if check_up(tree) or check_down(tree) or check_left(tree) or check_right(tree):
            total_visible += 1
        scenic_score = calc_left(tree) * calc_right(tree) * calc_up(tree) * calc_down(tree)
        if scenic_score > max_scenic:
            max_scenic = scenic_score
        x += 1
    x = 0
    y += 1

print("The total number of visible trees is: " + str(total_visible))
print("The highest scenic score is: " + str(max_scenic))