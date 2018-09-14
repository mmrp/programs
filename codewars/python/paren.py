#!/usr/bin/python
import itertools


"""
    for i in range(1, n-1):
        for e in f(i):
            for q in ["(" + e + ")" + p for p in f(n-1-i)]:
                arr.append(q)

        for e in f(n-1-i):
            for q in ["(" + e + ")" + p for p in f(i)]:
                arr.append(q)
"""
def f(n):
    if n <= 0: return [""]
    arr = []
    for e in f(n-1):
        arr.append("(" + e + ")")
    for i in range(1, n):
        for e in itertools.product(f(i), f(n-i)):
            arr.append(e[0] + e[1])
    return set(arr)

#!/usr/bin/python
g = {}
g[0] = ""
g[1] = ["()"]
def p(n):
    for e in range(2, n+1):
        g[e] = []
        for q in g[e-1]:
            g[e].append("(" + q + ")")
         
        for i in range(1, e):
           for q in itertools.product(g[i], g[e-i]):
                    v = q[0] + q[1]
                    if v not in g[e]:
                        g[e].append(v)
    return g[n] 

print(sorted(list(f(3))))
print(sorted(p(3)))
#print(p(4))
    

