from math import sqrt
def factors(n):
    step = 2 if n%2 else 1
    return (reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, 
        step) if n % i == 0)))

print factors(int(raw_input("n : ")))
