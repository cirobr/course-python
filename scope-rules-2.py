#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 13:36:58 2020

@author: ciro
"""

def increment(n):
    n += 1                   # pegadinha: n não é criado localmente
    #blank#
    #print("increment: ", n)
    return n                 # por isso precisa adicionar essa linha
    
n = 1    
while n < 10:
    #print("main_antes: ", n)
    n = increment(n)
    #print("main_depois: ", n)
print(n)