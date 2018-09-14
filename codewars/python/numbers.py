#!/usr/bin/python

def inc(n):
    s = map(int, str(n))
    f = s[0]
    for e in s[1:]:
        if f < e:
            return False
        f = e
    return True

def dec(n):
    s = map(int, str(n))
    f = s[0]
    for e in s[1:]:
        if f > e:
            return False
        f = e
    return True

def formula(d):
    count = {1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
    s = sum(count[1][:-1]) + sum(count[1][1:]) - 9
    for i in range(2, d+1):
        a = count[i-1]
        count[i] = [sum(a[:j+1]) for j in range(len(a))]
        s += sum(count[i][:-1]) + sum(count[i][1:]) - 9
    return s+1



print(sum(filter(lambda x: x, [inc(i) for i in range(1000, 10000)])))
print(sum(filter(lambda x: x, [dec(i) for i in range(100, 1000)])))
for i in range(1, 11):
    print(formula(i))
