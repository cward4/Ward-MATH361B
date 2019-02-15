# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:28:55 2019

@author: caitl
"""
N = 10000
m = 2
first_terms = [0,1]
list = []

for i in range(2,N):
    f = first_terms[i-1]+first_terms[i-2]
    first_terms.append(f)
    if f%m==0:
        list.append(f)

length = len(list)
percentage = (length/N)

print('Percentage of ', m, 'multiples is ', percentage)
