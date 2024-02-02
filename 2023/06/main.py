from functools import reduce

input = [i.strip() for i in open('input', 'r').readlines()]

class Record:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance
    
    def __str__(self):
        return f"Time: {self.time}, Distance: {self.distance}"  

def analyze(record) -> int:
    winners = 0

    for i in range(1, record.time):
        if i * (record.time - i) > record.distance:
            winners += 1
    
    return winners

def solve():
    """ times = list(map(int, input[0].split(":")[1].split()))
    distances = list(map(int, input[1].split(":")[1].split()))

    records = list()

    for i in range(0, len(times)):
        records.append(Record(times[i], distances[i]))

    permutations = list()
    for r in records:
        permutations.append(analyze(r))

    print(reduce(lambda x, y: x * y, permutations))
    """

    time = int("".join(input[0].split(":")[1].split()))
    distance = int("".join(input[1].split(":")[1].split()))
    print(analyze(Record(time, distance)))

solve()
    
