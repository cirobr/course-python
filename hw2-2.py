#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:34:22 2020

@author: ciro
"""

import numpy as np
import random

def create_board():
    empty_board = np.zeros((3,3), dtype = int)
    return(empty_board)

def place(board, player, position):
    if board[position] == 0:
        if player in range(1,3):
            board[position] = player
        else:
            print("jogador errado")
    else:
        print("ocupado")
    
    #print(board, "\n")

def possibilities(board):
    x = np.where(board == 0)
    x0 = list(x[0])
    x1 = list(x[1])
    n = len(x0)
    l = []
    for i in range(n):
        l.append((x0[i], x1[i]))
    return(l)

def random_place(board, player):
    possib = possibilities(board)
    pos = random.choice(possib)
    place(board, player, pos)
    return(pos)

def row_win(board, player):
    axis = 1
    x = np.equal(board, player)
    x = np.mean(x, axis = axis)   # axis = 1 >>> rows
    y = [i == 1 for i in x]
    y = sum(y) > 0
    return(y)

def col_win(board, player):
    axis = 0
    x = np.equal(board, player)
    x = np.mean(x, axis = axis)   # axis = 0 >>> columns
    y = [i == 1 for i in x]
    y = sum(y) > 0
    return(y)

def diag_win(board, player):
    n = len(board)
    x = np.equal(board, player)
    
    y1 = [x[i,i] for i in range(n)]
    y1 = ((sum(y1) == 3))
    
    y2 = [x[i,n-i-1] for i in range(n)]
    y2 = ((sum(y2) == 3))
    
    y = y1 | y2
    return(y)

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        win = row_win(board, player) | col_win(board, player) | diag_win(board, player)
        if win:
            winner = player
        pass
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner



# 10
random.seed(1)
def play_game():
    board = create_board()
    #print(board, "\n")
    winner = 0
    while (winner == 0):
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner >= 1:
                #print("Winner is: ", winner, "\n")
                break
            elif (winner == -1):
                #print("No Winner !!!", "\n")
                break
    return(winner)

results = []
for i in range(1000):
    res = play_game()
    results.append(res)

print("Player 1 wins: ", results.count(1))
print("Player 2 wins: ", results.count(2))
print("Ties: ", results.count(-1))



# 11
random.seed(1)
def play_strategic_game():
    board = create_board()
    #print(board, "\n")
    winner = 0
    place(board, 1, (1,1))
    random_place(board, 2)

    while (winner == 0):
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner >= 1:
                #print("Winner is: ", winner, "\n")
                break
            elif (winner == -1):
                #print("No Winner !!!", "\n")
                break
    return(winner)

results = []
for i in range(1000):
    res = play_strategic_game()
    results.append(res)

print("Player 1 wins: ", results.count(1))
print("Player 2 wins: ", results.count(2))
print("Ties: ", results.count(-1))
