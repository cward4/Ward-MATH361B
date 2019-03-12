# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:59:19 2019

@author: caitl
"""
a0 = 400
N = 20

my_list = []
my_list.append(a0)

for i in range (N):
    if (my_list[i] == 1):
        print('This sequence starting with',a0, 'took', len(my_list)-1, 'terms before reaching 1.')
        break
    if (my_list[i]%2 == 0):
        my_list.append(my_list[i]/2)
    if (my_list[i]%2 != 0):
        my_list.append((3*my_list[i])+1)
if 1 not in my_list:
    print('This sequence starting with',a0, 'with', N,'terms does not reach 1.')