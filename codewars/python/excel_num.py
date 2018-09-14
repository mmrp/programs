#!/usr/bin/python

def get_column_title(num):
    str = ""
    while num:
        q = (num-1) % 26
        str += chr (65 + q)
        num = (num-1)/26
    return str[::-1]


print get_column_title(input("num : "))
