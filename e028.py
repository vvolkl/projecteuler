from __future__ import division
doc = """

Valentin Volkl """
import argparse
import numpy as np
import re
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=1001, 
                   help='the main variable for our program')
parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
n=args.n
start = time.time()

def rot(arr):
    return [arr[1],-arr[0]]
    

if not n%2:
    print "grid must have odd dimensions! switching to %i +1" % n
    n = n +1


spiral = np.zeros((n,n))
#fill the spiral
pos = np.array( [np.floor(n/2)] * 2 )
vec = np.array( [0,1])
i = 0
while 0<=pos[0]<n and 0<=pos[1]<n: 
    i = i+1
    spiral[pos[0],pos[1]] = i
    pos = pos + vec 
    rotvec = rot(vec)
    if args.verbose:
        print spiral

    try:
        if not spiral[pos[0]+rotvec[0], pos[1] + rotvec[1]]:
            vec = rotvec
    except IndexError:
        break
result = np.sum(np.diagonal(spiral))
result = result + np.sum(np.diagonal(np.rot90(spiral)))

            
print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

