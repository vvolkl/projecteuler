import numpy as np
from itertools import chain, combinations

def factors2(n): 
    result = []
    # test 2 and all of the odd numbers
    # xrange instead of range avoids constructing the list
    for i in chain([2],xrange(3,n+1,2)):
        s = 0
        while n%i == 0:  #a good place for mod
            n /= i
            s += 1
        result.extend([i]*s) #avoid another for loop
        if n==1:
            return result

def allsubsets(n):
    return  list(chain(*[combinations(np.arange(0,n), ni) for ni in np.arange(1,n)]))

def divisorsum(a):
    na = len(a)
    h = np.array([list(e) for e in allsubsets(na)])
    return np.sum(np.unique( map(np.prod, [[a[e] for e in f] for f in h]))) + 1

def solve(n=10000, verbose=False): 
    result = 0
    divtable = np.zeros(n+1)
    for i in np.arange(1,n+1):
        e = divisorsum(factors2( i ))
        divtable[i] = e    
        if e < n + 1 and divtable[e]:
            if i != e and i == divtable[e]:
                if verbose:
                    print i,e
                result = result + i + e
        elif e < n + 1:
            if i != e and i == divisorsum(factors2( i )):
                if verbose:
                    print i,e
                result = result + i + e
    return result 

