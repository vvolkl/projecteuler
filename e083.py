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
   
import matplotlib.pyplot as plt

plt.ion()
from numpy.random import random_sample
import itertools
def weighted_values(values, probabilities, size):
    bins = np.add.accumulate(probabilities)
    return values[np.digitize(random_sample(size), bins)] 

m = np.loadtxt('matrix.txt', delimiter=',', dtype=int)
p = np.zeros(m.shape, dtype=int)
p[0,0] = 1
p[-1,-1] = 2

c = np.zeros(m.shape, dtype=int)

maxentry = np.amax(m)

moves = (np.array([0, 1], dtype=int),
        np.array([1, 0], dtype=int),
        np.array([-1,0], dtype=int),
        np.array([0,-1], dtype=int))
dirs = {-4: moves[1],
        -1: moves[3],
        -5: moves[0],
        -2: moves[2]}

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

def add_segment(pid,loc,p):
    if loc == None:
        return None,None
    opt = [] 
 
    for move in moves:   
        if valid_move(loc + move, p.shape):
            if not (p[tuple(loc + move)]) == pid: # or p[tuple(loc + move)] == pid + 1):
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
    #TODO: rewrite weighted_values to accept integers
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

def rebuild_p(p, c, path, pid):
    for loc in path[:-1]:
        for m in moves:
            if valid_move(loc + m, p.shape):
                p[tuple(loc + m)] = pid + 1
                c[tuple(loc + m)] = -3 - m[0] - 2 *  m[1] 
   
    count = 0
    for loc in path:
        p[tuple(loc)] = pid
        c[tuple(loc)] = count
        count += 1
    

class paths:
    loc = np.zeros((2))
    path = [loc]
    counter = 1 
    def __init__(self, pid=10):
        self.pid = pid 
        p[tuple(self.loc)] = self.pid

    def update(self,p,c):
        oldloc = self.loc
        self.loc, self.env = add_segment(self.pid, self.loc,p) 
        ploc = p[tuple(self.loc)]
        print self.loc, ploc
        if ploc == self.pid:
            return 'going back!'
        if not ploc:
            
            # mark neighbouring sites with a code to find the path
            for e in self.env:
                if not p[tuple(e)]:
                    p[tuple(e)] = self.pid + 1
                    c[tuple(e)] = -3 - ( oldloc[0] - e[0] ) - 2 * ( oldloc[1] - e[1] )
            p[tuple(self.loc)] = self.pid
            self.path.append(self.loc)
            self.counter += 1
            c[tuple(self.loc)] = self.counter
        elif ploc == self.pid + 1:
            self.connloc = self.loc + dirs[c[tuple(self.loc)]]
            self.path = self.path[:c[tuple(self.connloc)]+1]
            self.counter = len(self.path)
            self.loc = self.path[-1]
            c[p == self.pid] = 0
            c[p == self.pid + 1] = 0
            p[p == self.pid] = 0
            p[p == self.pid + 1] = 0
            rebuild_p(p,c, self.path, self.pid)
            


class path(paths):
    pass

a = paths()
#a.allpaths = [path() for i in range(10)]


f = plt.figure()
graph1 = f.add_subplot(211)
graph2 = f.add_subplot(212) 
for i in range(100):
    a.update(p,c)
    graph1.matshow(p)
    graph2.matshow(c)
    
    raw_input()
    plt.draw()


"""
for trial in range(1):
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
            loc1, env = add_segment(1,loc1,p)
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
            loc2, env = add_segment(10,loc2,p)
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
        print path1[-1]
        print path2[-1]
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
"""
