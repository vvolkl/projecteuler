from __future__ import division
doc = """

Valentin Volkl """
import argparse
import numpy as np
import re
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=10000, 
                   help='the main variable for our program')
parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
n=args.n
start = time.time()
result = 0

######## 

lycrels = []

for i in range(n):
    temp = i
    j = 0
    done = 0
    if args.verbose:
        print 'checking ', i
    while j < 50  and not done:
        if args.verbose:
            print '\riteration ', j
        temp = temp + int(str(temp)[::-1])
        if str(temp)[::-1] == str(temp): 
            done = 1
            if args.verbose:
                print 'found palindrome: ', temp
        j = j + 1 
    if done == 0:
        result += 1
        lycrels.append(i)
        if args.verbose:
            
            print 'found lycrel:', i
       

print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

