#!/usr/bin/python

def find_num(arr):
    rsum = [sum(r[:-1]) for r in arr[:-1]]
    tarr = zip(*arr)
    csum = [sum(c[:-1]) for c in tarr[:-1]]

    row_sum = tarr[-1]
    col_sum = arr[-1]
    r = [p for p, v in enumerate(zip(rsum, row_sum[:-1])) if v[0] != v[1]]
    c = [p for p, v in enumerate(zip(csum, col_sum[:-1])) if v[0] != v[1]]

    if r and c: # inner elements
        r = r[0]
        c = c[0]
        return (row_sum[r] - (rsum[r] - arr[r][c]))
    elif r and not c:  
        r = r[0]
        return rsum[r] 
    elif c and not r:  
        c = c[0]
        return csum[c] 
    else:
        return sum(rsum)
        

print find_num([ [2 ,2 ,3 ,6 ],    
           [4 ,5 ,6 ,15],
           [7 ,8 ,9 ,24],
           [12,15,18,45] 
         ])

c = [[1 ,2 ,3 ,7 ], 
     [4 ,5 ,6 ,15], 
     [7 ,8 ,9 ,24], 
     [12,15,18,45]]    

c=[ [1 ,2 ,3 ,6 ], [4 ,5 ,6 ,15], [7 ,8 ,9 ,24], [12,15,18,46]] #     46 is not correct
print find_num(c)

