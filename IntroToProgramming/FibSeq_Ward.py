# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:41:17 2019

@author: caitl
"""

list = []
check = []
F_0 = 0
F_1 = 1
list.append(F_0)
list.append(F_1)
for i in range(2,100):
    list.append((list[(i-1)]) + (list[(i-2)]))

for i in range(len(list)-1):
    if ((list[i])**2) - (list[i-1]*list[i+1]) == (-1)**(i-1):
       check.append('T')
    else:
       check.append('F')

print(list)
print(check)


