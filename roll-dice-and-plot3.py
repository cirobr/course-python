#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:05:17 2020

@author: ciro
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(7, size = (10000,6))
print(x)
y = np.sum(x, axis = 1)
print(y)

plt.hist(y)