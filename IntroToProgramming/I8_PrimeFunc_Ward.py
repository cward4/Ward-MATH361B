# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 20:36:10 2019

@author: caitl
"""

import numpy as np

N = 4

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

print(prime_check(200))
    
prime_list = [2]
for ii in range (3, 10000):
    p = prime_check(ii)
    if(p  == True):
        prime_list.append(ii)
        if (len(prime_list) == N):
            break

print("The", N, "prime number is", prime_list[-1])