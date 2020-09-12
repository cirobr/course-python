#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:33:30 2020

@author: ciro
"""

import numpy as np
zero_vector = np.zeros(5)
print(zero_vector, "\n")

zero_matrix = np.zeros((4,7))
print(zero_matrix, "\n")

x1 = np.ones(8)
x2 = np.empty((3,4))   # não inicializa os elementos do array, o que tem lá é lixo
print(x1, "\n")
print(x2, "\n")


x = np.array([1, 2, 3])
y = np.array([2, 4, 6])
print(x + y, "\n")


[1,3], [5,9]
[[1,3], [5,9]]
A = np.array([[1,3], [5,9]])
A
A.transpose()


X = np.array([[1,2,3], [4,5,6]])
print(X, "\n")

#referenciando linhas e colunas inteiras
X[:,1]
X[:,0]
X[1,:] == X[1]   # linha 1 inteira


# bolean indexing
z1 = np.array([1,3,5,7,9])
print(z1)
ind = z1 > 6
print(z1[ind], "\n")


# automated lists of elements
print(np.linspace(0, 100, 10), "\n")
print(np.logspace(0, 1, 10), "\n")   # 10 ** lista
print(np.logspace(np.log10(250), np.log10(500), 10), "\n")


X.shape
X.size


x = np.random.random(10)
np.any(x > 0.9)
np.all(x >= 0.1)
print(x, "\n")