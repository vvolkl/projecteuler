
import numpy as np
from Primes import is_prime
from itertools import permutations

def greatest_pandigital():
    #Note: Nine numbers cannot be done 
    #(1+2+3+4+5+6+7+8+9=45 => always dividable by 3) 
    #Note: Eight numbers cannot be done 
    #(1+2+3+4+5+6+7+8=36 => always dividable by 3)
    for n in range(1,8)[::-1]:
        s = ''.join( [ str(a) for a in range(1, n+1)[ ::-1 ] ] )
        if verbose:
            print 'checking %i pandigital numbers: ' % n, s
        for e in permutations( s ):
            e = ''.join( e )
            if verbose:
                print e
            if is_prime( int(e) ):
                return e        

def solve(n=100, verbose=False): 
    result = greatest_pandigital()
    return result
