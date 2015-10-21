import numpy as np
from Primes import sieve

def brute_force(N=20):
    i = N
    done = False
    while not done:
        i = i + N
        done = True
        div = N - 1
        is_candidate = True
        while is_candidate and div > 1:
            is_candidate *= not ( i % div )
            div = div + 1
        done = is_candidate
    return i                

def smart(N, verbose=False):
    """
    Form product of primes up to N. Each prime factor has 
    a multiplicity that is given by its highest power that is still smaller than N.
    """
    result = 1
    logN = np.log(N)
    primes = sieve(N)
    for prime in primes:
         # every prime shows up ``exponent`` times in the final product
         exponent = np.floor(1. / np.log(prime) * logN)  
         if verbose:
             print prime, exponent
         result *= prime ** exponent
    return result

def solve(N=20):
    return smart(N)


