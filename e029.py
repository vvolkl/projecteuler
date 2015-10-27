import numpy as np
from itertools import chain

def factors2(n): 
    result = []
    # test 2 and all of the odd numbers
    # xrange instead of range avoids constructing the list
    for i in chain([2], xrange(3, n + 1, 2)):
        s = 0
        while n % i == 0:  #a good place for mod
            n /= i
            s += 1
        result.extend([i]*s) #avoid another for loop
        if n == 1:
            return result

def solve(n=100, verbose=False):
    # idea for improvement: check before adding number to
    # save disk space
    terms = []
    i = 0
    for a in np.arange(2, n + 1):
        for b in np.arange(2, n + 1):
            if verbose:
                print i,a,b
            terms.append(sorted(factors2(a)*b))
            i = i + 1
    #terms = terms[np.nonzero(terms)] 
    terms = np.array(terms)
    result = np.alen( np.unique(terms) )
    return result
