#!/usr/bin/python

def next_version(str1):

    n = map(int, str.split("."))
    
    
    return '.'.join(map(str, n[::-1]))


print next_version("10.8.9")
