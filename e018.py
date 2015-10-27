import numpy as np

def loadtriangle(fname):
    """ numpy.loadtxt, my weapon of choice, only accepts equal-length rows.
    this function is a hack that only does integers for the time being.
    """
    a = []
    with open(fname) as f:
        for line in f:
            num = line.split()
            num = map(int, num)
            a.append(np.array(num))
    return np.array(a)

def getpairs(a):
    paths = np.zeros(np.alen(a)-1)
    for i in range(np.alen(a)-1):
        paths[i] = max(a[i],a[i+1])
    return paths

def solve():
    triangle = loadtriangle('e018.txt')
    testtriangle  = loadtriangle('e018test.txt')
    #start with the bottom row, selecting always two neighbouring numbers
    #corresponding to the possible choices for the number above
    paths = 0
    for row in triangle[::-1]:
        row = row + paths
        paths = getpairs(row)
    return row 

