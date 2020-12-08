#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:55:04 2020

@author: ciro
"""

#2a
# write your code here
import math
print("Pi/4: %.6f" %(math.pi/4), "\n")


#2b
import random

random.seed(1) # Fixes the see of the random number generator.

def rand():
   # define `rand` here!
   res = random.uniform(-1, 1)
   return(res)

rand()
print("Rand:", rand(), "\n")


#2c
def distance(x, y):
   # define your function here!
   import math
   d = ((x[0]-y[0]) ** 2) + ((x[1] - y[1]) ** 2)
   d = math.sqrt(d)
   return(d)

distance((0,0), (1,1))
print("Distância:", distance((0,0), (1,1)), "\n")


#2d
def in_circle(x, origin = [0,0]):
   # Define your function here!
    res = (distance(x, origin)) <= 1
    return(res)

in_circle((1,1))


#2e
random.seed(1) 

# write your code here!
inside = []
R = 10000

for i in range(R):
    point = (rand(), rand())
    res = in_circle(point)
    inside.append(res)
    
print("Proporção:", sum(inside) / R, "\n")


#2f
# write your code here!
d = abs(sum(inside) / R - math.pi/4)
print ("Diferença: %.6f" %d, "\n")