import numpy as np

def solve(n=1000):
    big_number = 2 ** n
    digit_sum = sum( [int(s) for s in str(big_number) ] )
    return digit_sum
