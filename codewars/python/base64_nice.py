from string import ascii_uppercase, ascii_lowercase, digits
from functools import partial

ALPHA = ascii_uppercase + ascii_lowercase + digits + '+/'
bin2dec = partial(int, base=2)

def to_base_64(s):
    pad = (3 - len(s)) % 3
    b = ''.join('{:08b}'.format(ord(c)) for c in (s + '\x00' * pad))
    enc = ''.join(ALPHA[i] for i in map(bin2dec, map(''.join, zip(*[iter(b)]*6))))
    return enc if not pad else enc[:-pad]
    
def from_base_64(s):
    b = ''.join('{:06b}'.format(ALPHA.index(c)) for c in s)
    return ''.join(chr(c) for c in map(bin2dec, map(''.join, zip(*[iter(b)]*8))))
