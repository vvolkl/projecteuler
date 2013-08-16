from __future__ import division
doc = """

Valentin Volkl """

import argparse
import numpy as np
import re
import itertools
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=500, 
                    help='the main variable for our program')
parser.add_argument('f', metavar='f', type=int, nargs='?', default=False, 
                    help='switch for brute force solution')
args = parser.parse_args()
n=args.n

#d1ef trinum(n):
#    return np.sum(np.arange(1,n+1))

def checkfordiv(b):
    total = 0
    for e in np.arange(1,np.ceil(b/2+1)):
        r = b / e
        #print b,e,r
        if r == np.ceil(r):
            #print 'found it: ',e 
            total = total + 1
    return total 
    

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

from itertools import chain

def factors2(n):
    result = []
    # test 2 and all of the odd numbers
    # xrange instead of range avoids constructing the list
    for i in chain([2],xrange(3,n+1,2)):
        s = 0
        while n%i == 0:  #a good place for mod
            n /= i
            s += 1
        result.extend([i]*s) #avoid another for loop
        if n==1:
            return result

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

def istriangle(n):
    t = 0
    i = 0
    while t<n:
        t=t+i
        i=i+1
    return t == n

def findnumdiv(c):
    tot = 1

    d = np.bincount(c)
    e = np.nonzero(d)
    d = d[e] + 1
    return np.prod(d)
    
        
    

def bruteforce(n):
    a = sieve(20000000)
    start = time.time()
    total = i = 0
    trinum = 0 
    j = 0
    while  total<n:
        i = i + 1
        trinum = trinum + i
        if trinum != a[j]:
            total = findnumdiv(factors2(trinum))
            print total,i,trinum
        else:
            j = j + 1
            


    print 'result:'
    print i, trinum
    print 'elapsed time:'
    print time.time()-start

def dumb():
    #instead, generate all numbers with > 500 divisors and check if they are triangle numbers
    a = sieve(100000)
    b = np.prod(a[0:9])
    i = 1
    for crit in np.arange(10,14):
        old = a[0:9]
        for e in itertools.permutations(a[0:crit]):
            f = sorted(e[0:9]) 
            print f,old,e    
            if f != old:
                old = f
                b = np.prod(f)
                #b = b * i
                i = i + 1
                print f 
                if istriangle(b):
                    print 'result: ', b
                    return b

def smarter():
    a = sieve(100000)
    for k in np.arange(1,20):
        for i in np.arange(0,10):
            for j in np.arange(0,9):
                c = a[0:9]
                c[j]=a[i]
                print i,j,k
                b=np.prod(c)*k
                if istriangle(b):
                    return b

#print checkfordiv(236215980)
#print findnumdiv(factors2(28))

a = bruteforce(n)
print a

