# Given a list of commands, determine the sum of the signals at the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
# The signal is calculated by the cycle number x the register value at the cycle.

# Also, determine the letters output by converting the commands to pixels.

# Read in input.
with open('Day 10\input.txt') as f:
    commands = [line.strip() for line in f]
    f.close()

queue = []

# Turn commands into queue.
for cmd in commands:
    if cmd == "noop":
        queue.append(0)
    else:
        _, num = cmd.split(' ')
        queue.append(0)
        queue.append(int(num))
        
reg = 1
signals = []

for i in range(len(queue)):
    if (i + 1) % 40 == 0:
        print('\n', end ='')
    elif i % 40 == reg or i % 40 == reg - 1 or i % 40 == reg + 1:
        print('▓', end='')
    else:
        print('░', end='')
    if i == 19 or i == 59 or i == 99 or i == 139 or i == 179 or i == 219:
        signals.append(reg * (i + 1))
    reg += queue[i]
    
print("The sum of the signals is: " + sum(signals))