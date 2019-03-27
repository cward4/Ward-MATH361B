# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:39:53 2019

@author: caitl
"""

#mult inverse is when a*b=1

m = 20
mult_div = []

for ii in range(2,m-1):
    for jj in range(1,m-1):
        x = ii*jj
        mod = x%m
        if (mod == 1):
            mult_div.append(ii)

print("The multiplicative inverses of the", m, "set of integers is",mult_div,". This set has", len(mult_div), "inverses.")


