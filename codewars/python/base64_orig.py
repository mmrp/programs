#!/usr/bin/python

import re


def from_base_64(str):
    bin = {}
    rbin = {}
    for i in range(256):
        bin[i] = "{0:06b}".format(i)        # decimal to bin
        rbin[bin[i]] = i                    # bin to decimal
    #print bin

    l = len(str)
    if str[l-2:] == '==':
        l -= 2
    elif str[l-1] == '=':
        l -= 1

    base64=[]           # base64 characters
    for i in range(26):
        base64.append(chr(65+i))    # A, B, C ...Z
    for i in range(26):
        base64.append(chr(97+i))    # a, b, c ...z
    for i in range(10):
        base64.append(chr(48+i))    # 0, 1, 2 ...9
   
    base64.append('+')      # '+'
    base64.append('/')      # '/'

    rbase64 = {}
    for p,v  in enumerate(base64):
        rbase64[v] = p


    binstr=''   # convert str to bin
    for c in str[:l]:
        binstr += bin[rbase64[c]]

    cstr = ''
    tlen = ((l * 6)/8) * 8
    for i in range(0, tlen, 8):
        cstr += "{0:c}".format(int('0b' + ''.join(binstr[i:i+8]), base=2))
  
#    print str, cstr
    return cstr




def to_base_64(str):

    bin = {}
    rbin = {}
    for i in range(256):
        bin[i] = "{0:08b}".format(i)        # decimal to bin
        rbin[bin[i]] = i                    # bin to decimal
    #print bin

    base64=[]           # base64 characters
    for i in range(26):
        base64.append(chr(65+i))    # A, B, C ...Z
    for i in range(26):
        base64.append(chr(97+i))    # a, b, c ...z
    for i in range(10):
        base64.append(chr(48+i))    # 0, 1, 2 ...9
   
    base64.append('+')      # '+'
    base64.append('/')      # '/'

    #print base64

    binstr=''   # convert str to bin
    for c in str:
        binstr += bin[ord(c)]

    extra_char = (3 - len(str)) % 3
    for i in range(extra_char):
        binstr += bin[0]       # append zeros


    tlen = len(binstr) - (extra_char) * 6 # skip the character(s) at the end

    cstr = ''
    for i in range(0, tlen, 6):
        cstr += base64[rbin['00' + ''.join(binstr[i:i+6])]]
  
#    cstr +=  '=' * extra_char
#   print len(str)
#    print str, cstr
    return cstr

to_base_64("any carnal pleasur")
to_base_64("pleasure.")
to_base_64("leasure.")
to_base_64("easure.")
to_base_64("asure.")
to_base_64("sure.")
s = to_base_64("ure.")
print s
print from_base_64(s)
print from_base_64(to_base_64("the quick brown fox jumps over the white."))

print from_base_64('TDRGK09UVU9IWVlDczBOaFpLOS9RUjRrWWhi')

print to_base_64('sGSI')
