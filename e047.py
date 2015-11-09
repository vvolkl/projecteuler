

#TODO: performance
#TODO: check
from Primes import factors2, is_prime

def solve(n=4, verbose=True):
    result = 0
    i = 0
    count = n
    while not result:
        i += 1
        if not is_prime(i):
            if len(set(factors2(i))) == n:
                count -= 1
            else:
                count = n
        else:
            count = n
        if not count:
            result = i - n 
        if verbose:
            print i, count
    return result
