# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:22:02 2019

@author: caitl
"""

f = [1,-4,2] #coefficints of polynomial entered into list so that the index (0,1,2,..) matches the power of x
g = [2,2] #coefficints of polynomial entered into list so that the index (0,1,2,..) matches the power of x

def deflation(f,g):
    x = f[-1]%g[-1]
    if len(f) >= len(g) and x == 0:
        r = list.copy(f)
        y = f[-1]/g[-1]
        q = 0 + y
        gg = []
        rr = []
        for i in range(len(g)):
            gg.append((g[i])*y)
        for j in range(len(g)):
            rr.append(r[j]-gg[j]) 
        rr.append(r[-(len(f)-len(g))])
    return 'f(x)=', f , 'g(x)=', g,'the quotient is ', q,'the remainder is ', rr

print(deflation(f,g))

#(x+2)(2x^2-6x-3) = 