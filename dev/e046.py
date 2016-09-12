
#TODO: performance
#TODO: check
from Primes import is_prime, sieve
import numpy as np

def solve(verbose=True):
    """
    Find the smallest odd composite number that cannot be written
    as the sum of a prime and a two times a square.
    """
    upperLimit = 100000
    result = 1
    for num in xrange(2, upperLimit):
        if not is_prime(num) and num % 2:
            result = 0
            for e in sieve(num):
                for f in xrange(int(np.ceil(np.sqrt((num-e)/2))+1)):
                    if verbose:
                        print num, e, f, result
                    result += num == e + 2 * f**2 
        if not result:
            result = num
            break
    return result
