
def determinant(M):
    n = len(M)
    if n == 2: return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    d = 0
    for i in range(n):
        m = [M[j][:i] + M[j][i+1:] for j in range(1, n)]
        r = determinant(m)
        d += (-1)**i * M[0][i] * r
    return d

    


m1 = [ [1, 3], [2,5]]
m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]
print(determinant(m2))
