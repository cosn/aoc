from collections import Counter

input = [i.strip() for i in open('input', 'r').readlines()]

TYPES = [
    [1, 1, 1, 1, 1], # high card
    [2, 1, 1, 1], # one pair
    [2, 2, 1], # two pair
    [3, 1, 1], # three of a kind
    [3, 2], # full house
    [4, 1], # four of a kind
    [5], # five of a kind
]

def value(hand) -> int:
    order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    score = 0
    for c in hand:
        score += order.index(c)
        score *= 100

    return score

def solve():
    hands = list()
    for line in input:
        hand, bid = line.split()
        typ = sorted(Counter(hand).values(), reverse = True)
        type_rank = TYPES.index(typ) + 1
        hand_val = value(hand)

        score = pow(1000, 1000) * type_rank + hand_val 
        hands.append((hand, score, bid))
   
    winnings = 0
    for i, (_, _, b) in enumerate(sorted(hands, key=lambda x: x[1])):
        winnings += int(b) * (i + 1)
    
    print(winnings)

solve()