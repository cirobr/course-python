import os 
import pandas as pd 
import numpy as np 
from collections import Counter


def count_words_fast(text): 
    text = text.lower() 
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"] 
    for ch in skips: 
        text = text.replace(ch, "") 
    word_counts = Counter(text.split(" ")) 
    return word_counts

def word_stats(word_counts): 
    num_unique = len(word_counts) 
    counts = word_counts.values() 
    return (num_unique, counts)


hamlets = pd.read_csv("./data/hamlets.csv", sep=",", index_col=(0))
print(hamlets.head(5), "\n")
print(hamlets.columns, "\n")

language, text = hamlets.iloc[0]
counted_text = count_words_fast(text)
print(counted_text["hamlet"])

data = pd.DataFrame(data=counted_text)
