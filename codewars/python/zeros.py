import math
def calculate_primes(n):
    primes = []
    print(n)
    for i in range(2, n+1):
        found = True
        last = math.ceil(math.sqrt(i))
        p, j = 1, 0
        while j < len(primes) and p < last:
            p = primes[j]
            if i % p == 0:
                break
            j += 1
        else:
            primes.append(i)
    return primes

def factorize(num, primes):
    f = []
    i = 0
    while num > 1 and i < len(primes):
        p = primes[i]
        c = 0
        while num % p == 0:
            num /= p
            c += 1
        if c: f.append((p, c))
        i += 1
    if num != 1:
        f.append((num, 1))
    return f

primes = calculate_primes(int(1+math.sqrt(900719925474)))
def trailing_zeros(n, b):
    factors = factorize(b, primes)
    m = []
    for p, c in factors:
        c1 = 0
        tn = n
        while tn:
            tn = tn/p
            c1 += tn
        c1 = c1 / c
        m.append(c1)
    return min(m)
