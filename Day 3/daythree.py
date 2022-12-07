# Suppose a string represents an elf's rucksack.
# The string is varying length which can be split into two compartments by splitting the string in half.
# If there are items/chars matching in each compartment, there is a priority.
# Calculate the total priorities of input.
# In addition, calculate the sum of the priorities of each 3-elf group by 

# a -> z = 1 -> 26
# A -> Z = 27 -> 52

def find_badge(priorities):
    return set(priorities[0]) & set(priorities[1]) & set(priorities[2])

def score_priorities(priorities):
    total = 0
    for char in priorities:
        if char.isupper():
            total += ord(char) - 38
        else:
            total += ord(char) - 96
    return total

# given the rucksack string, find the priorities and calculate the score.
def find_priorities(rucksack):
    first_compartment = rucksack[:len(rucksack)//2]
    second_compartment = rucksack[len(rucksack)//2:]
    priorities = ''.join(set(first_compartment).intersection(second_compartment))
    return score_priorities(priorities)

with open('Day 3\input.txt') as f:
    total_score = 0
    group_score = 0
    index = 0
    group = [None] * 3
    for line in f:
        group[index] = line.replace("\n", "")
        total_score += find_priorities(line)
        index += 1
        if index == 3:
            group_score += score_priorities(find_badge(group))
            index = 0
    f.close()
    
print("The total priorities is: " + str(total_score))
print("The total group priorities is: " + str(group_score))