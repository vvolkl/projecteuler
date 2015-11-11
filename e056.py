import numpy as np

def digitsum(num):
    num = str(num)
    s = 0
    for e in num:
        s += int(e)
    return s

def solve(n=100, verbose=True):
    result = 0
    for a in range(100):
        for b in range(100):
            result = max(result, digitsum(a**b))
    return result


