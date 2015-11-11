
from scipy import misc
import numpy as np

def solve(n=100, verbose=False):
    result = 0
    m = 100
    doub = False
    set_doub=False
    for _n in range(n + 1):
        for r in range(min(m, _n+1)):
            if misc.comb(_n,r) < 1e6:
                if doub:
                    result += 2
                else:
                    result += 1
                if verbose:
                    print _n, r, result, misc.comb(_n,r)  
            else:
                m = r + 1 
                set_doub = True
        if set_doub:
            doub=True
    return np.sum(range(n+2)) - result

def brute_force():
    result = 0
    for N in range(n+1):
        for r in range(N+1):
            if misc.comb(N,r)>1e6:
                result = result + 1
                if verbose:
                    print r,N,misc.comb(N,r)
    return result
        

