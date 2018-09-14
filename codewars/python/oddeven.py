#!/usr/bin/python

def even(num):
    glist=[]
    start = 0
    data = map(int, list(str(num)))
#    print data
    even = (data[0] % 2 == 0)
    for p,v in enumerate(data):
        if even and v % 2 == 0:
            continue
        if not even and v % 2 != 0:
            continue
       
        even = not even
        glist.append(int(''.join(map(str, data[start:p]))))
        start = p
#    print start, p
    if start < len(data):
        glist.append(int(''.join(map(str, data[start:len(data)]))))
    return glist

print even(123)
