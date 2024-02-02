class Map:
    def __init__(self):
        self.pairs = {}
    
    def set(self, mapping, line):
        print(mapping, line)
        
        fro, _, to = mapping.split('-')
        if self.pairs.get((fro, to)) is None:
            self.pairs[(fro, to)] = {}
        
        destination, source, length = map(int, line.split())
        
        for i in range(length):
            self.pairs[(fro, to)][source + i] = destination + i
        
    def traverse(self, seed) -> int:
        soil = self.pairs.get(('seed', 'soil')).get(seed, seed)
        fertilizer = self.pairs.get(('soil', 'fertilizer')).get(soil, soil)
        water = self.pairs.get(('fertilizer', 'water')).get(fertilizer, fertilizer)
        light = self.pairs.get(('water', 'light')).get(water, water)
        temperature = self.pairs.get(('light', 'temperature')).get(light, light)
        humidity = self.pairs.get(('temperature', 'humidity')).get(temperature, temperature)
        location = self.pairs.get(('humidity', 'location')).get(humidity, humidity)

        return location

input = [i.strip() for i in open('input', 'r').readlines()]

def solve():
    seeds = [int(i) for i in input[0].split(':')[1].split(' ') if len(i) > 0]
    
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
              
solve()