import numpy as np
import time

def sumMultiples(n):
    d = np.arange(0, n, 1)
    return np.sum(d[(d % 3 == 0) + (d % 5 == 0)])

def solve(n=1000):
    return sumMultiples(n)

