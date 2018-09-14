"""
Description:

    The input is a string str of digits. Cut the string into chunks of size sz (ignore the last chunk if its size is less than sz).

    If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse it; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

    If

    sz is <= 0 or if str is empty return ""
    sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
    Examples:
    revrot("123456987654", 6) --> "234561876549"
    revrot("123456987653", 6) --> "234561356789"
    revrot("66443875", 4) --> "44668753"
    revrot("66443875", 8) --> "64438756"
    revrot("664438769", 8) --> "67834466"
    revrot("123456779", 8) --> "23456771"
    revrot("", 8) --> ""
    revrot("123456779", 0) --> ""
"""

def revrot(strng, sz):
    if sz <= 0 or sz > len(strng):
        return ""
        
    p = 0
    nstr=""
    while p+sz < len(strng):
        if sum([int(i)**3 for i in strng[p:p+sz]]) % 2 == 0:
            nstr += strng[p:p+sz][::-1]
        else:
            nstr += strng[p+1:p+sz] + strng[p]
        p += sz
        print nstr 
    return nstr
    # your code

s = "733049910872815764"
print revrot(s, 5)
