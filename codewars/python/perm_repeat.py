#!/usr/bin/python


def prep(arr, repeat = 0):
    if repeat == 1: 
        return [[e] for e in arr]
    narr = []
    for e in arr:
        for q in prep(arr, repeat - 1):
            narr.append([e]+q)
    return narr

def permutation(arr):
    if len(arr) == 1:
        return [[arr[0]]]
    narr = []
    for i in range(len(arr)):
        arr[0],arr[i] =  arr[i], arr[0]
        for e in permutation(arr[1:]):
            narr.append([arr[0]] + e)
        arr[0],arr[i] =  arr[i], arr[0]
    return narr
        
#print(prep("123", 4))
print(len(permutation([1,2,3,4,5])))
