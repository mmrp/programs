import math
class Primes:
    def __init__(self):
        pass
        
    @staticmethod
    def isprime(data, v):
        f = int(math.sqrt(v)) + 1
        for e in data[:f]:
            if v % e == 0:
                return False
        return True
        
    @staticmethod
    def first(n):
        data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        cur = len(data)

        p = 30
        while cur < n:
            if Primes.isprime(data, p):
                data.append(p)
                cur += 1
            p += 1

        return data


print Primes.first(50000)[-1]
