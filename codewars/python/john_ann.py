#!/usr/bin/python

"""
a = {}
j = {}
a[0] = 1
j[0] = 0
def r_john(n):
    if n in j:
        return j[n]
    j[n] = n - ann(john(n-1))
    return j[n]

def r_ann(n):
    if n in a:
        return a[n]
    a[n] = n - john(ann(n-1))
    return a[n]

"""

 
def get_john(n, a, j):
    a[0] = 1
    j[0] = 0
    for i in range(1, n+1):
        j[i] = i - a[j[i-1]]
        a[i] = i - j[a[i-1]]
    return j[n]

def john(n):
    a = [-1] * (n+1)
    j = [-1] * (n+1)
    get_john(n, a, j)
    return j[n]

def ann(n):
    a = [-1] * (n+1)
    j = [-1] * (n+1)
    get_john(n, a, j)
    return a[n]


def sum_john(n):
    a = [-1] * (n+1)
    j = [-1] * (n+1)
    get_john(n, a, j)
    return sum(j)


def sum_ann(n):
    a = [-1] * (n+1)
    j = [-1] * (n+1)
    get_john(n, a, j)
    return sum(a)

   

for i in range(11):
    print i, ann(i)
    
    return
    # your code
                
def sum_ann(n):
    return
    # your code


for i in range(11):
    print i, ann(i)
