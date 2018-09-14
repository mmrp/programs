#!/usr/bin/python

def merge(A, B, C):
    p, q = len(A), len(B)
    i, j = 0, 0
    res = []
    while i < p and j < q:
        if B[j][0] >= A[i][0]:
            res.append(B[j])
            j += 1
        else:
            k = A[i][1]
            C[k] += q - j
            res.append(A[i])
            i += 1

    if i < p: res += A[i:]
    if j < q: res += B[j:]
    return res


def mergesort(A, C):
    if len(A) == 1: return A
    m = len(A)/2
    A1 = mergesort(A[:m], C)
    B1 = mergesort(A[m:], C)
    A = merge(A1, B1, C)
    return A 

import random
arr = [(10,0), (6, 1), (3, 2), (7, 3), (6, 4), (1, 5), (3, 6), (10, 7), (10, 8), (7, 9)]#[(random.randint(0, 10), i) for i in range(10)]
C = [0]*10
print(arr)
res = mergesort(arr, C)
print(res)
print(C)
