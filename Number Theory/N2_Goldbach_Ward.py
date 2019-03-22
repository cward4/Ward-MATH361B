# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:05:06 2019

@author: caitl
"""

import numpy as np

N = 500

comp_list = []
odd_comp = []

prime_list = [2]

def prime_check(N):
    prime = True
    for i in range (2,int(np.sqrt(N))+1):
        mod = N%i
        if (mod != 0):
            prime = True
        elif (mod == 0):
            prime = False
            break
    return prime 

for ii in range (3, 10000):
    p = prime_check(ii)
    if(p  == True):
        prime_list.append(ii)
        if (len(prime_list) == N):
            break 
    else:
        comp_list.append(ii)

for k in range (len(comp_list)):
    modu = k%2
    if (modu != 0):
        odd_comp.append(k)

for l in range (len(odd_comp)):
    GB = False
    for m in range (len(prime_list)):
        for n in range (N):
            if (n == (np.sqrt(abs(l-m)))/2):
                GB = True
        if (GB == False):
            break
            print(l)



#c = p +2x^2
#sqrt( l-m)/2 = n








        
        