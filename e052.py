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
result = 0

######## 
i = 0

def has_same_digits(a, b):
    for char in a:
        b = b.replace(char,'',1)
        #print b
    return b == ''



while not result:
    j = 1
    while has_same_digits(str(j*i),str((j+1)*i)) and j < n :
        if j == n - 1:
            result = i
        if args.verbose:
            print '\r %(i)5i \t %(j)1i' % locals(),
        j = j + 1
    i = i + 1
     
    




print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

