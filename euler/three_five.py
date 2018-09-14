import sys
def sum(a, d, N):
    n = N // d
    if N % d == 0:
        n -= 1
    return ((2 * a  + (n - 1) * d) * n)//2 if n > 0 else 0

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    s = sum(3, 3, n)
    print(s)
    s += sum(5, 5, n)
    print(s)
    s -= sum(15, 15, n)
    print(s)
    print(s)

