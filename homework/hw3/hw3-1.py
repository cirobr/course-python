# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:54:05 2020

@author: ciror
"""

def encoding(x_char, encode_key):
    import string
    alphabet = " " + string.ascii_lowercase
    values = list(range(27))

    positions = [(alphabet[i], values[i]) for i in values]
    positions = dict(positions)

    x_pos = positions[x_char]
    y_pos = x_pos + encode_key
    if y_pos > 26:
        y_pos = y_pos % 26 - 1
    y_char = [alphabet[i] for i in values if i == y_pos]
    y_char = y_char[0]
    return y_char

message = "hi my name is caesar"
encoded_message = [encoding(char, 1) for char in message]
msg = "".join(encoded_message)
print(msg)

decoded_message = [encoding(char, -2) for char in encoded_message]
msg = "".join(decoded_message)
print(msg)
