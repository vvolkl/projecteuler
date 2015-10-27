import numpy as np

ds = {0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'}

dd = ['',
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety']

dtens = ['ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen']

def wordlength(num):
    l = 0
    literal = str(num).zfill(3)[::-1]
    f = []
    for d in literal:
        f.append(int(d))
    if f[1] != 1:
        l = l + len(ds[f[0]])
        l = l + len( dd[f[1]])
    elif f[1] == 1:
        l = l + len(dtens[f[0]]) 
    if f[2]:
        l = l + len (ds[f[2]] + 'hundred')
        if f[1] or f[0]:
            l = l + len('and')
    if num == 1000:
        l = len("onethousand")
    if num > 1000:
        print 'error! number too big!'
    return l

def solve(n=1000):
    x = np.arange(1,n+1)
    result  = 0
    for e in x:
        result = result + wordlength(e)
    return result 

