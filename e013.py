from __future__ import division
doc = """

Valentin Volkl """

import argparse
import numpy as np
import re
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=10, 
                   help='the main variable for our program')
args = parser.parse_args()
n=args.n
start = time.time()


#dat = np.loadtxt('e013.txt')
#print np.sum(dat)
dat = []
with open('e013.txt') as f:
    for line in f:
        l = []
        #print line
        for char in line.strip():
            #print char
            l.append(int(char))
        dat.append(l)

dat = np.array(dat)
#print dat
tot = 0
corr = int( np.log10( np.sum(dat[:,0]))) + 1
print corr
for i in range(n - corr):
    print n-corr -i,i
    tot = tot +  np.sum(dat[:,i]) * 10 ** (n-corr - i)
    print np.sum(dat[:,i])

print tot

jump, hurdle = 1, 0
i = 1
remainder = 0
while (100 * jump > hurdle):
    hurdle = 10 ** i
    jump = np.sum(dat[:,n-corr+i]) + remainder * 10
    remainder = jump % hurdle
    
    print 'i, hurdle,np.sum(dat[:,9+i]),  jump, remainder, int(jump / hurdle)'
    print i, hurdle,np.sum(dat[:,9+i]),  jump, remainder, int(jump / hurdle)
    tot  = tot + int((jump) / hurdle)
    i = i + 1



print 'result:'
print tot
print 'elapsed time:'
print time.time()-start
