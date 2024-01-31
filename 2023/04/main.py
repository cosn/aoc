input = [i.strip() for i in open("input","r").readlines()]

def solve():
    points = 0;
    for card in input:
        _, cm = [i.strip() for i in card.split(':')]
        c, m = cm.split('|')

        c_set = set(int(n) for n in c.split(' ') if n)
        m_set = set(int(n) for n in m.split(' ') if n)
        
        matches = c_set.intersection(m_set)
        
        if len(matches) > 0:
            points += pow(2, len(matches)-1)
    
    print(points)

solve()