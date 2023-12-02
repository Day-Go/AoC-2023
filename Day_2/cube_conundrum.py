from collections import defaultdict
from functools import reduce
import operator

with open("input.txt", "r") as f:
    lines = f.readlines()

LIMTS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

# Part 1
sum = 0
for line in lines:
    game_id = line.split()[1].strip(':')
    sets = ' '.join(line.split()[2:]).split(';')

    VALID_FLAG = True
    for set in sets:
        marbles = set.strip().lstrip().split(',')
        
        for marble in marbles:
            num, color = marble.split()
            num = int(num)
            if num > LIMTS[color]:
                VALID_FLAG = False
                break
            
    if VALID_FLAG:
        sum += int(game_id)
    
print(sum)

# Part 2
sum = 0
for line in lines:
    game_id = line.split()[1].strip(':')
    sets = ' '.join(line.split()[2:]).split(';')

    d = defaultdict(int)
    for set in sets:
        marbles = set.strip().lstrip().split(',')

        for marble in marbles:
            num, color = marble.split()
            num = int(num)
            d[color] = max(num, d[color])

    sum +=  reduce(operator.mul, d.values(), 1)

print(sum)
