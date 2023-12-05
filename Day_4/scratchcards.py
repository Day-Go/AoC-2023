with open('input.txt', 'r') as f:
    lines = f.readlines()

cards = [1] * len(lines)

# Part 1
s = 0
for i, line in enumerate(lines):
    line = ''.join(line.split(':')[1:])
    winning_numbers = line.split('|')[0].split()
    my_numbers = line.split('|')[1].split()

    game_score = 0
    for num in my_numbers:
        if num in winning_numbers:
            game_score += 1

    r = min(i+game_score+1, len(cards))
    for idx in range(i+1, r) :
        cards[idx] += cards[i]


    s += game_score

print(s)
print(sum(cards))


