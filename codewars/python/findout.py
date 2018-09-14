#!/usr/bin/python

def iq_test(str):
    oddness=[0, 0, 0, 0]
    for p, v in enumerate(str.split()):
        oddness[int(v)%2] = p+1
        oddness[int(v)%2 + 2] += 1

    if oddness[2] == 1:
        return oddness[0]
    else:
        return oddness[1]

print iq_test("2 4 7 8 10")# => 3 
