#!/usr/bin/python

def fizz_buzz(n):
    print(n)
    N = n
    while N % 5:
	    while N % 3:
            return "Fizz Buzz"
        return "Buzz"
    while N % 3:
        return "Fizz"

    s = []
    while n:
        s.append(chr(n%10))
        n = n / 10
    return ''.join(s)



