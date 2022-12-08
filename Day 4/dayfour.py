# Given campsites that each elf must cover as a pair.
# Find the total number of assignment pairs where one range contains another.
# Find the total number of assignment pairs where one range overlaps with another.

# e.g.
# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
# has 2 pairs where one range contains another and 4 where they overlap.

# Determines if a pair overlapping ranges.
def overlaps(pair):
    first = [int(i) for i in pair[0].split("-")]
    second = [int(i) for i in pair[1].split("-")]
    return first[0] <= second[0] <= first[1] or first[0] <= second[1] <= first[1] or second[0] <= first[0] <= second[1] or second[0] <= first[1] <= second[1]

# Determines if a pair has a range fully containing another.
def contains(pair):
    first = [int(i) for i in pair[0].split("-")]
    second = [int(i) for i in pair[1].split("-")]
    return first[0] <= second[0] and first[1] >= second[1] or first[0] >= second[0] and first[1] <= second[1]
    
with open('Day 4\input.txt') as f:
    total_subsets = 0
    total_overlaps = 0
    for line in f:
        if contains(line.replace('\n', '').split(",")):
            total_subsets += 1
        if overlaps(line.replace('\n', '').split(",")):
            total_overlaps += 1
    f.close()
            
print("The total number of pairs with one range fully in another is : " + str(total_subsets))
print("The total number of pairs with one range overlapping another is : " + str(total_overlaps))