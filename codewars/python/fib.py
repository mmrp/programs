#!/usr/bin/python

import time
def repeated_squaring(a, p):
    st = time.time()
    c = 1
    b = a
    while p > 1:
        if p % 2 != 0:
            c = c * b
        b = b * b
        p = p / 2
    print c * b


    et = time.time()
    print (et - st)

def matrix_mul(A, B):
#    print A, B
#    print len(A), len(A[0])
    C = [[0 for i in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += (A[i][k] * B[k][j])
    return C


# matrix repeated squaring
def repeated_mat_squaring(A, p):
    st = time.time()
    c = [[1, 0], [0, 1]]
    b = A
    while p > 1:
        if p % 2 != 0:
            c = matrix_mul(c, b)
        b = matrix_mul(b, b)
        p = p / 2

    et = time.time()
    print (et - st)
    return (matrix_mul(c, b))

#a = int(raw_input("a: "))
#n = int(raw_input("n: "))
#matrix_mul([[1, 2],[3,4]], [[1], [2]])
#import sys
#sys.exit(0)

c = repeated_mat_squaring([[1, 1], [1, 0]], 1000000)
print matrix_mul(c, [[0],[1]])[0][0]
#repeated_squaring(a, n)
import sys
sys.exit(0)
#for i in range(21):
#    print(repeated_squaring(2, i))
