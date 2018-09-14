import time
def sum_pairs(ints, s):
    #print ints
    s = time.time()
    p = 0
    l = len(ints)
    #print dct
    cur = [len(ints), len(ints)]
    p = 0
    dct = {}
    while p < cur[1]:
        v = ints[p]
        if s-v not in dct:
            for e, i in enumerate(ints[p:cur[1]]):
                if s-e not in dct:
                    dct[s-e] = i
                    if s == e + v:
                        break
            
        if s-v in dct and p < dct[s-v] and dct[s-v] <= cur[1]:
            cur[0], cur[1] = p, dct[s-v]
        
        p += 1
     #   print cur
     #   print p
    e = time.time()
    print(e-s)
    return [ints[cur[0]], ints[cur[1]]] if cur[0] != len(ints) else None


a = [i for i in range(10000000)]

print sum_pairs([1, 2, 4, 1, 0], 2)
print sum_pairs(a, 10000003)
#print sum_pairs([1, 4, 8, 7, 3, 15], 8)
