#!/usr/bin/python

def fact(n):
    r = 1
    for i in range(2, n+1, 1):
        r = r * i
    return r

def rank(s):
    i = 0
    r = 0
    l = len(s)
    while i < l:
 #       print i
        s1 = s[i:]
        s2 = sorted(s1)
        k = {}
        for c in s2:
            if c not in k:
                k[c] = 0
            k[c] += 1

        tlen = len(s1)
        f_t = fact(tlen-1)
#        print s1, s2, fact(tlen-1)
        j = -1
        p = ''
#        print "index = ", s2.index(s1[0])
        for j in range(s2.index(s1[0])):
            if p == s2[j]:
                continue
            p = s2[j]
            f = f_t
            for v in k:
                f1 = k[v]
                if v == s2[j]:
                    f1 -= 1
                f = f/fact(f1)
#                print s2[j], v, f, f1, fact(f1)
            r += f
#            print "rank = ", r, s1[0], f
        i += 1
            
                
    print r+1

rank('ABAB')

#rank('BAAA')
#rank('QUESTION')
#rank('INDIA')
#rank('BOOKKEEPER')
