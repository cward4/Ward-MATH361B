# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:03:12 2019

@author: caitl
"""
import turtle 

Do = "Fa"
N = 60

length = 10

for i in range(N):
    for char in Do:
        if char == 'a':
            Do = Do.replace('a','aRbFR')
        if char == 'b':
            Do = Do.replace('b','LFaLb')
    #print(Do)
    for ii in range(len(Do)):
       if Do[ii] == 'R': 
           turtle.right(90)
           turtle.forward(length)
       if Do[ii] == 'F':
            turtle.forward(length)
       elif Do[ii] == 'L': 
            turtle.left(90)
            turtle.forward(length)
            
###The code produces a memory error although it still produces a Do with the replacements 
###if you copy and paste lines 21-27 into the console after getting the error, it will produce
### the graphics in another window.