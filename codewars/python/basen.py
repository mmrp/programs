#!/usr/bin/python

def to_base_n(n, base):
    s = []
    while n > 1:
        s.append(str(n % base))
        n = n / base
    if n:
        s.append(str(n))
    return '.'.join(s[::-1])


def from_a_to_b_base(num, a, b):
    c = 0
    p = 1
    for i in num[::-1]:
        c = c * p + int(i) 
        p *= a
    print c
    return to_base_n(c, b)

n = int(raw_input("n : "))
a = int(raw_input("a : "))
b = int(raw_input("b : "))
print to_base_n(n, b)
#print from_a_to_b_base(str(n), a, b)
