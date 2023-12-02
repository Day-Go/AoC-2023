import os

with open("input.txt", "r") as f:
    lines = f.readlines()

LIMTS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

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