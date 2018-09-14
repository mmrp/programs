import math
primes=[ 2, 3, 5, 7, 11, 13, 17]
def isprime(p):
    for i in primes:
        if p % i == 0:
            return False
    return True

def get_primes(n):
    i = primes[len(primes)-1] + 2
    m = int(math.sqrt(n)) + 2
    for i in range(i, m, 2):
        if isprime(i):
            primes.append(i)
    # your code
    return (sol)



from math import sqrt
def factors(n):
    step = 2 if n%2 else 1
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


def sol_equa(n):
    sol = list()
    f = list(factors(n))
    f.sort()
    print f
    e = f[-1]
    for v in f:
        if v >= e:
            break
        e = n/v
        a = v
        b = e
        if (a - b) % 4 == 0:   
            if a > b:
                b, a = a, b
            sol.append([(a+b)/2, (b-a)/4])
    return sol

def sol_equa1(n):
    sol = list()
    print n
    if n > 9000000041:
        return []
    inc = 2
    if n % 2 == 0:
        inc = 1
        
    end = n
    i = 1
    while i < end:
        if n % i == 0:
            b = n/i
            end = b
            if (i - n/i) % 4 == 0:   
                a = i
                if a > b:
                    b, a = a, b
                print i, end
                sol.append([(a+b)/2, (b-a)/4])
        i += inc
    # your code
    return (sol)

import time
s = time.time()
print sol_equa1(int(raw_input("n:")))
print sol_equa(int(raw_input("n:")))
e = time.time()
print (e-s)
