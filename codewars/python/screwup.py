#!/usr/bin/python

g = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? \n'
def encode(s):
    r = ''
    for p, c in enumerate(s):
        if c in g:
            r1 = g.index(c) + 1
            r2 = 2 ** (p+1)
            r3 = ((r1 * r2) % len(g)) - 1
            r += g[r3]
        else:
            r += c

    return r
        



def decode(s):
    r = ''
    for p, c in enumerate(s):
        r1 = 2**(p+1) % len(g)
        r2 = g.index(c) + 1
        if c in g:
            for e in g:
                if (r1 * (g.index(e)+1)) % len(g) == r2:
                    r += e
                    break
        else:
            r += c
    return r
print(len(g))
print(decode(encode(g[:66])) == g[:66]) #abcdefghijklmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVWYXZ'))
print(encode('?')) 
print(decode('bhx,zWyLZ3pOGIhzeXTYtjAaDWiO8miYH\n8U9y0SIAIF2ynwze,'))
