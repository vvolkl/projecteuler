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
#parser.add_argument('a', metavar='a', type=int, nargs='?', default=2000, 
#                   help='the auxiliary variable for our program')
parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
n=args.n
start = time.time()

def is_pent(num):
    a = np.sqrt(1/36 + 2/3 * num)
    b = 1/6
    #if args.verbose:
    #    print "calculating n... ",np.ceil(a+b), a+b, b-a
    return np.ceil(b  +  a) - ( b +  a) < 0.00000001

def pent(n):
    n = n + 1
    return n * (3 * n - 1) // 2 

result = 0

results = []
#pen = [a * (3 * a - 1) / 2 for a in range(1,n)]
l = n 
j = l 
while not result:
    j += 1 
    if args.verbose:
        print "checking bigger pent number", j
    for i in range(0,j):
        if is_pent(abs(pent(j)-pent(i))):
            if is_pent(pent(j) + pent(i)):
                result = (j,i)  


#[[results.append(set([i,j]))  for i in range(0,j) if is_pent(abs(pent(j)-pent(i))) and is_pent(pent(j)+pent(i))] for j in range(l)]
#su  = [[set([i,j])  for i in range(l) if abs(pen[i]+pen[j]) in pen ] for j in range(l)]
#if args.verbose:
    #print pen[:10]
    #print np.array(diff)

#su = [e for f in su for e in f if e]
#diff = [e for f in diff for e in f if e]
#for e in diff:
##    if e in su:
#        results.append(e)
print results
#print [e for e in su if e and e in diff]
#icand =  [[(i,j) for i in range(l) if ( diff[i][j] in pen)] for j in range(l)]
#print np.array(cand)

print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

