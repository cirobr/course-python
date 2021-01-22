import pandas as pd 
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
print(hamlets.head, "\n")
print(hamlets.columns, "\n")

language, text = hamlets.iloc[0]
counted_text = count_words_fast(text)
print(counted_text["hamlet"])

data = pd.DataFrame(data=list(counted_text.items()), columns=["word", "count"])
data.insert(loc=2, column="lenght", value=0)
data.insert(loc=3, column="frequency", value="")

def lf(w, c):
    l = len(w)
    
    if c > 10:
        f = "frequent"
    elif c == 1:
        f = "unique"
    else:
        f = "infrequent"
    
    return l, f

for ind in data.index:
    d = lf(data["word"][ind], data["count"][ind])
    data["lenght"][ind] = d[0]
    data["frequency"][ind] = d[1]
print(data.head(10))

# number of unique words
d1 = data[data.frequency == "unique"]
len(d1)

# create subdata
sub_data = data.groupby(['frequency']).agg({"count": "sum",
                                            "lenght": "mean"})
sub_data.insert(loc=0, column="language", value=language)
sub_data = sub_data.rename(columns = {"count" : "num_words",
                                      "lenght": "mean_word_length"})
