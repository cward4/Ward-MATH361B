# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 15:28:58 2019

@author: caitl
"""

import numpy as np 

n = 10000
x = np.zeros((n))
z = np.zeros((n))
y = 1

for     i in range(2, n):
    x[i] = (((i**3)-1)/((i**3)+1))
    y = y*(x[i])
    z[i] = y
#print(y)

o = 1000
a = np.zeros((o))
c = np.zeros((o))
b = 1

for     i in range(2, o):
    a[i] = ((np.exp(i/100))/(i**10))
    b = b*(a[i])
    c[i] = b
#print(b)

p = 1000
d = np.zeros((p))
f = np.zeros((p))
e = 1

for     i in range(2, p):
    d[i] = i
    e = e*(d[i])
    f[i] = e
#print(b)

firstf = z[2:16]
firstl = z[-15:]
secondf = c[2:16]
secondl = c[-15:]
thirdf = f[2:16]
thirdl = f[-15:]

print('The first 15 and last 15 terms of the first series are ', np.append(firstf, firstl))
print('The first 15 and last 15 terms of the second series are ', np.append(secondf, secondl))
print('The first 15 and last 15 terms of the third series are ', np.append(thirdf, thirdl))
