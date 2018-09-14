#!/usr/bin/python

""" 
1. find the smallest number from the lhs (if it is at the end, return)
2. find the next highest number compared to above as far as possible from the above index
3. Swap 1 and 2
"""
def next_number(num):
    print num,
    s = str(num)
    found = False
    entered = False
    for j in range(len(s)-1, 0, -1):
        for i in range(j-1, -1, -1):
            if s[j] > s[i]:
                if first:
                    l, m = i, j
                    entered = True
                found = True
                break

        if found:
            if i == l:
                if s[j] < s[m]:
                    l, m = i, j
            elif i > l:
                l, m = i, j
            found = False

    if not entered:
        return -1

    s = list(s)
    s[l], s[m] = s[m], s[l]

    return int(''.join(s[:l+1] + sorted(s[l+1:])))

print next_number(1223)
print next_number(1322)
print next_number(13233467001322)
print next_number(6543)
print next_number(59884848459853)
print next_number(459853)
   


