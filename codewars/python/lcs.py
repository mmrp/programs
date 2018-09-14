def lcs(x, y):
    lx = len(x)
    ly = len(y)
    cnt = [[0 for i in range(ly+1)] for j in range(lx+1)]

    for i in range(1, lx+1):
        for j in range(1, ly+1):
            c = 0
            if x[i-1] == y[j-1]:
                c = 1 + cnt[i-1][j-1]
            cnt[i][j] = max(c, cnt[i-1][j], cnt[i][j-1])

    i = lx
    j = ly
    s = ''
    while i != 0 and j != 0:
        if x[i-1] == y[j-1]:
            s += x[i-1]
            i -= 1
            j -= 1
        elif cnt[i][j] == cnt[i-1][j]:
            i -= 1
        else:
            j -= 1

    return(s[::-1])
print(lcs("abcdef", "abc"))
print(lcs("how do you do boy", "do it body"))
print(lcs("a", "b"))
print(lcs("132535365", "123456789"))
