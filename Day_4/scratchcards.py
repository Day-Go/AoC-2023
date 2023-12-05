with open('input.txt', 'r') as f:
    lines = f.readlines()

# Part 1
sum = 0
for line in lines:
    line = line[10:]
    winning_numbers = line.split('|')[0].split()
    my_numbers = line.split('|')[1].split()

    game_score = 0
    for num in my_numbers:
        if num in winning_numbers:
            if game_score == 0:
                game_score += 1
            else:
                game_score *= 2

    sum += game_score

print(sum)


