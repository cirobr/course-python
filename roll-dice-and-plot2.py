#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:27:58 2020

@author: ciro
"""

import random
import matplotlib.pyplot as plt

ys = []
for rep in range (100000):
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
        
    ys.append(y)
    
plt.hist(ys)