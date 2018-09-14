
import math
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def sum_for_list(lst):
    print(lst)
    m = max(lst)
    m = m if m > 0 else -m
    maxp = math.sqrt(m) + 1
    first(maxp)
    
    dct = {}        
    for e in lst:
        get_factors(e, dct)
    
    return [[k, dct[k][1]] for k in sorted(dct)]
        
    print(dct)
        
def get_factors(e, dct):
    oe = e
    if e < 0:
        e = -e
    se = math.sqrt(e) + 1
    factors = []
    for v in data:
        if v > se:
            break
        while e % v == 0:
            e = e // v
            if v not in dct:
                dct[v] = [0, 0]
                
            if dct[v][0] == 0:
                dct[v][1] += oe
                dct[v][0] = 1
                
        if v in dct:
            dct[v][0] = 0
            
    if e != 1:
        if e not in dct:
            dct[e] = [0, 0]
        dct[e][1] += oe
    
    
    
def isprime(v):
    f = int(math.sqrt(v)) + 1
    for e in data[:f]:
        if v % e == 0:
            return False
    return True
                
def first(n):
    n = n if n > 0 else -n
    cur = len(data)
    p = data[-1] + 1
    while cur < n:
        if isprime(p):
            data.append(p)
            cur += 1
        p += 1
    
    
