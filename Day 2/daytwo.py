# given input, determine the total score according to
# rock paper scissors strategy guide.
# opponent:
# - rock: A
# - paper: B
# - scissors: C

# you (pt. 1):
# - rock: X
# - paper: Y
# - scissors: Z

# you (pt. 2):
# - lose: X
# - tie: Y
# - win: Z

# scoring:
# 1 for rock, 2 for paper, 3 for scissors.
# if win, get 6.
# if tie, get 3.
# if loss, get 0.

# e.g.
# pt. 1: A/rock Y/paper = you win. score = 2 for paper + 6 for win.
# pt. 2: A/rock Y/draw = you choose rock. score = 1 for rock + 3 for tie.

# dict storing points returned from move made.
points_dict = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
}

# dict storing what would win given opponent's move.
win_dict = {
    "A" : "Y",
    "B" : "Z",
    "C" : "X",
}

# dict storing what would tie given opponent's move.
tie_dict = {
    "A" : "X",
    "B" : "Y",
    "C" : "Z",
}

# dict storing what would lose given opponent's move.
lose_dict = {
    "A" : "Z",
    "B" : "X",
    "C" : "Y",
}

# storing total points.
total_points_by_move = 0
total_points_by_result = 0


# given the opponent's move and the result needed, calculate the move we need to make
# and returns the points it will make.
def calc_move(opponent, result):
    score = 0
    if result == "X":
        score = points_dict[lose_dict[opponent]]
    elif result == "Y":
        score = 3 + points_dict[tie_dict[opponent]]
    else:
        score = 6 + points_dict[win_dict[opponent]]
    return score
        
# given the opponent's move and your move, calculate the points it will make.
def calc_points(opponent, you):
    score = 0
    if you == tie_dict[opponent]:
        score = 3 + points_dict[you]
    elif you == win_dict[opponent]:
        score = 6 + points_dict[you]
    else:
        score = points_dict[you]
    return score


with open('Day 2\input.txt') as f:
    for line in f:
        opponent = line[0]
        you, result = line[2], line[2]
        
        # adds points from your move and opponent's move.
        total_points_by_move += calc_points(opponent, you)
        
        # adds points from your move and result.
        total_points_by_result += calc_move(opponent, result)
        
print("The total score bsdrf on move strategy is: " + str(total_points_by_move))
print("The total score based on result strategy is: " + str(total_points_by_result))