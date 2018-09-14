#!/usr/bin/python

def peak(arr):
    end = len(arr) - 1
    arr += [max(arr) + 1]
    pos = 1
    items = []

    print(end, arr)
    while pos < end:
        if arr[pos] > arr[pos-1]:
            if arr[pos] > arr[pos+1]:
                items += [pos]
                print('h s: %d' % pos)
                pos += 2
            elif arr[pos] == arr[pos+1]:
                    while (arr[pos] == arr[pos+1]): pos += 1
                    if arr[pos] > arr[pos+1]:
                        items += [pos]
                        print('s: %d' % pos)
                        pos += 2
                    else:
                        pos += 1
            else:
                pos += 1
        else:
            pos += 1
    return [arr[v] for v in items], items

print(peak([1,2,2, 2, 1,4,5,1,2,3,4,5,6,1]))
