#!/usr/bin/python


def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

# should be 1 indexed
def heapify(a):
    n = len(a)-1
    for p in range(n/2, 0, -1):
        l = 2 * p
        if l < n and lt(a[l], a[l+1]):
            l += 1

        if gt(a[p], a[l]):
            down(a, p)

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def push_up(a, v, pos_arr):
    a.append(v)
    up(a, len(a) - 1, pos_arr)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l  
            pos[a[l][1]] = p  
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break        
 
def pop_down(a, pos):
#    print a
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1] 
    v = a.pop()
    down(a, 1, pos)
    return v[0]

def heapsort(a, pos):
    while len(a) != 1:
        yield pop_down(a, pos)    

from random import shuffle
#a = [i for i in range(10)]
a = [0, 3, 2, 1, 4, 5, 10, 12, 6, 7, -1, -3, 4]
#shuffle(a)
#heapify(a)
p = [i for i in range(len(a))]
q = [0]
print a
for i, v in enumerate(a[1:]):
    push_up(q, [v, i+1], p)
print q
for i in heapsort(q, p):
    print i,
#print
print p
print
