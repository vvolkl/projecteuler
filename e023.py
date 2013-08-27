from __future__ import division
doc = """

Valentin Volkl """
import argparse
import numpy as np
import re
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=100, 
                   help='the main variable for our program')
parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
n=args.n
start = time.time()

from itertools import chain, combinations

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

allsubsets = lambda n: list(chain(*[combinations(np.arange(0,n), ni) for ni in np.arange(1,n)]))

def divisorsum(a):
    a = factors2(a)
    na = len(a)
    h = np.array([list(e) for e in allsubsets(na)])
    return np.sum(np.unique( map(np.prod, [[a[e] for e in f] for f in h]))) + 1
def gen_abundant(): 
    abundant = []
    for i in np.arange(1,28123):
        e = divisorsum(i)
        if e > i:
            if args.verbose:
                print i,e
            abundant.append(i)
    np.savetxt('e023abundant.txt',np.array(abundant))
    return abundant

abundant = np.loadtxt('e023abundant.txt')

result = 0
def gen_sums():
    sums = []
    i = 0
    for e in abundant:
        i = i + 1
        if args.verbose:
            print i
        for f in abundant[0:i]:
            sums.append(f+e)

    sums = np.unique(sums)
    sums = np.sort(sums)
    np.savetxt('e023sums.txt', sums)
sums = np.loadtxt('e023sums.txt')
if args.verbose:
    print len(sums)
    print sums[0:10]

for e in np.arange(0,28124):
    if e not in sums:
        if args.verbose:
            print e
        result = result + e


print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

