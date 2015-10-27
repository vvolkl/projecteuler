from __future__ import division

def solve(n=99, verbose=True):
    result = 1.
    for a in range(10,n):
        for bdigit in range(1,10):
            b = str(bdigit) * 2
            b = map(''.join, zip(str(a),b) + zip(b,str(a)))
            b = map(int,b)
            #if verbose:
            #    print "============= b: ",b, str(a*2)
            for e in zip(b, str(a)*2):
            #    if verbose:
            #        print a,bdigit,e
                adigit = int(str(a).replace(e[1], '', 1))
                if a / e[0] == adigit / bdigit and a / e[0] < 1 and int(e[1]):
                    print result
                    result = result * a / float(e[0])
                    #result = result * adigit / float(bdigit)
                    if verbose:
                        print 'adigit,a: %i,%i' % (adigit, a)
                        print "%i / %i" % (a, e[0])
                        print "found it! == %i / %i" % (adigit, bdigit) 
    return result
        
        


