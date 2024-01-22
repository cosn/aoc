def merge_digits(digit1, digit2):
    return int(str(digit1) + str(digit2))

DIGITS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def solve():
    with open("input") as file:
        entries = []
        for line in file:
            n1, n2 = 0, 0
            for i, ch in enumerate(line):
                if ch.isdigit():
                    if n1 == 0:
                        n1 = int(ch)
                    n2 = int(ch)
                else:
                    for k, v in DIGITS.items():
                        if line[i:].startswith(k):
                            if n1 == 0:
                                n1 = v
                            n2 = v
                            break
            entries.append(merge_digits(n1, n2))

        print(sum(entries))

solve()