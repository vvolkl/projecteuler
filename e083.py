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
result = 0

######## 
   

from numpy.random import random_sample

def weighted_values(values, probabilities, size):
    bins = np.add.accumulate(probabilities)
    return values[np.digitize(random_sample(size), bins)] 

m = np.loadtxt('matrix.txt', delimiter=',', dtype=int)
p = np.zeros(m.shape, dtype=m.dtype)
p[0,0] = 1
p[-1,-1] = 2

maxentry = np.amax(m)

moves = (np.array([0, 1], dtype=int),
        np.array([1, 0], dtype=int),
        np.array([-1,0], dtype=int),
        np.array([0,-1], dtype=int))



def connected(l1, path2):
    for e in path2:
        if np.sum(np.abs(e - l1)) == 1:
            return e
    return False 

#TODO: don't allow cluster forming
def valid_move(loc,L):
    return 0 <= loc[0] < L[0] and 0 <= loc[1] < L[1] 

def add_segment(pid,loc):
    if loc == None:
        return None
    opt = [] 
 
    for move in moves:   
        if valid_move(loc + move, p.shape):
            if not p[tuple(loc + move)]:
                opt.append(loc + move)
    if opt == []:
        return None
    if len(opt) == 1:
        return np.array(opt[0])
    tprob = np.sum([m[tuple(e)] for e in opt])
    #print tprob
    probs = np.array([(tprob - m[tuple(e)])/tprob for e in opt])
    #print probs
    return np.array(weighted_values(np.array(opt), probs, 1)[0])

loc1 = np.array([0,0])
loc2 = np.array(m.shape)-1
print m[-1,-1] == m[tuple(loc2)]

path1 = [loc1]
path2 = [loc2]

conn = 0
done = 0
while not done and (loc1 is not None or loc2 is not None):
    loc1 = add_segment(1,loc1)
    if loc1 is not None:
        path1.append(loc1)
        p[tuple(loc1)] = 1
        if connected(loc1,path2):
            done = 1
            break
    loc2 = add_segment(2,loc2)
    if loc2 is not None:
        path2.append(loc2)
        p[tuple(loc2)] = 2
        if connected(loc2, path1):
            #conn = connectd
            done = 1
    #print path1
    #print path2 


#TODO: calculate Pathsum


#TODO: spawn random paths in the middle and merge on contact


print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

