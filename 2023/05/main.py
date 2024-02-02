from collections import defaultdict
class Map:
    def __init__(self):
        self.pairs = defaultdict(list)
    
    def set(self, mapping, line):
        fro, _, to = mapping.split('-')
        self.pairs[(fro, to)].append(list(map(int, line.split())))
        
    def traverse(self, seed) -> int:
        soil = self._find(self.pairs[('seed', 'soil')], seed)
        fertilizer = self._find(self.pairs[('soil', 'fertilizer')], soil)
        water = self._find(self.pairs[('fertilizer', 'water')], fertilizer)
        light = self._find(self.pairs[('water', 'light')], water)
        temperature = self._find(self.pairs[('light', 'temperature')], light)
        humidity = self._find(self.pairs[('temperature', 'humidity')], temperature)
        location = self._find(self.pairs[('humidity', 'location')], humidity)

        return location

    def traverse_pairs(self, seeds) -> int:
        locations = list()

        for s in range(seeds[0], seeds[0]+seeds[1]):
            locations.append(self.traverse(s))

        return min(locations)

    def _find(self, entries, target) -> int:
        res = target
        for dest, src, len in entries:
                if target < src or target > src + (len - 1):
                    continue
                else:
                    res = dest + (target - src)
                    break
        return res

input = [i.strip() for i in open('input', 'r').readlines()]

def solve():
    seeds = [int(i) for i in input[0].split(':')[1].split(' ') if len(i) > 0]
    
    seed_pairs = list()
    for i in range(0, len(seeds), 2):
        seed_pairs.append((seeds[i], seeds[i+1]))

    m = Map()
    i = 2

    while i < len(input):
        if input[i].endswith(':'):
            mapping = input[i].split(' ')[0]
            i += 1

            while i < len(input) and input[i] != '':
                m.set(mapping, input[i])
                i += 1
        
        i += 1

    print(min(map(m.traverse, seeds)))
    print(min(map(m.traverse_pairs, seed_pairs)))
              
solve()