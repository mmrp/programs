#!/usr/bin/python


def sequence(a):
    D = [0] * len(a)

    D[0] = 1
    for i in range(1, len(a)):
        D[i] = max([1] + [D[j]+1 for j in range(i) if a[i] > a[j]])
    print(D)
    return max(D)        
            



n = int(input().strip())
#a = list(map(int, input().strip().split(" ")))
a = [0] * n
for i in range(n):
    a[i] = int(input().strip())
print(sequence(a))
