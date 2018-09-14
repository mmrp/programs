#!/usr/bin/python

""" 
1. find the smallest number from the lhs (if it is at the end, return)
2. find the next highest number compared to above as far as possible from the above index
3. Swap 1 and 2
"""
def next_number(num):
    print num
    s = str(num)
    m = [(v, i) for i,v in enumerate(s)]
    p = len(s)
    mi = (0, p)
    while p > 0 and mi[1] == p:
        mi = min(m[:p])
        p -= 1
    if p == 0:
        return ''

    p = mi[1]
    n = min([(v, i) for i, v in enumerate(s[p+1:]) if v > mi[0]])
    q = n[1] + p + 1
    while q < (len(s)-1) and s[q] == s[q+1]:
        q += 1
    l = list(s)
    l[p], l[q] = l[q], l[p]
    return int(''.join(l))

print next_number(1223)
print next_number(1322)
print next_number(13233467001322)
print next_number(6543)
   


