#!/usr/bin/python

def from_base_64(str):
    base64  = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    rbase64 = {v: p for p,v in enumerate(base64)}
    binstr  = ''.join("{0:06b}".format(rbase64[c]) for c in str)
    return ''.join("{0:c}".format(int('0b'+''.join(v), base=2)) for v in zip(*[iter(binstr)]*8))

def to_base_64(str):

    bin = {}
    rbin = {}
    for i in range(256):
        bin[i] = "{0:08b}".format(i)        # decimal to bin
        rbin[bin[i]] = i                    # bin to decimal

    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    binstr = ''.join(bin[ord(c)] for c in str)   # convert str to bin
    extra_char = (3 - len(str)) % 3
    binstr += bin[0] * extra_char       # append zeros

    tlen = len(binstr) - (extra_char) * 6 # skip the character(s) at the end
    cstr = ''.join(base64[rbin['00'+''.join(binstr[i:i+6])]] for i in range(0, tlen, 6))

#    cstr += '=' * extra_char
    return cstr

def to_base_641(str):
    pad = (3 - len(str)) % 3


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
