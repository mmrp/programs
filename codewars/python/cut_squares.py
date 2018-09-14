#!/usr/bin/python
"""The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).



Can you translate this drawing into an algorithm?

You will be given two dimensions

a positive integer length (parameter named lng)
a positive integer width (parameter named wdth)
"""

def sqInRect(a, b):
    if a == b:
        return None
    lst = []
    while a != b:
        c = min(a, b)
        if a == c:
            b = b - c
        else:
            a = a -c 
        lst.append(c)

    lst.append(a)
    return lst
        
print(sqInRect(300, 120)) #input("len = "), input("wid = "))
