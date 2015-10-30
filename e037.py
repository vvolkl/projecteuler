
import numpy as np
from Primes import is_prime, sieve

def solve(n=100, verbose=False): 
    result = 0
    pfound = 0
    results = []
    i = 8
    while pfound < 11:
        if is_prime(i): # and ['4','6','8','0'] not in str(i):
            if verbose:
                print 'checking prime ', i
            s = str(i)
            relevance = 1
            for j in xrange(len(s)):
                num = s[j:]
                if verbose:
                    print '\t truncating from left, now checking ', num
                if not is_prime(int(num)):
                    relevance = 0
                    break
                num = s[:j+1]
                if verbose:
                    print '\t truncating from right, now checking ', num
                if not is_prime(int(num)):
                    relevance = 0
                    break
                #j = j + 1
            if relevance:
                if verbose:
                    print 'found it: ', i
                results.append(i)
                pfound = pfound + 1
        i = i + 1 
    result = sum(results)
    return result
