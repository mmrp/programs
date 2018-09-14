#!/usr/bin/pyton

from collections import Counter, defaultdict
import string
def count_atoms_rec(s, p):
    cnts = Counter()
    while p < len(s):
        print(p, len(s))
        v = s[p]
        if v in '{([':
            c, p = count_atoms_rec(s, p+1)
            cnts += c
        elif v in '}])':
            if s[p+1] in string.digits:
                for k in cnts.keys():
                    cnts[k] = cnts[k] * int(s[p+1])
                p += 1
            break
        else: #if v not in '123456789':
            while p < len(s) and s[p+1] in string.lowercase: 
                v += s[p+1]; 
                p += 1

            if s[p+1] in '23456789':
                cnts[v] += int(s[p+1]) - 1
                p += 1
            cnts[v] += 1
        p += 1
    return (cnts, p)
                
    
        
#count_atoms('H2O')
#count_atoms('K4[ON(SO3)2]2')
print(count_atoms_rec('(' + 'K4[ON(SO3BC1D2)2]2' + ')1', 0))
print(count_atoms_rec('(' + '()' + ')1', 0))
print(count_atoms_rec('(' + '(Mg2)' + ')1', 0))
print(count_atoms_rec('(' + '[(Uee4Mg2)2]5' + ')1', 0))
