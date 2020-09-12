#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:55:04 2020

@author: ciro
"""

# 1a
# write your code here!
import string
alphabet = string.ascii_letters


# 1b
sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
# write your code here!
for letter in sentence:
    if letter in alphabet:
        if letter not in count_letters:
            count_letters[letter] = 1
        else:
            count_letters[letter] += 1
    
print(count_letters, "\n")
x = list(count_letters)
print(x[3-1], x[8-1], "\n")
print(count_letters[x[3-1]], count_letters[x[8-1]], "\n")

# 1c
# write your code here!
def counter(input_string):
    import string
    alphabet = string.ascii_letters

    count_letters = {}
    for letter in input_string:
        if letter in alphabet:
            if letter not in count_letters:
                count_letters[letter] = 1
            else:
                count_letters[letter] += 1
    
    return(count_letters)

print(counter(sentence), "\n")


# 1d
address = """Four score and seven years ago our fathers brought forth on this continent, a new nation, 
conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a 
great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. 
We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final 
resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper 
that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- 
this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add 
or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. 
It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so 
nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored 
dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here 
highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of 
freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""

# write your code here!
address_count = counter(address)
print(address_count, "\n")


# 1f
# write your code here!
max_value   = max(address_count.values())
list_values = list(address_count.values())
list_index  = list_values.index(max_value)
list_keys = list(address_count.keys())
print("Most frequent character:", list_keys[list_index], "\n")
print(address_count["h"])
