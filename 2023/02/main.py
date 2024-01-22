import re
from functools import reduce
import operator


BAG = {
     "red": 12,
     "green": 13,
     "blue": 14,
}

def solve():
    possible_games = []
    minimum_cubes = []

    with open("input") as file:
        for line in file:
            game, results = line.split(":")
            game_number = int(game.split(" ")[1])

            if all([not any(x > limit for x in map(int, re.findall(f"(\d+) {color}", results))) for color, limit in BAG.items()]):
                possible_games.append(game_number)
            
            minimum_cubes.append(reduce(operator.mul, [max(map(int, re.findall(f"(\d+) {color}", results))) for color in BAG.keys()]))
            
    print("Possible", sum(possible_games))
    print("Minimum", sum(minimum_cubes))
solve()