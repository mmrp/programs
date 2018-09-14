
def get_index(pos, v):
    l = 0
    h = len(pos)-1

    if v < pos[0]:
        return 0

    if h == 0:
        return -1

    if v >= pos[0] and v < pos[1]:
        return 1

    if h == 1:
        return -1

    while l < h:
        m = (l+h)/2
        if pos[m] < v:
            l = m+1
        elif pos[m] > v:
            h = m-1
     #   print l, h
    
    r = l
    if pos[l] < v:
        if l == len(pos)-1:
            r = -1
        else:
            r = l+1
    return r
    
import time

def sum_pairs(ints, s):
    
    start = time.time()
    dct = {} 
    for p,v in enumerate(ints):
            dct[v] = -1
    end = time.time()
    print end - start
    start = end
    p = 0
    cur = [len(ints), len(ints)]
    while p < cur[1]:
        v = ints[p]
        if s-v in dct:
            pos = dct[s-v]
            tp = get_index(pos, p)
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


print get_index([1,2,3,4,10,12,16], 15)

#print sum_pairs([1, 4, 8, 7, 3, 15], 8)
print sum_pairs(a, 10000003)
print sum_pairs([1, 2, 3, 4, 1, 0], 2)
#print sum_pairs([1, 4, 8, 7, 3, 15], 8)
