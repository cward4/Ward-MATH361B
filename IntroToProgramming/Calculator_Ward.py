# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 12:38:46 2019

@author: caitl
"""

x = 5
y = 2
z = 1 

mylist = []

mylist.append(x + 1)
mylist.append((y*z)+(3*x))
mylist.append((mylist[0])**2)
mylist.append(((2*(mylist[1]))-(x/2))/(mylist[0]))
mylist.append(7/3)

mylist[2] += 3
mylist[4] *= (3/4)
print('The sum of all the components is', sum(mylist))