#!/usr/bin/python
import time

def sum_pairs(ints, s):
#    print ints
    start = time.time()
    dct = [(e, i) for i, e in enumerate(ints)]
    #zip(ints, [i for i in range(len(ints))]))
    dct.sort()
    l = 0
    h = len(ints) - 1
    rv = [h+1, h+1]
#    print dct
#    end = time.time()
#    print (end - start)
#    start = end
    while l < h:
        d1, d2 = dct[l], dct[h]
        cs = d1[0] + d2[0]
        #l += 1
        if cs > s:
            h -= 1
        elif cs < s:
            l += 1
        else:
            lp, hp = d1[1], d2[1]
            if lp < hp:
                l += 1
            else:
                h -= 1
                hp, lp = lp, hp
            if hp < rv[1]:
                if lp < rv[0]:
                    rv[0], rv[1] = lp, hp
            else:
                if lp >= rv[0]:
                    rv[0], rv[1] = lp, hp
#                print rv
            
#        print l, h
    end = time.time()
    print (end - start)
#    print dct
    return [ints[rv[0]], ints[rv[1]]] if rv[0] != rv[1] else None


a = [i for i in range(10000000)]
                      10000000

#print get_index([1,2,3,4,10,12,16], 15)
print (sum_pairs([4, -2, 3, 3, 4], 8))
print (sum_pairs([1, 4, 8, 7, 3, 15], 8))
print (sum_pairs([1, 2, 6, 2, 7, 15], 8))
print (sum_pairs(a, 10000003))
#print sum_pairs([1, 2, 3, 4, 1, 0], 2)
#print sum_pairs([1, 4, 8, 7, 3, 15], 8)
