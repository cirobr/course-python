#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:16:10 2020

@author: ciro
"""

class MyList(list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))

x = [10, 3, 5, 1, 2, 7, 6, 4, 8]
print(x)
print(dir(x))

y = MyList(x)     # a lista y possui 2 métodos a mais que os métodos default para "list"
print(y)
print(dir(y))     # aparecem remove_min e remove_max como métodos de y