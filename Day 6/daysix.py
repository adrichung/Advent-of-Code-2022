# Given a datastream string, find the first index where the preceding four characters are non-repeating.
# Also, find the index where the preceding 14 characters are non-repeating.

# e.g.
# bvwbjplbgvbhsrlpgdmjqwftvncz
# index 5: vwbj

def check(str):
    return

with open('Day 6\input.txt') as f:
    datastream = f.readline()
    
    # We know the first index is 4 (or 3 in practical terms)
    index_1 = 4
    index_2 = 14
    while True:
        substring = datastream[index_1 - 4: index_1]
        if len(set(substring)) == len(substring):
            break
        index_1 += 1
    while True:
        substring = datastream[index_2 - 14: index_2]
        if len(set(substring)) == len(substring):
            break
        index_2 += 1
    f.close()

print("The index of the datastream with a 4-char marker is: " + str(index_1))
print("The index of the datastream with a 14-char marker is: " + str(index_2))
