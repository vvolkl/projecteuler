
import numpy as np

def solve(n=1000000, verbose=False): 
    result = 0
    for num in xrange(n):
        if str(num) == str(num)[::-1]:
            if verbose:
                print 'found palindrome in base 10: ', num
            s = str(bin(num))[2:]
            if s == s[::-1]:
                if verbose:
                    print '\t and in base 2: ', s
                result = result + num
    return result
