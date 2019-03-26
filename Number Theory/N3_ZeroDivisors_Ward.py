# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:08:24 2019

@author: caitl
"""

import numpy as np

m = 6

zero_div = np.zeros([0,2])

for ii in range(1,m-1):
    for jj in range(1,m-1):
        x = ii*jj
        mod = x%m
        if (mod == 0):
            zero_div = np.vstack([zero_div, np.array([ii,jj])])

div_list = zero_div.tolist()
print("The zero divisors for the group of integers modulo", m, " in the form [x,y] is", div_list,". The number of zero divisors for this group is",len(div_list)-1, ".")
            