# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:15:58 2020

@author: ciror
"""


import random
import numpy as np
import matplotlib.pyplot as plt

rolls = []
for i in range(100):
    rolls.append(random.choice([1,2,3,4,5,6]))
plt.hist(rolls, bins = np.linspace(0.5, 6.5, 7))


ys = []
for rep in range (1000000):
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
        
    ys.append(y)
    
plt.hist(ys, bins = np.linspace(5.5, 60.5))
