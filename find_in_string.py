# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import string

x = "125,000"

# Solução For loop
status = True
for i in x:
    status = i in string.digits
    if status == True:
        print(i, status)
    else:
        break
print(i, status)

# Alternativas ao For loop
print(str.isalnum(x))

print(str.isdigit(x))