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
from matplotlib.colors import LogNorm
plt.ion()
from numpy.random import random_integers
import itertools

def weighted_values(values, probabilities, total, size):
    bins = np.add.accumulate(probabilities)
    return values[np.digitize(random_integers(1, high=total-1,size=size), bins)] 


m = np.loadtxt('matrix.txt', delimiter=',', dtype=int)
p = np.zeros(m.shape, dtype=int)
c = np.zeros(m.shape, dtype=int)
maxentry = np.amax(m)

moves = (np.array([0, 1], dtype=int),
        np.array([1, 0], dtype=int),
        np.array([-1,0], dtype=int),
        np.array([0,-1], dtype=int))
amoves = (np.array([0, 1], dtype=int),
          np.array([1, 0], dtype=int))
bmoves = (np.array([0, -1], dtype=int),
          np.array([-1, 0], dtype=int))

bweights=(1,1,0,0)
aweights=(0,0,1,1)

dirs = {-4: moves[1],
        -1: moves[3],
        -5: moves[0],
        -2: moves[2]}

def connected(l1, path2, pid):
    for e in path2:
        if np.sum(np.abs(e - l1)) == pid:
            return e
    return False 

def valid_move(loc,L):
    return 0 <= loc[0] < L[0] and 0 <= loc[1] < L[1] 

def add_segment(pid,loc,p):
    if loc == None:
        return None,None
    opt = [] 
    weights = (1,1,0.2,0.2)
    aweights = [1,1]
    bweights = [1,1]
    if pid == 10:
        weights = []
        for move, we in zip(amoves, aweights):   
            if valid_move(loc + move, p.shape):
                if not (p[tuple(loc + move)]) == pid: # or p[tuple(loc + move)] == pid + 1):
                    opt.append(loc + move)
                    weights.append(we)
                    
    elif pid == 20:
        weights = []
        for move, we in zip(bmoves, bweights):   
            if valid_move(loc + move, p.shape):
                if not (p[tuple(loc + move)]) == pid: # or p[tuple(loc + move)] == pid + 1):
                    opt.append(loc + move)
                    weights.append(we)
    else:
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
    probs = np.array([(tprob-int(e[1]*m[tuple(e[0])])) for e in zip(opt, weights)])    
    #probs = probs #/ np.sum(probs)
    #TODO: rewrite weighted_values to accept integers
    return np.array(weighted_values(np.array(opt), probs,np.sum(probs), 1)[0]), opt


def calc_pathsum(path1,path2,loc):
    s = 0
    path1 = map(tuple, path1)
    path2 = map(tuple, path2)
    for e in path2:
        s += m[e]
    for e in path1:
        s += m[e]
        if np.allclose(e,loc):
            return s

def rebuild_p(p, c, path, pid):
    c[p == pid] = 0
    c[p == pid + 1] = 0
    p[p == pid] = 0
    p[p == pid + 1] = 0
    for loc in path[:-1]:
        for m in moves:
            if valid_move(loc + m, p.shape):
                p[tuple(loc + m)] = pid + 1
                c[tuple(loc + m)] = -3 + m[0]  + 2 *  m[1] 
   
    count = 0
    for loc in path:
        p[tuple(loc)] = pid
        c[tuple(loc)] = count
        count += 1
    
pathlist = {}

class paths:
    #loc = np.zeros((2))
    #path = [loc]
    counter = 1
    special = False 
    active = 1
    def __init__(self,loc, pid=10):
        self.pid = pid 
        self.loc = loc
        self.path = [loc]
        self.special = (pid == 10) or (pid == 20)
        p[tuple(self.loc)] = self.pid

    def update(self,p,c):
        oldloc = self.loc
        self.loc, self.env = add_segment(self.pid, self.loc,p)
        if self.loc is None:
            return None 
        ploc = p[tuple(self.loc)]
        #print self.loc, ploc
        if ploc == self.pid:
            print 'going back'
            return 'going back!'
        elif ploc == 0:
            
            # mark neighbouring sites with a code to find the path
            for e in self.env:
                if not p[tuple(e)]:
                    p[tuple(e)] = self.pid + 1
                    c[tuple(e)] = -3 - ( oldloc[0] - e[0] ) - 2 * ( oldloc[1] - e[1] )
            p[tuple(self.loc)] = self.pid
            self.path.append(self.loc)
            self.counter += 1
            c[tuple(self.loc)] = self.counter
            return True
        elif ploc == self.pid + 1:
            self.connloc = self.loc + dirs[c[tuple(self.loc)]]
            #print np.allclose(self.connloc,self.loc)
            self.path = self.path[:c[tuple(self.connloc)]+1]
            self.counter = len(self.path)
            self.loc = self.path[-1]
            rebuild_p(p,c, self.path, self.pid)
            return True
        else:
            if ploc in [10,11,20,21]:
                if self.special:
                    # we are done
                    if c[tuple(self.loc)] < 0:
                        self.connloc = self.loc + dirs[c[tuple(self.loc)]]
                    else:
                        self.connloc = self.loc
                    return False
                else: 
                    """
                    if c[tuple(self.loc)] < 0:
                        self.connloc = self.loc + dirs[c[tuple(self.loc)]]
                    else:
                        self.connloc = self.loc
                    pathlist[p[tuple(self.connloc)]].connloc = self.loc
                    pathlist[p[tuple(self.connloc)]].loc = self.loc
                    merge(p,c,pathlist, pathlist[p[tuple(self.connloc)]], self)
                    """
                    
                    c[p == self.pid] = 0
                    c[p == self.pid + 1] = 0
                    p[p == self.pid] = 0
                    p[p == self.pid + 1] = 0
                    self.active = 0
                    return True
            else:
                #implement merging routine here
                self.path.append(self.loc)
                if c[tuple(self.loc)] < 0:
                    self.connloc = self.loc + dirs[c[tuple(self.loc)]]
                else:
                    self.connloc = self.loc
                #print 'merging ', self.connloc,self.pid, ploc
                #print p[self.connloc[0]-5:self.connloc[0]+5, self.connloc[1]-5:self.connloc[1]+5]
                merge(p,c,pathlist, self, pathlist[p[tuple(self.connloc)]])
                #print p[self.connloc[0]-5:self.connloc[0]+5, self.connloc[1]-5:self.connloc[1]+5]
            return True

special_pids = [10,20]

        
def merge(p,c,pathlist, path1, path2):
    mergepoint = path1.connloc
    path2.path = path2.path[:c[tuple(mergepoint)]+1]
            
    c[p == path2.pid] = 0
    c[p == path2.pid + 1] = 0
    p[p == path2.pid] = 0
    p[p == path2.pid + 1] = 0

    path1.path = path1.path + path2.path[::-1]
    path1.loc = path1.path[-1]
    rebuild_p(p,c,path1.path, path1.pid)
    path2.active = 0


#a.allpaths = [path() for i in range(10)]

#record 754109

fig = plt.figure()
graph1 = fig.add_subplot(111)
#graph2 = f.add_subplot(212)
g1 = graph1.matshow(p, norm=LogNorm(vmin=1, vmax=100))
#g2 = graph2.matshow(c)
done = 0    
mres = 2 * maxentry * m.shape[0] 
result = mres
numpaths = 40 
#TODO: spawn more paths here
for i in range(100):

    step = 0
    p[:,:] = 0
    c[:,:] = 0
    a = paths(np.array([0,0]), pid=10)
    b = paths(np.array(m.shape)-1, pid=20)
    pathlist = {}
    pathlist[a.pid] = a
    pathlist[b.pid] = b
    j = 3
    while j < numpaths + 3:
        xloc = random_integers(low=0, high=m.shape[0]-1,size=2)
        if random_integers(low=1,high=maxentry,size=1) < maxentry - m[tuple(xloc)]:
            pathlist[10*j] = paths(np.array(xloc), pid=10*j)
        
            j = j + 1

    #### 
    #raw_input()
    unconnected = True
    while unconnected == True and step < 1e5:
        if len(pathlist.values()) < 20:
            added = 0
            while not added:
                xloc = random_integers(low=0, high=m.shape[0]-1,size=2)
                if p[tuple(xloc)] ==0:
                    if random_integers(low=1,high=maxentry,size=1) < maxentry - m[tuple(xloc)]:
                        pathlist[10*j] = paths(np.array(xloc), pid=10*j)
                        added=1 
                        j = j + 1
        for pa in pathlist.values():
            #plt.show()
            #plt.matshow(p)
            #raw_input()
            if pa.active:
                unconnected  = pa.update(p,c)
            else:
                pathlist.pop(pa.pid,None)
            if unconnected == False:
                if pa.pid == 10:
                    result = calc_pathsum(pathlist[b.pid].path, pathlist[a.pid].path, pathlist[a.pid].connloc)
                elif pa.pid == 20:
                    result = calc_pathsum(pathlist[a.pid].path, pathlist[b.pid].path, pathlist[b.pid].connloc)
       
                mres = min(mres, result)
                print result, mres
                break
        rebuild_p(p,c,pathlist[10].path,10)
        rebuild_p(p,c,pathlist[20].path,20)
        if 0: #not step % 1e3 and 1:
            g1.set_data(p)
            plt.draw()
            raw_input()
    
    #raw_input()

"""
        if unconnected == True:
            unconnected = b.update(p,c)
            if unconnected == False:
                result = calc_pathsum(a.path, b.path, b.connloc)
        
                mres  = min(mres, result)
                break
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
