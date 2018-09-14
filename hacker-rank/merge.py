def merge(a, b):
    la = len(a)
    lb = len(b)
    i, j, k = 0, 0, 0
    inv = 0
    while i < la and j < lb:
        if a[i] <= b[j]:
            c[k] = a[i]
            k += 1
            i += 1
        else:
            c[k] = b[j]
            k += 1
            j += 1
            inv += la - i
            
    if i == la:
        for p, v in enumerate(b[j:]):
            c[k+p] = v
        
    if j == lb:
        for p, v in enumerate(a[i:]):
            c[k+p] = v
        inv += len(a[j:])

    return inv

def mergesort(a, l, h):

    if h - l <= 1:
        return 0
    
    inv = 0
    m = (l+h)//2
    inv += mergesort(a, l, m)
    inv += mergesort(a, m, h)
    inv += merge(a[l:m], a[m:h])
    a[l:h] = c[:h-l]
    return inv

c = [0] * (10**5+10)
def count_inversions(a):
    inv = mergesort(a, 0, len(a))
    return inv

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(count_inversions(arr))
