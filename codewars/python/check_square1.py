#!/usr/bin/python
n = 6
import sys
import itertools

def get_set(perm, n):
    s = [set([]) for _ in range(n)]
    for g in perm: 
        for p, v in enumerate(g): 
            s[p].add(v)
    return s 


    s = [set([]) for _ in range(6)]
    if not(a1) and not(a2):
        return [set(range(1,7)) for _ in range(6)]

    for e in perm.keys():
        l = perm[e]
        f, b = e
        if (not(a1) and b == a2) or (f == a1 and not(a2)) or (f == a1 and b == a2):
            for p, v in enumerate(l):
                s[p].add(v)
       
    return s if all(s) else []

perm_all = {}
def generate_all_permutations(size):
    def greater(s):
        g = s[0]
        count = 1
        for e in s:
            if e > g:
                count += 1
                g = e
        return count

    perm_all[(0,0)] = []
    for e in list(itertools.permutations(range(1, size+1))):
        f, b = greater(e), greater(e[::-1])
        if (f,b) not in perm_all:
            perm_all[(f,b)] = []
        perm_all[(f,b)].append(e)
        perm_all[(0,0)].append(e)

    for i in range(1, size+1):
        res = []
        for j in range(1, size+1):
            if (i, j) in perm_all:
                for e in perm_all[(i, j)]:
                    res.append(e)
        if res:
            perm_all[(i,0)] = res

    for i in range(1, size+1):
        res = []
        for j in range(1, size+1):
            if (j, i) in perm_all:
                for e in perm_all[(j, i)]:
                    res.append(e)
        if res:
            perm_all[(0,i)] = res

generate_all_permutations(6)
#print(get_set(perm_all[(1,3)], 6))
print(perm_all[(2,4)])
print(perm_all[(2,2)])
import sys
args = map(int, sys.argv[1:])
def get_map(a,b,c,d,e,f):
    print(a,b,c,d,e,f)
    s1 = get_set(perm_all[(a,b)], 6)
    s2 = get_set(perm_all[(d,e)], 6)
    def print_set(s1):
        for i in range(6):
            print i, list(s1[i])
    print_set(s1)
    print_set(s2)
    print(c, f, s1[c-1] & s2[f-1]) 


get_map(*args)
