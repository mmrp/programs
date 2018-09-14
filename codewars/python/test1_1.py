import time
def sum_pairs(ints, s):
    #print ints
    s1 = time.time()
    p = 0
    l = len(ints)
    dct={}
    dct[s/2] = []
    for p, v in enumerate(ints[::-1]):
        if v not in dct:
            dct[v] = l-1-p
        elif v == s/2:
            dct[v].append(l-1-p)
   # print dct
    cur = [l, l]
    p = 0
    while p < cur[1]:
        v = ints[p]
        if s-v in dct:
            endp = dct[s-v]
            if v == s/2:
                endp = p
                while dct[v] and endp <= p:
                    endp = dct[v].pop()
 #                   print endp

            if p < endp and endp <= cur[1]:
                cur[0], cur[1] = p, endp

     #   print cur
        p += 1
     #   print p
    e1 = time.time()
    print(e1-s1)
    return [ints[cur[0]], ints[cur[1]]] if cur[0] != l else None


a = [i for i in range(10000000)]

print sum_pairs([1, 2, 4, 1, 0], 2)
print sum_pairs(a, 10000000)
print sum_pairs([1, 4, 8, 7, 3, 15], 8)
