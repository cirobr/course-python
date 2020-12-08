def count_words(text):
    text = text.lower()

    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

from collections import Counter
def count_words_fast(text):
    text = text.lower()

    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    
    word_counts = Counter(text.split(" "))

    return word_counts



# main
text = "Este é um texto de teste para ver se esta merda funciona. Parece que funciona."

res = count_words(text)
print(res)

res2 = count_words_fast(text)
print(res == res2)