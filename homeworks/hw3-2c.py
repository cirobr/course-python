# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 21:12:10 2020

@author: ciror
"""

def read_book(title_path):
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "")
        text = text.replace("\r", "")
    return text
