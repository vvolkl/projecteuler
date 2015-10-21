import numpy as np

def solve(n=100):
    x = np.arange(1, n+1)
    return  np.sum(x)**2 - np.sum(x**2) 

