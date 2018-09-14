#!/usr/bin/python

dct = {}
def digitcount(n):
    N = n
    if n in dct:
        return dct[n]
    c = 0
    while n != 0:
        n = n / 10
        c += 1
    dct[N] = c
    return c

def brutecount(N):
    return sum([digitcount(i) for i in range(N+1)])


def brutecount2(N, s):
    return "".join([str(i) for i in range(1, N+10)]).index(s)

def count(N):
    if N < 10: return N
    n = digitcount(N) 
    arr = [0] * n
    for i in range(1, n):
        arr[i] = arr[i-1] + i * 9 * 10**(i-1)
    return arr[n-1] + n * (N - 10**(n-1) + 1) 

def findstring(s, n):
#    print('findstring', s, n)
    i = 0
    while i < len(s):
        if s[i] == '0': return None
        rlen = len(s) - i
        n += 1
        N = str(n)
        if len(N) > rlen:
            break
        if s[i:i+len(N)] != N: return None
        i += len(N)
   
    if rlen == 0 or (s[-rlen:] == N[:rlen]): return True
    
    return False


def cstring(s, start = 1):
    if s[0] == '0': return False, None
    n = len(s)
    for i in range(start, n):
        res = findstring(s[i:], int(s[:i]))
        if res: 
            return True, s[:i]
    return False, None

def pstring(s):
    res, val = cstring(s)
    if res: 
        print('found', val)
        return
    for i in range(1, 100000000):
#        print('trying', str(i) + s)
        res, val = cstring(str(i) + s, len(str(i)) + 1)
        if res:
            print('found', val)
            return val

        
        


            
#print(brutecount2(45, "454"))
#print(brutecount2(99, "99100"))
#print(cstring("454"), 79)
print(pstring("991"), 79)
print(pstring("910"), 188)
print(pstring("00101"), 190)
print(pstring("123456798"), 1000000071)
#for i in range(1, 0):
#    if i % 1000 == 0:
#        print(i)
#    if count(i) !=  brutecount(i):
#        print(i, count(i), brutecount(i))
#        break


