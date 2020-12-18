# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 23:40:29 2020

@author: Alkapo
"""

import itertools

def getSomme(nlist,number,sumT):
      return [tup for tup in itertools.combinations(nlist, number) if sum(tup) == sumT]


_input = 'input.txt'
param = 2 
result = getSomme(nlist=[int(line.strip()) for line in open(_input, 'r')]
,number=param,sumT=sumt)
print(result[0][0]*result[0][1]*result[0][2])