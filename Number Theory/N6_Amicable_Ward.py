# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:04:59 2019

@author: caitl
"""

# =============================================================================
# d(n) = sum of the proper divisors of n 
# (n,m)
# d(n)=m and d(m)=n
# 
# =============================================================================


N= 300

def sum_propd(n):
    prop_div = []
    for i in range(1, int(n/2 + 1)):
        if n%i == 0:
            prop_div.append(i)
    sum_prop = sum(prop_div)
    return sum_prop 

amicable_nums = []

for a in range(1,N):
    d_a = sum_propd(a)
    for b in range(1,N):
        d_b = sum_propd(b)
        if d_a == b and d_b == a and a not in amicable_nums:
            amicable_nums.append(a)
            
print("The amicable numbers up to", N, "are:", amicable_nums)