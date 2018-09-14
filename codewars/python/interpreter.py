def brain_luck(code, input):
    data = [0] * len(input)
    c, p, i = 0, 0, 0
    output = ""
    input = map(ord, input)
    while c < len(code) and p < len(input):
        move_next = 1
        if   code[c] == '>':  p += 1
        elif code[c] == '<':  p -= 1
        elif code[c] == '+':  
            data[p] += 1 
            if data[p] == 256: 
                data[p] = 0
        elif code[c] == '-':  
            data[p] -= 1 
            if data[p] == -1: 
                data[p] = 255
        elif code[c] == '.':  
            output += chr(data[p])
        elif code[c] == ',':  
            data[p] = input[i]
            i += 1
        elif code[c] == '[' and data[p] == 0:
            move_next = 0
            count = 1
            c += 1
            while count > 0:
                if code[c] == '[':
                    count += 1
                elif code[c] == ']':
                    count -= 1
                c += 1
        elif code[c] == ']' and data[p] != 0:
            move_next = 0
            count = 1
            c -= 1
            while count > 0:
                if code[c] == '[':
                    count -= 1
                elif code[c] == ']':
                    count += 1
                c -= 1
            c += 2
        if move_next == 1:
            c += 1      
    return output

c = brain_luck(',+[-.,+]', 'Codewars' + chr(255))
c = brain_luck('', '')
print(c)
