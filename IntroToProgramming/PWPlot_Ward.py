# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:11:54 2019

@author: caitl
"""
import numpy as np
import matplotlib.pyplot as plt
 
def f(x):
    if x < -2:
        f = -3*(x+2)**2 + 1
    elif -2 <= x and x < -1:
        f = 1
    elif -1 <= x and x <= 1:
        f = (x-1)**3 + 3 
    elif 1 < x and x <2:
        f = np.sin(np.pi * x) + 3
    else:
        f = 3 * np.sqrt(x - 2) + 4
    return f
N = 1000
x = np.linspace(-3,3, num = N)
y = np.zeros(N)
for i in range (N):
    y[i] = f(x[i])

plt.plot(x, y)