#!/usr/bin/python

# should be 1 indexed
def heapify(a):
    n = len(a)-1
    for p in range(n/2, 0, -1):
        l = 2 * p
        if l < n and a[l] > a[l+1]:
            l += 1

        if a[p] > a[l]:
            down(a, p)

def up(a, k):
    while k > 1 and a[k/2] > a[k]:
        a[k/2], a[k] = a[k], a[k/2]
        k = k / 2


def push_up(a, v):
    a.append(v)
    up(a, len(a) - 1)

def down(a, p):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and a[l] > a[l+1]: # l < n, says right exists
            l += 1

        if a[p] > a[l]:
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break        
 
def pop_down(a):
#    print a
    a[-1], a[1] = a[1], a[-1] 
    v = a.pop()
    down(a, 1)
    return v

def heapsort(a):
    while len(a) != 1:
        yield pop_down(a)    

a=[i for i in range(1000)]
from random import shuffle
shuffle(a)
#print a
#heapify(a)
q=[]
for i in a[1:]:
    push_up(q, i)
#print a
for i in heapsort(q):
    print i,
