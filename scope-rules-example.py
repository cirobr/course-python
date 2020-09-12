#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:29:05 2020

@author: ciro
"""
# Scope Rules example
# LEGB

def update(n, x):
    n = 2                       # n is defined at this inner function, so n at outer level is unnafected
    x.append(4)                 # x is not defined here, so x is updated at the outer level
    print("update: ", n, x)
    
def main():
    n = 1
    x = [0, 1, 2, 3]
    print("main: ", n, x)
    update(n, x)
    print("main: ", n, x)

main()