H = [1]
def hamming1(limit):
    h = [1] * limit
    x2, x3, x5 = 2, 3, 5
    i = j = k = 0
 
    for n in xrange(1, limit):
        h[n] = min(x2, x3, x5)
        if x2 == h[n]:
            i += 1
            x2 = 2 * h[i]
        if x3 == h[n]:
            j += 1
            x3 = 3 * h[j]
        if x5 == h[n]:
            k += 1
            x5 = 5 * h[k]
        print(h, i, j, k)
 
    print(h)
    return h[-1]

def hamming(n):
    i, j, k = 0, 0, 0
    for _ in range(n):
        v = min(2 * H[i], 3 * H[j], 5 * H[k])
        if v == 2 * H[i]: i += 1
        if v == 3 * H[j]: j += 1
        if v == 5 * H[k]: k += 1
        H.append(v)
#        print(H, (i, j, k))
    return H[n-1]

print(hamming1(19), hamming(19))
