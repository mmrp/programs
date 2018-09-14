    t = 0
    fsum = list()
    for e in arr:
        t = t + e
        fsum.append(t)
    t = 0
    bsum = list()
    for e in arr[::-1]:
        t = t + e
        bsum.append(t)
    
    l = len(arr)
    for i in range(0, l):
        if fsum[i] == bsum[l-1-i]:
            return i
