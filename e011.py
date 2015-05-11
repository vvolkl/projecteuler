import numpy as np

def solve(debug=False):
    data = np.loadtxt('e011.dat', dtype=np.int)
    result = 0
    # check rows and columns
    for dat in [data, np.transpose(data)]:
        for row in dat:
            for num in range(np.alen(row[:-3])):
                if result < np.prod(row[num:num+4]):
                    result = np.prod(row[num:num+4])
    #check diagonals and anti-diagonals
    for dat in [data, np.rot90(dat)]:
        for i in np.arange(-np.alen(dat[0,:]),np.alen(dat[:,0])):
            row= np.diagonal(dat,i)
            if debug:
                print i,row
            if np.alen(row) > 3:
                for num in range(np.alen(row[:-3])):
                    if debug:
                        print '      ', row[num:num+4]
                    if result < np.prod(row[num:num+4]):
                        result = np.prod(row[num:num+4])
    return result

