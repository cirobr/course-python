#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:58:58 2020

@author: ciro
"""

# 1
import numpy as np
def create_board():
    empty_board = np.zeros((3,3), dtype = int)
    return(empty_board)

# 2
def place(board, player, position):
    if board[position] == 0:
        if player in range(1,3):
            board[position] = player
        else:
            print("jogador errado")
    else:
        print("ocupado")
    
    print(board, "\n")

board = create_board()
print(board, "\n")

place(board, 1, (0,0))

# 3
def possibilities(board):
    x = np.where(board == 0)
    x0 = list(x[0])
    x1 = list(x[1])
    n = len(x0)
    l = []
    for i in range(n):
        l.append((x0[i], x1[i]))
    return(l)
    
print(possibilities(board))

# 4
import random
random.seed(1)

def random_place(board, player):
    possib = possibilities(board)
    pos = random.choice(possib)
    place(board, player, pos)
    return(pos)

random_place(board, 2)
