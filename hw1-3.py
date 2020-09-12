# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 05:01:46 2020

@author: cirob
"""
from statistics import mean

# 3a
def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    #print(x)
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    #print(x)
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    md = []
    for i in range(n):
        y = x[i : i + width]
        m = mean(y)
        #print(y, m)
        md.append(m)
    
    return md

x = [0,10,5,3,1,5]
print(moving_window_average(x, 1))


# 3b
import random
random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.
    
# write your code here!
R = 1000
x = [random.random() for i in range(R)]

neighbors = 9
Y = []
for i in range(neighbors):
    Y = Y + moving_window_average(x, i+1)
    
n_list = 5
n_entry = 10
ind = n_list * R + n_entry
print(ind, Y[ind])


# 3c
# write your code here!
for i in range(neighbors):
    ind1 = i * R
    ind2 = ind1 + R - 1
    y = Y[ind1:ind2]
    y_min = min(y)
    y_max = max(y)
    y_range = y_max - y_min
    print(ind1, ind2, y_range)