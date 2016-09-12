#TODO: performance

import numpy as np
from itertools import permutations

def is_panmult(num):
    
    for x in range(999):
        x = int('9' + str(x))
        #if verbose:
         #   print "checking %i" % x
        for n in range(2,7 - len(str(x))):
            result = ""
            for i in range(1,n+1):
                result += str( int(x) * i)
                #if verbose:
                #    print x,i, result
            if result == num:
                return True
    return False 

def solve(n=100, verbose=False): 
    for e in permutations("987654321"):
        e = ''.join(e)
        if verbose:
            print "checking %s" % e
        if  is_panmult(e):
            result = e
            break
    return int(result)
