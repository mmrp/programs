#!/usr/bin/python

def spiral(l, w):
    b = [[0 for i in range(w+2)] for j in range(l+2)]
    for r in range(0, l+2):
        for c in (0, w+1):
            b[r][c] = 1 

    for c in range(0, w+2):
        for r in (0, l+1):
            b[r][c] = 1

    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    si = 1
    sj = 1
    d = 0
    dx, dy = delta[d]
    while b[si][sj] == 0:
#        print si, sj
        b[si][sj] = d + 1
        if b[si + dx][sj + dy] != 0:
            d = (d + 1) % 4
            #print "changed ", d

        dx, dy = delta[d]
        si += dx
        sj += dy
    grid(b)
        #print si, sj, nsprl[si][sj]

def grid(g):
    l = len(g)-1
    w = len(g[0])-1
    line = ' ' + '*'.join(['---' for i in range(1, w)])
    s = [' > |', ' v |', ' < |', ' ^ |']
    print line
    for i in range(1, l):
        print '|' + ''.join(s[g[i][j]-1] for j in range(1, w))
        print line

print spiral(8, 7)
