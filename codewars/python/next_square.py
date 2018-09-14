#/usr/bin/env python3


def next(n, p):
    s1 = (n*(n-1)) % (10**p) 
    for d in range(0, 10):
        if (d*10**(p-1)*(2*n-1) + s1) % (10**p) == 0:
            return d

def get_next_series(f, count):
    for d in range(2, count+1):
        v = next(f, d)
        if v:
            f = 10**(d-1) * v + f
            yield(f)

if __name__ == '__main__':
    d = 3000
    total = [5, 6] + sorted(list(get_next_series(6, d)) + list(get_next_series(5, d)))
    print(len(total))
