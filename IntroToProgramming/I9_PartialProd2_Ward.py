# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:35:14 2019

@author: caitl
"""

import numpy as np

N = 100

x = np.zeros((N))
a = np.zeros((N))
y = 1

a_n = lambda n: (1 + (2*n/n**2))

for n in range(1,N):
    x[n] = a_n(n)
    y = y*(x[n])
    a[n] = y

firstf = a[1:16]
firstl = a[-15:]  
#print(np.append(firstf , firstl))

t = np.zeros((N))
o = np.zeros((N))
u = 1

b = 2  # b > 0

b_i = lambda i: 1 + b**i

for i in range(1,N):
    t[i] = b_i(i)
    u = u*(t[i])
    o[i] = u

secondf = o[1:16]
secondl = o[-15:]  
print(np.append(secondf, secondl)) 



