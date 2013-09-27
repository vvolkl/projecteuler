"Helper functions for prime calculations for projecteuler problems"
import numpy as np

def sieve(n):
    m = (n-1) // 2
    b = [True]*m
    i,p,ps = 0,3,[2]
    while p*p < n:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i+=1; p+=2
    while i < m:
        if b[i]:
            ps.append(p)
        i+=1; p+=2
    return ps

#http://stackoverflow.com/questions/4545114
#
# sqrt(1000000000) = 31622
__primes = sieve(31622)
from bisect import bisect_left
def is_prime(n):
    # if prime is already in the list, just pick it
    if n <= 31622:
        i = bisect_left(__primes, n)
        return i != len(__primes) and __primes[i] == n
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
        if p > limit: return True
        if n % p == 0: return False
    # fall back on trial division if n > 1 billion
    for f in range(31627, limit, 6): # 31627 is the next prime
        if n % f == 0 or n % (f + 4) == 0:
            return False
    return True


def is_pent(num):
    a = np.sqrt(1./36 + 2./3 * num)
    b = 1./6 
    
    print "calculating n... ",np.ceil(a+b), a+b, b-a
    return abs(np.ceil(a + b) - (a + b)) < 0.00001 #or abs(np.ceil(b - a) - (b-a)) < 0.00001

def is_hex(num):
    b = 0.25
    a = np.sqrt( 0.0625 + num / 2.)
    return abs(np.ceil(a + b) - (a + b)) < 0.00001 # or abs(np.ceil(b - a) - (b-a)) < 0.00001

#if __name__ == "__main__":
#	import numpy as np
