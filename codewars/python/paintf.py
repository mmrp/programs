#!/usr/bin/python

def interpreter(code, iterations, width, height):
    forward = {}
    backward = {}
    stk = []
    for i in range(len(code)):
        if code[i] == '[': stk.append(i)
        if code[i] == ']': 
            f, b = stk.pop(), i
            forward[f] = b
            backward[b] = f
    
    tape = [[0] * width for _ in range(height)]
    r, c = 0, 0
    p = 0
    loops = 0
    while loops < iterations and p < len(code):
        r, c = r % height, c % width
        ch = code[p]
        if   ch == 'n': r -= 1
        elif ch == 's': r += 1
        elif ch == 'e': c += 1
        elif ch == 'w': c -= 1
        elif ch == '*': tape[r][c] = tape[r][c] ^ 1
        elif ch == '[': p = forward[p]  if tape[r][c] == 0 else p
        elif ch == ']': p = backward[p] if tape[r][c] != 0 else p
        else: loops -= 1
        p += 1
        loops += 1
   
    res = '\r\n'.join([''.join(map(str, tape[r])) for r in range(height)])
    return res 
print(interpreter("*[es*]", 9, 5, 6))
import sys
sys.exit(0)
print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 0, 6, 9))
print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 0, 6, 9))
#, displayExpected("000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000"), "Your interpreter should initialize all cells in the datagrid to 0")
print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 7, 6, 9))
#, displayExpected("111100\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000"), "Your interpreter should adhere to the number of iterations specified")
print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 19, 6, 9))
#, displayExpected("111100\r\n000010\r\n000001\r\n000010\r\n000100\r\n000000\r\n000000\r\n000000\r\n000000"), "Your interpreter should traverse the 2D datagrid correctly")
print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 42, 6, 9))
#, displayExpected("111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000"), "Your interpreter should traverse the 2D datagrid correctly for all of the \"n\", \"e\", \"s\" and \"w\" commands")
print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 100, 6, 9))
#, displayExpected("111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000"), "Your interpreter should terminate normally and return a representation of the final state of the 2D datagrid when all commands have been considered from left to right even if the number of iterations specified have not been fully performed")




