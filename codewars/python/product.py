"""
find x, y from 1 import to n inclusive such that
x*y = n*(n+1)/2 - x - y
"""
def removNb(n):
    print(n)
    s = (n*(n+1))/2
    seq = []
    stop = n+1
    i = 1
    while i < stop:
        j = (s-i) / (1+i)
        if  j <= n and j * (1+i) + i == s:
            seq.append((i,j))
            if j < stop:
                stop = j
        i += 1

    seq.extend([(j, i) for i, j in seq])
    seq.sort(key=lambda x: x[1], reverse=True)
    return seq

#print removNb(1000003)
print removNb(input("n : "))
# should equal [(550320, 908566), (559756, 893250), (893250, 559756), (908566, 550320)]
