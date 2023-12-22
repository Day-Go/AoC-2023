from enum import IntEnum, auto
from collections import namedtuple

class Rank(IntEnum):
    FIVE_OAK = 1
    FOUR_OAK = 2
    FULL_H = 3
    THREE_OAK = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7

    
class CardCounter:
    def __init__(self) -> None:
        self.d = {}

    def add(self, card: str) -> None:
        if card in self.d.keys():
            self.d[card] += 1
        else:
            self.d[card] = 1

# Define function for determining hand strength.
def determine_hand_strength(hand: str) -> Rank:
    cc = CardCounter()
    for card in hand:
        cc.add(card)

    if 5 in cc.d.values():
        return Rank.FIVE_OAK
    elif 4 in cc.d.values():
        return Rank.FOUR_OAK
    elif 3 in cc.d.values() and 2 in cc.d.values():
        return Rank.FULL_H
    elif 3 in cc.d.values():
        return Rank.THREE_OAK

    pairs = [card for card, count in cc.d.items() if count == 2]
    if len(pairs) == 2:
        return Rank.TWO_PAIR
    elif 2 in cc.d.values():
        return Rank.ONE_PAIR
    
    return Rank.HIGH_CARD

GameStats = namedtuple('GameStats', ['cards', 'bet'])

card_value_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
                  'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def sorting_key(game):
    hand_strength = determine_hand_strength(game.cards)
    card_values = tuple(card_value_map[card] for card in game.cards)
    return (-hand_strength.value, card_values)

with open("input.txt", "r") as f:
    lines = f.readlines()

games = []
for line in lines:
    cards = line.split(' ')[0]
    bet = line.split(' ')[1]
    games.append(GameStats(cards, int(bet)))

    sorted_games = sorted(games, key=sorting_key, reverse=False)

total = 0
for i, game in enumerate(sorted_games):
    total += (i + 1) * game.bet 

print(total)