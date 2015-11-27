
import numpy as np
import primehelpers_cpp as primehelpers
import Primes


def solve(n=1100, verbose=True):
    primes = primehelpers.sieve(n**2)
    # we only need the first n primes
    primes = primes[:n + 1]
    # generating checkTwoPrimeTable...
    checked = np.zeros((n + 1, n + 1))
    for i in range(n):
        for j in range(i, n):
            # checkTwoPrimes checks both concatenations
            # so no need to call it for values j < i
            checked[i, j] = primehelpers.checkTwoPrimes(primes[i], primes[j]) > 0
    # c should be symmetric, but one half was not touched before
    c = checked + checked.T
    for i in range(1, n): # for each prime do
        for j in np.nonzero(c[i, :])[0]: # go through its prime partners
            # the next partner must show up in both previous lists
            c1 = np.intersect1d(np.nonzero(c[i, :]), np.nonzero(c[j, :]))
            for k in c1: # and repeat procedure until we find a set that is long enough
                c2 = np.intersect1d(c1, np.nonzero(c[k, :]))
                for l in c2:
                    c3 = np.intersect1d(c2, np.nonzero(c[l, :]))
                    for m in c3:
                        c4 = np.intersect1d(c3, np.nonzero(c[m, :]))
                        # found 'em! return the sum of the corresponding primes
                        return np.sum([primes[_o] for _o in [i, j, k, l, m]])
                
