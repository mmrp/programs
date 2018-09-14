#!/usr/bin/python

def adjust(words, s, e, width):
    res = ""
    spaces = width - sum(map(len, words[s:e+1]))
    wlen = e - s    # we are gauranteed that a line has more than one word or fits perfectly
    if wlen == 0:
        return words[s] + '\n'

    minspace = spaces//wlen
    remspace = spaces - (minspace * wlen)
#    print (minspace, remspace)
    for w in range(s, e, 1):
        res += words[w] + ' ' * (minspace + (1 if remspace > 0 else 0))
        remspace -= 1
    res += words[e] + '\n'
    return res


#    print(s, e, spaces)

def justify(text, width):
    words = text.split()
    #print (words)
    s = 0
    e = len(words)
    m = 0
    result = ""
    while True:
        c = 0
        m = s
        while m < e:
            if c + len(words[m]) > width:
                break
            c += len(words[m]) + 1
            m += 1
        if m == e:
            result +=' '.join(words[s:m])
            break
        else:
            result += adjust(words, s, m-1, width)
        s = m
    return result

txt = """ Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor."""

print justify(txt, 15)
print justify('123 45 6', 7)
print justify('consectetur', 15)
