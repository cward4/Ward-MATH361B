# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 15:39:40 2019

@author: caitl
"""

import numpy as np 

n = 100
x = np.zeros((n))
z = np.zeros((n))
y = 0

for     i in range(1, n):
    x[i] = (np.log(i**4 + i + 3))/(np.sqrt(i) + 3)
    y = x[i] + y
    z[i] = y
#print('This is the first summation from 0 to 100 is ',y)

m = 10000
a = np.zeros((m))
c = np.zeros((m))
b = 0

for     i in range(1, m):
    a[i] = ((np.exp(i/100))/(i**10))
    b = a[i] + b
    c[i] = b
#print('This is the second summation from 0 to 10000 is ',b)
    
o = 10000
d = np.zeros((m))
f = np.zeros((m))
e = 0

for     i in range(1, o):
    d[i] = (i**2)
    e = d[i] + e
    f[i] = e
#print('This is the third summation from 0 to 10000 ',e)

firstf = z[1:16]
firstl = z[-15:]
secondf = c[1:16]
secondl = c[-15:]
thirdf = f[1:16]
thirdl = f[-15:]

print('The first 15 and last 15 terms of the first summation are ', np.append(firstf, firstl))
print('The first 15 and last 15 terms of the second summation are ', np.append(secondf, secondl))
print('The first 15 and last 15 terms of the third summation are ', np.append(thirdf, thirdl))
