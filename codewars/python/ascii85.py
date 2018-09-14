#!/usr/bin/python3

def toAscii85(data):
    def dec_radix85(n):
        q = []
        while n:
            q += [n % 85]
            n = n / 85
        q += [0] * (5 - len(q))
        return q[::-1]

    def convert(bytes):
        v = int(''.join(map(lambda x: bin(x)[2:].zfill(8), map(ord, bytes))),2)
        q = dec_radix85(v)
        return ''.join([chr(q[i] + 33) for i in range(len(q))])

    output = ""
    end = 4 * ((len(data)+3)/ 4)
    remc = end - len(data)
    data += '\0' * remc
    for i in range(0, len(data), 4):
        output += convert(data[i:i+4])

    return '<~' + (output[:-remc] if remc else output) + '~>'
            
def fromAscii85(data):
    def radix85_dec(d):
        a = [85**4, 85**3, 85**2, 85, 1]
        return sum([a[i] * d[i] for i in range(len(a))])
        
    def convert(d):
        v = radix85_dec(d)
        s = bin(v)[2:].zfill(32)
        return ''.join([chr(int(s[i:i+8], 2)) for i in range(0, len(s), 8)])

    output = ""
    data = data[2:-2]
    end = 5 * ((len(data) + 4)/ 5)
    remc = end - len(data)
    data += 'u' * remc
    data = [ord(c) - 33 for c in data]
    for i in range(0, len(data), 5):
        output += convert(data[i:i+5])

    return output[:-remc] if remc else output
     
    pass


print(toAscii85('Man '))
print(toAscii85('easy') == '<~ARTY*~>')
print(toAscii85('somewhat difficult'))
print(fromAscii85('<~ARTY*~>'))
print(fromAscii85('<~F)Po,GA(E,+Co1uAnbatCif~>'))
print(toAscii85('\0'))

