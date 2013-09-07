from __future__ import division
doc = """

Valentin Volkl """
import argparse
import numpy as np
import re
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=99, 
                   help='the main variable for our program')
parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
n=args.n
start = time.time()

result = 1

for a in xrange(10,n):
    for bdigit in xrange(1,10):
        b = str(bdigit) * 2
        b = map(''.join,zip(str(a),b) + zip(b,str(a)))
        b = map(int,b)
        #if args.verbose:
        #    print "============= b: ",b, str(a*2)
                
        for e in zip(b,str(a)*2):
        #    if args.verbose:
        #        print a,bdigit,e
            adigit = int(str(a).replace(e[1], '',1))
            if a / e[0] == adigit / bdigit and a / e[0] < 1 and int(e[1]):
                result = result * a / e[0]
                if args.verbose:
                    print 'adigit,a: %i,%i' % (adigit,a)
                    print "%i / %i" % (a,e[0])
                    print "found it! == %i / %i" % (adigit,bdigit) 
        
        



print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

