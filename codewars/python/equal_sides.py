#!/usr/bin/python
"""you are going to be given an array of integers. Your job is to take that 
array and find an index N where the sum of the integers to the left of N is 
equal to the sum of the integers to the right of N. If there is no index that 
would make this happen, return -1.

For example:

    Let's say you are given the array {1,2,3,4,3,2,1}:
    Your function will return the index 3, because at the 3rd position of the 
    array, the sum of left side of the index ({1,2,3}) and the sum of the right 
    side of the index ({3,2,1}) both equal 6.

    Let's look at another one.
    You are given the array {1,100,50,-51,1,1}:
    Your function will return the index 1, because at the 1st position of the 
    array, the sum of left side of the index ({1}) and the sum of the right 
    side of the index ({50,-51,1,1}) both equal 1.

    Note: Please remember that in most programming/scripting languages the 
    index of an array starts at 0.

    Input:
"""
def find_even_index(arr):
    t = 0
    fsum = list()
    for e in arr:
        t = t + e
        fsum.append(t)
    l = len(arr)
    tsum = fsum[l-1]
    for i in range(0, l):
        if ((fsum[i]<<1) - tsum) == arr[i]:
            return i
    return -1

    


print find_even_index([1,2,8,4,5,6])
print find_even_index([1,2,3,4,3,2,1])
