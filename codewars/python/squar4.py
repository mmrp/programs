#!/usr/bin/python3



def check(square, r, c,  conditions):
    v = square[r][c]

    for i in range(c):
        if v == square[r][i]:
            return False


    for i in range(r):
        if v == square[i][c]:
            return False
    
    def view_count(arr, s, e):
        c = 1
        g = arr[s]
        for i in range(s, e+1):
            if arr[i] > g:
                c += 1
                g = arr[i]
        return c

    rcond = conditions[0][r]
    if c == len(square)-1:
        rf = 1
        g = square[r][0]
        for i in range(1, c+1):
            if square[r][i] > g:
                g = square[r][i]
                rf += 1
        
        if rcond[0] and rf != rcond[0]: 
            return False

        rb = 1
        g = square[r][c]
        for i in range(c, -1, -1):
            if square[r][i] > g:
                g = square[r][i]
                rb += 1
        
        if rcond[1] and rb != rcond[1]: 
            return False
    
    if r == len(square)-1 and c == len(square)-1:
        ROWS = len(square)
        COLS = len(square)
        for i in range(COLS):
            cd = 1
            g = square[0][i]
            for j in range(ROWS):
                if square[j][i] > g:
                    g = square[j][i]
                    cd += 1

            if conditions[1][i][0] and cd != conditions[1][i][0]:
                return False

        for i in range(COLS):
            cu = 1
            g = square[ROWS-1][i]
            for j in range(ROWS-1, -1, -1):
                if square[j][i] > g:
                    g = square[j][i]
                    cu += 1

            if conditions[1][i][1] and cu != conditions[1][i][1]:
                return False
    
    return True

def solve(square, p, conditions):
    if p == len(square)**2: return True
    r = p / n
    c = p % n
    for j in range(1, n+1):
        square[r][c] = j
        if check(square, r, c, conditions) and solve(square, p+1, conditions):
            return True
    return False


 

#$clues = [ 3, 2, 2, 3, 2, 1, 1, 2, 3, 3, 2, 2, 5, 1, 2, 2, 4, 3, 3, 2, 1, 2, 2, 4];
#clues = [2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 2, 3, 3, 2, 1, 3]
#clues = [0, 0, 1, 3, 2, 0, 3, 0, 0, 0, 0, 3, 0, 2, 1, 3] #2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 2, 3, 3, 2, 1, 3]
clues = [2,2,0,2,0,0,1,0,0,0,0,0,1,0,0,0]
n = len(clues)/4
print(n)
square = [[0] * n for _ in range(n)]
conditions = []
conditions.append([(clues[4*n-1-i], clues[n+i]) for i in range(n)]) #top and bottom
conditions.append([(clues[0+i], clues[3*n-1-i]) for i in range(n)]) #left and right

solve(square, 0, conditions)
for e in square:
    print(e)
   
