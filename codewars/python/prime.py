#!/usr/bin/python

import math
class primes:
    def __init__(self):
        self.data = [None] * 10000
        self.data[:10] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.cur = 10
        
        n = 30
        while self.cur < 10000:
            if self.isprime(n):
                self.data[self.cur] = n
                self.cur += 1
            n += 1
        
        self.last = self.data[-1]

    def isprime(self, v):
        f = int(math.sqrt(v)) + 1
        for e in self.data[:f]:
            if v % e == 0:
                return False
        return True

    def first(self, n):
        print n
        if n > self.last**2:
            return None

        if n < len(self.data):
            return [i for i in self.data[:n]]
        
        return  [i for i in self.data] + \
                [i for i in range(self.last+1, n) if isprime(i)]
            

p = primes()
print p.first(100)
