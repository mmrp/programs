#!/usr/bin/python

q = {1: [[1]]}
def partition(n):
    def generate(n):
        if n in q:
            return q[n]
        v = [[n]]
        for i in range(1, n):
            l = n - i
            for e in generate(i):
                if e[0] <= l:
                    v.append([l] + e)
        q[n] = v
        return v

    return generate(n)

def product(p):
    return list(sorted(set([reduce(lambda a, b: a * b , e, 1) for e in p])))

for i in range(1, 50):
    part = partition(i)
    prd  = product(part)
    l    = len(prd)
    print(prd)
    print "Range: %d Average: %.2f Median: %.2f" % (prd[-1] - prd[0], 
                            sum(prd)*1.0/l, 
                            prd[l/2]*1.0 if l % 2 else (prd[l/2-1] + prd[l/2])/2.0)
                
