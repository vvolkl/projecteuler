from itertools import permutations

def solve():
    i = 0
    for e in permutations(range(10)):
        i = i + 1
        if i == 1000000:
            result = e
            break
    result = ''.join(map(str,result))
    return int(result)

