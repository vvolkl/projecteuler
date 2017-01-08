
from collections import OrderedDict
import itertools
import numpy as np

def intersect(l1, l2):
  return [val for val in l1 if val in l2]

def solve():
  func2s = OrderedDict()
  func2s["Triangle"] = lambda n: n * (n + 1) / 2
  func2s["Square"] = lambda n: n*n
  func2s["Pentagonal"] = lambda n: n * (3*n - 1) / 2
  func2s["Hexagonal"] = lambda n: n * (2*n - 1)
  func2s["Heptagonal"] = lambda n: n * (5*n - 3) / 2
  func2s["Octagonal"] = lambda n: n * (3*n - 2)
  for item in itertools.permutations(func2s.items()):
    funcs = OrderedDict(item)
    numbers = {}
    numbers_end = {}
    numbers_start = {}
    connection_counts = {}
    connection_counts_backward = {}
    for j,n in enumerate(funcs.keys()):
      print j,n
      numbers[n] = []
      numbers_start[n] = []
      numbers_end[n] = []
      connection_counts[n] = {}
      connection_counts_backward[n] = {}
      i = 1
      fi = 1
      while fi < 10000:
        fi = funcs[n](i)
        if fi > 999 and fi % 100 > 10:
          numbers[n].append(fi)
          numbers_start[n].append(fi % 100)
          numbers_end[n].append(int(fi / 100))
          if n == funcs.keys()[0]:
            connection_counts[n][int(fi % 100)] = 0
          
          else:
            try:
              if n == funcs.keys()[1]:
                if connection_counts[funcs.keys()[j-1]][fi / 100] == 0:
                  connection_counts[n][int(fi % 100)] = 1
                  connection_counts[funcs.keys()[j-1]][fi % 100] = 1
              else:
                if connection_counts[funcs.keys()[j-1]][fi / 100] == 1:
                  connection_counts[n][int(fi % 100)] = 1
              print n, fi, [a for a in numbers[funcs.keys()[j-1]] if a % 100 == fi / 100] 
              print "\t", numbers[funcs.keys()[j-1]]
            except KeyError:
              print 'passing'
              pass
        i = i + 1

    #for e in connection_counts[funcs.keys()[-1]].keys():
    #  print e
    #  
    #  if e in connection_counts[funcs.keys()[0]]:
    #    print [a for a in numbers[funcs.keys()[0]] if  connection_counts[funcs.keys()[0]][e] == 1]
    


    print connection_counts
    f = funcs.keys()[::-1]
    for j,n in enumerate(f):
      print j,n
      i = 1
      fi = 1
      while fi < 10000:
        fi = funcs[n](i)
        if fi > 999:
          try:
            if j == 0:
              print connection_counts_backward
              print connection_counts[n].keys(), fi
              if fi % 100 in connection_counts[n].keys():
                connection_counts_backward[n][fi / 100] = connection_counts[n][fi % 100]

            else:
              print fi
              if connection_counts_backward[f[j-1]][fi % 100] == 1:
                connection_counts_backward[n][int(fi / 100)] = 1
              print n, fi, [a for a in numbers[f[j-1]] if a / 100 == fi % 100] 
              print "\t", numbers[f[j-1]]
          except KeyError:
            print 'passing'
            print connection_counts_backward[n]
            pass
        i = i + 1

    for e in  connection_counts_backward[f[-1]].keys():
      print e, connection_counts[f[0]].keys()
      if e in connection_counts[f[0]].keys():
        print "success!"
        #todo: add all previous numbers:
        return 1


  return 1

solve()
