
def solve(verbose=False):
  results = []
  # take all reasonable value for the two 
  # factors a b 
  for a in xrange(1, 9999):
      for b in xrange(1,min(a,100)):
          t = str(a) + str(b)
          #first check: there are no repeat digits 
          # in the factors 
          if len(set(t)) == len(t):
              prod  = a * b 
              t = t + str(prod)
              if verbose:
                print  t
              # checks on all three numbers together: 
              if '0' not in t:
                if len(t) == 9:
                  if len(set(t)) == 9:
                    if verbose:
                      print ("found pandigital " 
                            " %i * %i = %i" % (a, b, prod))
                    # found one, store it, repeat ...
                    results.append(prod)
  # count all pandigital lists only once
  result = np.sum(np.unique(results))
  return result

