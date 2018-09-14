import itertools
from collections import Counter
def numeric_palindrome(*args):
    m = 0
    for i in range(2, len(args)+1):
        for p in itertools.combinations(args, i):
            res = reduce(lambda x, y: x * y, p, 1)
            s = sorted(Counter(str(res)).items(), reverse = True)
            head = "".join(k * (c/2) for k, c in s)
            middle = max(k * (c%2) for k, c in s)
            p = int(head + middle + head[::-1])        
            if p > m: m = p
            print(p, res)
    return m
print(numeric_palindrome(10351, 708, 40542, 13213, 7051, 895))
#print(numeric_palindrome(39919, 0, 59, 2162, 2, 96100, 18666))
#print(numeric_palindrome(657, 892))
#print(numeric_palindrome(15, 125, 8))
#print(numeric_palindrome(937,113))
#print(numeric_palindrome(15, 125, 8))
#print(numeric_palindrome (39, 6, 48, 68, 48215, 8712, 929))

