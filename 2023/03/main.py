from collections import defaultdict

input = [i.strip() for i in open("input","r").readlines()]

matrix = [[c for c in row] for row in input]
height = len(matrix)
width = len(matrix[0])

BITS = [(1, -1), (-1, -1), (1, 1), (-1, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]

def solve():
    p1,p2 = 0,0
    nums = defaultdict(list)
    for y, row in enumerate(matrix):
        num = 0
        part = False
        gears = set()
        for x, c in enumerate(row + ['.']):
            if c.isdigit():
                num = 10*num + int(c)
                for dx,dy in BITS:
                    if 0 <= y + dy < height and 0 <= x + dx < width:
                        cc = matrix[y + dy][x + dx]
                        if not cc.isdigit() and cc != '.':
                            part = True
                        if cc == '*':
                            gears.add((x + dx, y + dy))
            elif num != 0:
                if part:
                    p1 += num
                for gear in gears:
                    nums[gear].append(num)
                num, part, gears = 0, False, set()
    for _, l in nums.items():
        if len(l) == 2:
            p2 += l[0] * l[1]

    print(p1, p2)

solve()