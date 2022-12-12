# Given a list of commands of a rope, determine the movements of the tail given by movements by the head.
# Calculate how many points the tail will visit.
# Also calculate if the tail was 9 knots long.

# e.g. 

# R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2

# Covers 13 positions at least once.

# Class to represent the rope, where x,y is the position of the head of the rope.
class Rope:
    def __init__(self):
        self.x = 0
        self.y = 0
   
# Class to represent the tail of the rope, inheriting from Rope class.      
class Tail(Rope):
    def __init__(self):
        super().__init__()
        self.visited = 0
        self.history = set()
    
    # After a move, calculate the position of the tail. If the tail is in a new position, note it.
    def follow(self, x, y):
        distance_x = x - self.x
        distance_y = y - self.y
        if abs(distance_x) == 2 and distance_y == 0:
            if distance_x > 0:
                xv = 1
            else:
                xv = -1
            self.x += xv
        elif abs(distance_y) == 2 and distance_x == 0:
            if distance_y > 0:
                yv = 1
            else:
                yv = -1
            self.y += yv
        elif (abs(distance_y) == 2 and abs(distance_x) in (1, 2)) or (abs(distance_x) == 2 and abs(distance_y) in (1, 2)):
            if distance_x > 0:
                xv = 1
            else:
                xv = -1
            self.x += xv
            if distance_y > 0:
                yv = 1
            else:
                yv = -1
            self.y += yv
        if (self.x, self.y) not in self.history:
            self.visited += 1
        self.history.add((self.x, self.y))
            
        
rope = Rope()
tail = Tail()
tails = [Tail() for i in range(9)]

with open('Day 9\input.txt') as f:
    for line in f:
        dir, times = line.split()
        for i in range(int(times)):
            if dir == 'U':
                rope.y += 1
            elif dir == 'D':
                rope.y -= 1
            elif dir == 'L':
                rope.x -= 1
            elif dir == 'R':
                rope.x += 1
            tail.follow(rope.x, rope.y)
            tails[0].follow(rope.x, rope.y)
            for j in range(1, 9):
                tails[j].follow(tails[j - 1].x, tails[j - 1].y)
    f. close()
            
print("The number of points visited by the tail: " + str(tail.visited))
print("The number of points the tail of the larger rope has visited: " + str(tails[8].visited))
            