def solve(n=100, verbose=True):
    result = 0
    with open('e042words.txt') as f:
        words = f.read()
    words = words.replace('"', '').split(',')
    mlen = max( map(len, words) )
    if verbose:
        print words[0:10], '...'
        print "longest word has %i letters" % mlen
    maximum = 26 * mlen
    triangles = [ n * ( n+1 ) / 2 for n in range(1, maximum) ]
    if verbose:
        print "triangle hash list: ", triangles[0:10], "..."
    result = sum( [ sum( [ord(d) - 64 for d in w ]) in triangles for w in words ] )
    return result

