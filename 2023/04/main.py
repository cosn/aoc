import re

input = [i.strip() for i in open("input","r").readlines()]

def solve():
    points = 0;
    copies = [1] * len(input)

    for i, line in enumerate(input):
        numbers = re.search(f"Card\s+\d+:\s+([\d\s]+)\s+\|\s+([\d\s]+)", line)
        
        c_set = set(int(n) for n in numbers.group(1).split(' ') if len(n) > 0)
        m_set = set(int(n) for n in numbers.group(2).split(' ') if len(n) > 0)
        
        matches = c_set.intersection(m_set)
        
        if len(matches) > 0:
            points += pow(2, len(matches)-1)

            for _ in range(copies[i]):
                for j in range(len(matches)):
                    copies[i+j+1] += 1
    
    print(points)
    print(sum(copies))

solve()