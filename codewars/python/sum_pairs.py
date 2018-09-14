import time
def sum_pairs(ints, s):
    #print ints
    s1 = time.time()
    p = 0
    l = len(ints)
    print l
    dct={}
    if s % 2 == 0:
        dct[s/2] = []
    for p, v in enumerate(ints[::-1]):
        if v not in dct:
            dct[v] = l-1-p
        elif v + v == s:
            dct[v].append(l-1-p)
# print dct
    cur = [l, l]
    p = 0 
    while p < cur[1]: 
        v = ints[p]
        if s-v in dct:
            endp = dct[s-v]
            if v + v == s:
                endp = p
                while dct[v] and endp <= p:
                    endp = dct[v].pop()
 #                   print endp

            if p < endp and endp <= cur[1]:
                cur[0], cur[1] = p, endp

        p += 1
    e1 = time.time()
    print(e1-s1)
    print  [ints[cur[0]], ints[cur[1]]] if cur[0] != l else None
    return [ints[cur[0]], ints[cur[1]]] if cur[0] != l else None

print sum_pairs([i for i in xrange(10)], 10-1)

def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)
