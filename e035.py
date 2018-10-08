
import numpy as np
from Primes import is_prime, sieve

def all_rotations(s):
    for i in range(len(s)):
        yield s[i:] + s[:i]


def solve(n=1000000, verbose=False):
    results = []
    for num in sieve(n):
        if num not in results:
            if verbose:
                print "checking prime %i for circularity ..." % num
            relevant = True
            for rotated_prime in all_rotations(str(num)):
                if not is_prime(int(rotated_prime)):
                    relevant = False
            if relevant:
                if verbose:
                    print " ... it is circular!"
                    print rotations
                results += [int(e) for e in all_rotations(str(num))]
    result = len(np.unique(results))
    return result
