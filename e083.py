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
import itertools
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

id1 = 1
id2 = 10

def connected(l1, path2, pid):
    for e in path2:
        if np.sum(np.abs(e - l1)) == pid:
            return e
    return False 

#TODO: don't allow cluster forming
def valid_move(loc,L):
    return 0 <= loc[0] < L[0] and 0 <= loc[1] < L[1] 

def add_segment(pid,loc):
    if loc == None:
        return None,None
    opt = [] 
 
    for move in moves:   
        if valid_move(loc + move, p.shape):
            if not (p[tuple(loc + move)] == pid or p[tuple(loc + move)] == pid + 1):
                opt.append(loc + move)
    #print opt
    if opt == []:
        return None,[None]
    if len(opt) == 1:
        return np.array(opt[0]), [np.array(opt[0])]
    tprob = np.sum([m[tuple(e)] for e in opt])
    #print opt,len(opt), tprob
    #print [m[tuple(e)] for e in opt]
    probs = np.array([(tprob-m[tuple(e)])/tprob for e in opt])    
    probs = probs / np.sum(probs)
    #print probs 
    #raw_input()
    #kum = itertools.combinations(range(len(opt)),len(opt)-1)
    #for e in kum:
    #    for f in e:
    #        print m[tuple(opt[f])] 
    #probs = np.array([(np.sum([m[tuple(opt[f])] for f in e]))/tprob for e in kum])
    #print probs
    #indopt = range(len(opt))
    #print indopt
    #choice = weighted_values(indopt, probs, 1)
    #print 'choice', choice, indopt.remove(choice) 
    return np.array(weighted_values(np.array(opt), probs, 1)[0]), opt


def calc_pathsum(path1,path2,loc):

    path1 = map(tuple, path1)
    path2 = map(tuple, path2)
    s = np.sum(m[path2])
    for e in path1:
        s += m[tuple(e)]
        if np.allclose(e,loc):
            return s
succ_path = np.zeros(p.shape)
totalpath = np.zeros(p.shape) 
inloc1 = np.array([0,0])
inloc2 = np.array(m.shape)-1
print m[-1,-1] == m[tuple(inloc2)]
maxres = 1e9
for trial in range(10):
    done = 0
    while not done:
        result = 0
        loc1 = inloc1
        loc2 = inloc2
        path1 = [inloc1]
        path2 = [inloc2]
        p = np.zeros(m.shape, dtype=m.dtype)
        p[0,0] = 1
        p[-1,-1] = 2

        conn = 0
        done = 0

        while not (done == 1  or (loc1 is None and loc2 is None)):
            loc1, env = add_segment(1,loc1)
            if loc1 is not None:
                path1.append(loc1)
                for e in env:
                    p[tuple(e)] = id1 + 1
                p[tuple(loc1)] = id1
                conn = connected(loc1,path2,id2)
                if conn is not False:
                    print path1[-1], path2[-1]
                    done = 1
                    result = calc_pathsum(path2,path1,conn)
                    maxres = min(maxres, result) 
                    print maxres, result
                    break
            loc2, env = add_segment(10,loc2)
            if loc2 is not None:
                path2.append(loc2)
                for e in env:
                    p[tuple(e)] = id2 + 1
                p[tuple(loc2)] = id2
                conn = connected(loc2, path1,id1)
                if conn is not False:
                    #conn = connectd
                    print path1[-1], path2[-1]
                    result = calc_pathsum(path1, path2, conn)
                    maxres = min(result, maxres)
                    print  maxres, result
                    done = 1
        if done:
            succ_path = succ_path + p
        else:
            totalpath = totalpath + p
            print 'not finished at ', path1[-1], path2[-1]
        #print path1[-1]
        #print path2[-1]
        #print conn
        # print result
        

#TODO: calculate Pathsum
#here = path1[-1]
#while not


#TODO: spawn random paths in the middle and merge on contact


print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

