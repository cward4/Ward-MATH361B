# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:28:55 2019

@author: caitl
"""

list = []
evens = []
mult_three =[]
mult_four =[]
prime = []
F_0 = 0
F_1 = 1
list.append(F_0)
list.append(F_1)
for i in range(2,10000):
    list.append((list[(i-1)]) + (list[(i-2)]))
for i in range(len(list)):
    if (((list[i]) % 2) == 0):
        evens.append(list[i])
    if (((list[i]) % 3) == 0):
        mult_three.append(list[i])
    if (((list[i]) % 4) == 0):
        mult_four.append(list[i]) 
#for ii in range(2,list[i]):
 #   if (list[i] >1 and list[i] % ii == 0):
  #      prime.append(list[i]) 

#print(len(evens))
print((len(evens)/10000)*100)
print((len(mult_three)/10000)*100)
print((len(mult_four)/10000)*100)

#print(len(prime))
