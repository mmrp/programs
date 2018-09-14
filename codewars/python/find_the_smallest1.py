#!/usrbin/python
def smallest(n):
    print n,
    digits = map(int, str(n))
    for f in range(len(digits)):
        si = f
        flag = False
        for e in range(len(digits)-1, f, -1):
            if digits[si] > digits[e]:
                si = e 
            elif digits[e] == digits[f] and not flag:
                flag = True
                si = e
#        print si, f 
        if si != f:
            # abcdefgh
            if digits[si] == 0:
                ndigits = digits[:f] + digits[f+1:si+1] + digits[f:f+1] + digits[si+1:]
                si, f = f, si
            else:
                while digits[si] == digits[si-1]:
                    si -= 1
                ndigits = digits[:f] + digits[si:si+1] + digits[f:si] + digits[si+1:]
            if si == f + 1:
                si, f = f, si
            return [int(''.join(map(str, ndigits))), si, f]
    return []

print smallest(123456)
print smallest(123450)
print smallest(162235) #2, 0
print smallest(261235) #[126235, 2, 0]);
print smallest(209917) #[29917, 0, 1]);
print smallest(285365) #[238565, 3, 1]);
print smallest(269045) #[26945, 3, 0]);
print smallest(296837) #[239687, 4, 1]);
print smallest(187863002809)
print smallest(261235)
print smallest(209917)
print smallest(285365)
print smallest(269045)
print smallest(296837)
print smallest(187863002809)
print smallest(199819884756)
print smallest(94883608842)
print smallest(256687587015)
print smallest(935855753)
print smallest(1000003001)
print smallest(1100003001)
print smallest(1222222211)
