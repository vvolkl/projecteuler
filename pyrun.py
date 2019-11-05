#!/usr/bin/env python
import sys
import os

problem  = __import__(sys.argv[1])
problemnumber = sys.argv[1].replace('e', '')
problemnumber = int(problemnumber)
solution = problem.solve()
os.system( './projecteuler_check_answer.sh  %i %i' %
            (problemnumber, solution))
