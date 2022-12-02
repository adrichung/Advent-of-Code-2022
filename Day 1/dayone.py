# given input with each line as num. of cals. in food item.
# each line break separates elves.
# find the max number of calories held by an elf.
# find the total of the top three elves.


# e.g. 
# 1000
# 2000
# 3000

# 4000
# 
# 5000
# 6000
# 
# 7000
# 8000
# 9000
# 
# 10000

# output 24000, for 7000 + 8000 + 9000
# output 45000 for total of top 3.

# stores the max calories counted so far.
max = 0

# array storing top 3 calorie totals so far.
top_three = [0, 0, 0]

# given a number, it checks if this number is greater than the minimum in top_three.
# if yes, replace the minimum with the number.
def insert(num):
    mini = min(top_three)
    if mini < num:
        index = top_three.index(mini)
        top_three[index] = num

with open('Day 1\input.txt') as f:
    current = 0
    for line in f:
        # \n indicates end of elf's list
        if line == "\n":
            
            # check if this elf would be in our running list of top 3 elves.
            insert(current)
            
            # replace max calories counted so far if the elf has more than our old max.
            if max < current:
                max = current
                
            # reset count
            current = 0
        else:
            current += int(line)
    f.close()
    
print("The highest amt of calories is: "  + str(max))
print("The top three are carrying: " + str(sum(top_three)))