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

def order(part=1):
    order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    if part == 2:
        order = ['J'] + order

    return order

def value(hand, part=1) -> int:
    score = 0
    for c in hand:
        score += order(part).index(c)
        score *= 100

    return score

def replace_joker(hand) -> str:
    if 'J' not in hand:
        return hand
    if hand == 'J' * 5:
        return 'A' * 5
    else:
        cards = Counter(hand)
        mc = cards.most_common()
        if mc[0][0] == "J":
            mc = mc[1:]

        top = [n for n in mc if n[1] == mc[0][1]]
        tmc = sorted([(order(2).index(n[0]), n) for n in top])
        r = tmc[-1][1][0]

        return hand.replace('J', r)

def solve(part=1):
    hands = list()
    for line in input:
        hand, bid = line.split()
        typ = sorted(Counter(replace_joker(hand)).values(), reverse = True)
        type_rank = TYPES.index(typ) + 1
        hand_val = value(hand, part)

        score = pow(1000, 1000) * type_rank + hand_val
        hands.append((hand, score, bid))
   
    winnings = 0
    for i, (_, _, b) in enumerate(sorted(hands, key=lambda x: x[1])):
        winnings += int(b) * (i + 1)
    
    print(winnings)

solve(1)
solve(2)