# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:29:24 2020

@author: ciror
"""

text = "Este é um texto que só tem texto como repetição. Mais um texto."

def count_words_fast(text):
    from collections import Counter
        
    text = text.lower()
    skips = [",", ".", ";", ":", "?", "'", '"', "!"]
    for ch in skips:
        text = text.replace(ch, "")
        
    word_counts = Counter(text.split(" "))
    return word_counts

x = count_words_fast(text)
print(x)