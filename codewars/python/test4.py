import time
def sum_pairs(ints, s):
    
    start = time.time()
    dct = {} 
    for p,v in enumerate(ints):
        dct[s-v] = []

    end = time.time()
    print end - start
    start = end
    p = 0
    return None
    cur = [len(ints), len(ints)]
    while p < cur[1]:
        v = ints[p]
        if s-v in dct:
            pos = dct[s-v]
    #        print pos, p, tp
            if tp == -1:
                p += 1
                continue
            ep = pos[tp]
            if ep < cur[1]:
                cur[0], cur[1] = p, ep
        p += 1
    end = time.time()
    print end - start
    return [ints[cur[0]], ints[cur[1]]]


a = [i for i in range(10000000)]



#print sum_pairs([1, 4, 8, 7, 3, 15], 8)
print sum_pairs(a, 10000003)
print sum_pairs([1, 2, 3, 4, 1, 0], 2)
#print sum_pairs([1, 4, 8, 7, 3, 15], 8)
