# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:03:28 2019

@author: caitl
"""

# =============================================================================
# mk = n 
# m is a divisor of n
# m is a proper divisor of n iff 0<m<n
# =============================================================================


def divisors(n):
    prop_div = []
    for i in range(1, int(n/2 + 1)):
        if n%i == 0:
            prop_div.append(i)
    return prop_div 

print(divisors(12))