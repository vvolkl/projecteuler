def solve(verbose=False):
    names = []
    result = 0
    with open('e022_names.txt') as f:
        a = f.read()
        names = a.replace('"','').split(',')
    if verbose:
        print len(names)
        print names[1:10]
    names = sorted(names)
    if verbose:
        print len(names)
        print names[1:10]     
    i = 0
    for e in names:
        wordscore  = 0
        i = i + 1
        for char in e:
            wordscore = wordscore + ord(char) - 64
        if verbose:
            print i,e,wordscore,result    
        result = result  + wordscore * i
    return result

