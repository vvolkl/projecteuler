
import numpy as np
import primehelpers_cpp as primehelpers
import Primes


def solve(n=1100, verbose=True):
    p = Primes.sieve(n**2)
    print 'generating checkTwoPrimeTable...'
        #print e
    checked = np.zeros((n+1,n+1))
    for i in range(n):
        for j in range(i,n):
            checked[i,j] = primehelpers.checkTwoPrimes(p[i], p[j]) > 0
    c = checked + checked.T
    p2 = p[:c.shape[0]]
    for i in range(1,1100):
        print i
        for j in np.nonzero(c[i,:])[0]:
            c1 = np.intersect1d(np.nonzero(c[i,:]), np.nonzero(c[j,:]))
            for k in c1:
                c2 = np.intersect1d(c1, np.nonzero(c[k, :]))
                for l in c2:
                    c3 = np.intersect1d(c2, np.nonzero(c[l, :]))
                    for m in c3:
                        c4 = np.intersect1d(c3, np.nonzero(c[m, :]))
                        print [p2[_o] for _o in [i,j,k,l,m]]
                        return np.sum([p2[_o] for _o in [i,j,k,l,m]])
                
