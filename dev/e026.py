import numpy as np
import decimal as dec

def solve(verbose=False):
    prec = 3000 
    dec.getcontext().prec = prec
    result = 0
    cyc = 0
    for num in np.arange(2,1001):
        d = dec.Decimal(1) / dec.Decimal(num)
        a = str(d)[2:]
        for j in np.arange(1,prec//2-2):
            if len(a)>prec - 3:
                l = [a[i:i+j] for i in range(0, len(a)-j-1, j)]
                if l.count(l[0]) == len(l):
                    if verbose:
                        print num,l[0],j
                    if cyc < j:
                        result = num
                        cyc = j
                    break
    return result        

