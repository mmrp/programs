
def toAscii85(data):
    def dec_radix85(n):
        q = []
        while n:
            q += [n % 85]
            n = n / 85
        q += [0] * (5 - len(q))
        return q[::-1]

    def convert(bytes, skip = 0):
        v = int(''.join(map(lambda x: bin(x)[2:].zfill(8), map(ord, bytes))),2)
        q = dec_radix85(v)
        return ''.join([chr(q[i] + 33) for i in range(len(q) - skip)])

    output = ""
    print(map(ord, data))
    end = 4 * ((len(data)+3)/ 4)
    remc = end - len(data)
    data += '\0' * remc
    bcopied = 0
    for i in range(0, len(data), 4):
        if ''.join(data[i:i+4]) == '\0\0\0\0':
            output += 'z'
            bcopied = 1
        else:
            output += convert(data[i:i+4])
            bcopied = 5
    if remc:
        output = output[:-bcopied] + convert(data[i:i+4])
    
    return '<~' + (output[:-remc] if remc else output) + '~>'
            
def fromAscii85(data):
    def radix85_dec(d):
        a = [85**4, 85**3, 85**2, 85, 1]
        return sum([a[i] * d[i] for i in range(len(a))])
        
    def convert(d):
        remc = 0
        if len(d) < 5:
            remc = 5 - len(d)
            d += 'u' * remc
        d = [ord(c) - 33 for c in d]
        v = radix85_dec(d)
        s = bin(v)[2:].zfill(32)
        return (''.join([chr(int(s[i:i+8], 2)) for i in range(0, len(s), 8)]), remc)

    output = ""
    
    #print(data)
    #end = 5 * ((len(data) + 4)/ 5)
    #remc = end - len(data)
    #data += 'u' * remc
    #data = [ord(c) - 33 for c in data]
    i = 0
    remc = 0
    data = ''.join(data.split())
    while i < len(data):
        print(data[i], i)
        if data[i] == 'z':
            output += '\0' * 4
            i += 1
            print('am here', i)
        else:
            out, remc = convert(data[i:i+5])
            output += out
            i += 5
    
    return output[:-remc] if remc else output
#print(fromAscii85('<~F)Po,GA(E,+Co1uAnbatCif~>'), 'somewhat difficult') 
print(fromAscii85('zH=_,8/T>`AAncL$A'))
print(fromAscii85('GA(]4ATMg !@q?d)ATMq'))
