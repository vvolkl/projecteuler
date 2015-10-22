import numpy as np

def solve(n=1000):
    # loop over first triplet number
    for a in np.arange(1, n):
        # second triplet number must be bigger than first
        for b in np.arange(a+1, n+1):
            # third triplet number is determined by first two
            c = np.sqrt(a**2 + b**2)
            # if c is an integer and the triplet sums up to 1000 we are done
            cc = np.ceil(c)
            if cc == c:
                if np.sum([a,b,cc]) == 1000: 
                    #print a, b, cc, np.sum([a, b, cc])
                    result = np.prod([a,b,cc])
                    return result
