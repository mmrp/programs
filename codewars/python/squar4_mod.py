#!/usr/bin/python3

def greater(arr, s, e):
    c = 1
    g = arr[s]
    for i in range(s, e+1):
        if arr[i] > g:
            c += 1
            g = arr[i]
    return c


def check(square, r, c, conditions, n):
    v = square[r][c]
    if v in square[r][:c]: 
        return False

    for i in range(r):
        if v == square[i][c]:
            return False
   
    #check row after col end is filled
    rf, rb  = conditions[0][r]
    if c == n - 1:
        if rf and rf != greater(square[r], 0, c):
            return False
        
        if rb and rb != greater(square[r][::-1], 0, c):
            return False
   
    #check all cols after last row is filled
    if r == (n-1) and c == (n-1):
        rows = n 
        cols = n 
        for col in range(cols):
            cd, cu = conditions[1][col]
            s  = [square[row][col] for row in range(rows)]

            if cd and cd != greater(s, 0, n-1):
                return False

            if cu and cu != greater(s[::-1], 0, n-1):
                return False
    
    return True

def solve(square, p, conditions, n):
    if p == n**2: return True
    r = p / n
    c = p % n
    for j in range(1, n+1):
        square[r][c] = j
        if check(square, r, c, conditions, n) and solve(square, p+1, conditions, n):
            return True
    return False


 

clues = [ 3, 2, 2, 3, 2, 1, 1, 2, 3, 3, 2, 2, 5, 1, 2, 2, 4, 3, 3, 2, 1, 2, 2, 4];
#clues = [2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 2, 3, 3, 2, 1, 3]
n = len(clues)/4
print(n)
square = [[0] * n for _ in range(n)]
conditions = []
conditions.append([(clues[4*n-1-i], clues[n+i]) for i in range(n)]) #top and bottom
conditions.append([(clues[0+i], clues[3*n-1-i]) for i in range(n)]) #left and right

solve(square, 0, conditions, n)
for e in square:
    print(e)
   
