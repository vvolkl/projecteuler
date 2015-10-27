import scipy.misc

def solve(n=20):
    return int( scipy.misc.comb(2 * n, n) )
