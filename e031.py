from __future__ import division
doc = """

Valentin Volkl """
import argparse
import numpy as np
import re
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=200, 
                   help='the main variable for our program')
parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
n=args.n
start = time.time()

coins  = [1,2,5,10,20,50,100,200][::-1]
c = len(coins)
if args.verbose:
    print "%i coins available" % c
result = 0

def tryCoin(res, iSize):
    
    if args.verbose:
        print "%i left, trying coin %i pence" % (res, coins[iSize])
    global result
    t = res - coins[iSize]
    if t == 0:
        result = result + 1
        if args.verbose:
            print "hit zero, registering possibility %i" % result

        
    #elif t < 0:
    #    pass
    elif t > 0:
        tryCoin(t, iSize)
        
        while iSize < c-1:
            iSize = iSize + 1
            if args.verbose:
                print "moving to smaller coin %i with index %i" % (coins[iSize], iSize)
            tryCoin(t, iSize )

      

for i in range(c):
    if args.verbose:
        print "trying coin %i" % coins[i]
    tryCoin(n,i)



print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

