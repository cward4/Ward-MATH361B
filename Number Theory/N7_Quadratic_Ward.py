# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:03:01 2019

@author: caitl
"""

import numpy as np 

P = 65

def prime_check(N):
    prime = True
    for i in range (2,N):
        mod = N%i
        if (mod != 0):
            prime = True
        elif (mod == 0):
            prime = False
            break
    return prime 

p_primes = []

for i in range(P):
    prime = prime_check(i)
    if prime == True:
        p_primes.append(i)

x = np.zeros([0,2])

for p in p_primes:
    quad_res = [0]
    for n in range(p):
        for k in range(p):
            if (k**2)%p == n and n not in quad_res:
                quad_res.append(n)
    x = np.vstack([x, np.array([p,len(quad_res)])])

print('Zp has has the following number of quadratic residues')
print(x)

neg_one = np.zeros([0,2])

for m in p_primes:
    neg = False
    for k in range(m):
        if (k**2)%p == (p-1):
            neg_one = np.vstack([neg_one,np.array([m, 'yes'])])
            break
    else:
        neg_one = np.vstack([neg_one,np.array([m, 'no'])])

print('Is -1 a quadatic residue of Zp?', neg_one)



#265, 220, 116 and 117, newton method julia set, fractials, 173