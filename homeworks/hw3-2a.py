# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:29:24 2020

@author: ciror
"""

text = "Este é um texto que só tem texto como repetição. Mais um texto."

def count_words(text):
    text = text.lower()
    skips = [",", ".", ";", ":", "?", "'", '"', "!"]
    for ch in skips:
        text = text.replace(ch, "")
        
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

x = count_words(text)
print(x)