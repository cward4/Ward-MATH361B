# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:03:20 2019

@author: caitl
"""

P = [2,4,0,-1] #input polynomial  -(x**3)+4x+2    -8+8+2 = 2
x = 2 #point to be evaluated at 

G = [] #polynomial at point x
D = [] #derivative of polynomial     -3(x**2)+4    -12+4 = -8
M = [] 
a = 0
I = []


def p(x): #f(x) = -(x**3)+4x+2
    for i in range(len(P)): 
        l = x**i
        G.append(P[i]*l)
    return sum(G)

def P_deriv(x): #f'(x) = 3(x**2)+4
    for ii in range(len(P)): 
        h = P[ii]*ii 
        M.append(h) #[0,4,0,-3]
        N = M[1:] #[4,0,-3]
    for j in range(len(N)): #multiply by index then sum 
        k = x**j #[0,2,4]
        D.append(N[j]*k) 
    return sum(D)

def P_int(x): #int(f) = (-(x**4)/4)+2(x**2)+2x+C
    O = [a] + P #[0,2,4,0,-1] -(x**4)+4(x**2)+2x+C
    for ll in range(len(O)): 
        if O[ll]!= 0:
            O[ll] = O[ll]/ll #[0,2/1,4/2,0,-1/4] = #[0,2,2,0,-1/4]
    for jj in range(len(O)):
        f = x**jj #f = 1,2,4,8,16   
        I.append(O[jj]*f) #(-(x**4)/4)+2(x**2)+2x+C    [0,2,2,0,-.25]
    return sum(I)

print('The the polynomial evaluated at ', x, 'is' , p(x))
print('The derivative of the polynomial evaluated at ', x, 'is' , P_deriv(x))        
print('The integral of the polynomial evaluated at ', x, 'is' , P_int(x))


#polynomial division: 
#f= qg + r
#f/g = q + r/g