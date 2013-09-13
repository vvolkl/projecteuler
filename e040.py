from __future__ import division
doc = """

Valentin Volkl """
import argparse
import numpy as np
import re
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=6, 
                   help='the main variable for our program')
parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
n=args.n
start = time.time()

counter, result  = 1, 1
length = 0
interesting = []
for e in range(1,n+1):
    interesting.append(10**e)
i = 0

if args.verbose:
    print "interesting: ", interesting

#while length < max( interesting ):
while i < len(interesting):
#    if args.verbose:
#        print counter
    length += len(str(counter))
#    if args.verbose:
#        print length, interesting[i]
    if length >= interesting[i]:
        digit =  int( str( counter)[::-1][length - interesting[i] ]  ) 
        result *= digit
        if args.verbose:
            print "found it: length: ", length," new number: ", counter," result so far: ", result, "digit that was added: ", digit 
        i += 1
    counter += 1



print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

