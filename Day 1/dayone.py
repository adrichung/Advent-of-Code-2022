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


max = 0
top_three = [0, 0, 0]

def insert(num):
    mini = min(top_three)
    if mini < num:
        index = top_three.index(mini)
        top_three[index] = num

with open('input.txt') as f:
    current = 0
    for line in f:
        if line == "\n":
            insert(current)
            if max < current:
                max = current
            current = 0
        else:
            current += int(line)
    f.close()
    
print("The highest amt of calories is: "  + str(max))
print("The top three are carrying: " + str(sum(top_three)))