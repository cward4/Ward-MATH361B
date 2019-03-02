# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:45:58 2019

@author: caitl
"""

import numpy as np

N = 400
x = np.zeros([0,4])

for ii in range(1,N):
    for jj in range(ii,N):
            y = ii**2 + jj**2
            c = np.sqrt(y)
            d = ii + jj + c
            if (c.is_integer() == True): #and (ii < jj < np.sqrt(y))):
                x = np.vstack([x, np.array([ii,jj,c,d])])
                if (d == 1026):
                    print('The Pythagorean Triple for which the sum is 1026 is a=', ii, 'b =', jj, 'and c=', c)
