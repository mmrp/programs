#!/usr/bin/python
"""
0-9 Push this number onto the stack.
+ Addition: Pop a and b, then push a+b.
- Subtraction: Pop a and b, then push b-a.
* Multiplication: Pop a and b, then push a*b.
/ Integer division: Pop a and b, then push b/a, rounded down. If a is zero, push zero.
% Modulo: Pop a and b, then push the b%a. If a is zero, push zero.
! Logical NOT: Pop a value. If the value is zero, push 1; otherwise, push zero.
` Greater than: Pop a and b, then push 1 if b>a, otherwise push zero.
> Start moving right.
< Start moving left.
^ Start moving up.
v Start moving down.
? Start moving in a random cardinal direction.
_ Pop a value; move right if value = 0, left otherwise.
| Pop a value; move down if value = 0, up otherwise.
" Start string mode: push each character's ASCII value all the way up to the next ".
: Duplicate value on top of the stack. If there is nothing on top of the stack, push a 0.
\ Swap two values on top of the stack. If there is only one value, pretend there is an extra 0 on bottom of the stack.
$ Pop value from the stack and discard it.
. Pop value and output as an integer.
, Pop value and output the ASCII character represented by the integer code that is stored in the value.
# Trampoline: Skip next cell.
p A "put" call (a way to store a value for later use). Pop y, x and v, then change the character at the position (x,y) in the program to the character with ASCII value v.
g A "get" call (a way to retrieve data in storage). Pop y and x, then push ASCII value of the character at that position in the program.
@ End program.
(i.e. a space) No-op. Does nothing.
The above list is slightly modified: you'll notice if you look at the Wikipedia page that we do not use the user input instructions and dividing by zero simply yields zero.
"""
import random
def interpret(code):
    print(code)
    grid = [[' '] * 80 for _ in range(25)]
    print(code.split('\n'))
    lines = code.split('\n')
    for i, l in enumerate(lines):
        print(l, len(l))
        for j, c in enumerate(l):
            grid[i][j] = c
    #print(grid)
    x, y = 0, -1
    dx = 0
    dy = 1
    output = ""
    stack = []
    stringmode = False
    steps = 0
    while True:
        x = (x + dx) % 25
        y = (y + dy) % 80
        c = grid[x][y]
        print(x, y, c, steps, dx, dy)
        #print(stack)
        #print(output)
        #raw_input()
        steps += 1
        if stringmode:
            if c != '"':
                stack.append(ord(c))
            else:
                stringmode = False
            continue

        if c in '0123456789': stack.append(int(c))
        elif c in '+/%*%-':
            b, a = stack.pop(), stack.pop()
            if c == '%' and a == 0:
                stack.append(0)
            else:
                stack.append(int(str(eval(str(a) + c +  str(b)))))
        elif c == '`': a = stack.pop(); b = stack.pop(); stack.append(1 if eval(str(b) + '>' + str(a)) else 0)
        elif c == '!': a = stack.pop(); stack.append(1 if eval('not ' + str(a)) else 0)
        elif c == '>': dx, dy = 0,  1
        elif c == '<': dx, dy = 0, -1
        elif c == '^': dx, dy = -1, 0
        elif c == 'v': dx, dy =  1, 0
        elif c == '_': a = stack.pop(); dx, dy = (0, 1) if a == 0 else (0, -1)
        elif c == '|': a = stack.pop(); dx, dy = (1, 0) if a == 0 else (-1, 0)
        elif c == '"': stringmode = True
        elif c == ':': a = stack[-1] if stack else 0; stack.append(a)
        elif c == '\\' and len(stack) >= 1:
            b = 0
            a = stack.pop()
            if len(stack) >= 1:
                b = stack.pop()
            stack.append(a)
            stack.append(b)
        elif c == '$': stack.pop()
        elif c == '.': output += str(stack.pop()) + " "
        elif c == ',': output += chr(stack.pop())
        elif c == '#': y += dy
        elif c == '@': break
        elif c == 'p':
            a = stack.pop()
            b = stack.pop()
            v = stack.pop()
            #print('grid', 'p', a, b, chr(v));
            grid[a][b] = chr(v)
        elif c == 'g':
            a = stack.pop()
            b = stack.pop()
            #print('grid', a, b, grid[a][b])
            stack.append(ord(grid[a][b]))
        elif c == '&':
            n = 20 #int(raw_input())
            stack.append(n)
        elif c == '?':
            pos = [(0,1), (0,-1), (1,0), (-1,0)]
            dx, dy = pos[random.randint(0,3)]


    
    return output

d1 = """>              v
v  ,,,,,"Hello"<
>48*,          v
v,,,,,,"World!"<
>25*,@"""
d2 = """ >25*"!dlrow ,olleH":v
                  v:,_@
                  >  ^ """
d3 = '>987v>.v\nv456<  :\n>321 ^ _@'
d = """>987v>.v
v456<  :
>321 ^ _@"""
d= """2>:3g" "-!v\ g30          <
 |!`"&":+1_:.:03p>03g+:"&"`|
 @               ^  p3\" ":<"""
d = """&>:1-:v v *_$.@ 
 ^    _$>\:^"""
quine = """0v 
"<@_ #! #: #,<*2-1*92,*25,+*92*4*55.0"""
seive = """2>:3g" "-!v\  g30          <
 |!`"O":+1_:.:03p>03g+:"O"`|
 @               ^  p3\" ":<"""
f = """08>:1-:v v *_$.@ 
  ^    _$>\:^"""
q = """01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@"""
q1 = """:0g,:"~"`#@_1+0"Q">_"""
q2 = """:0g,:93+`#@_1+"""
seive = """2>:3g" "-!v\  g30          <
 |!`"&":+1_:.:03p>03g+:"&"`|
 @               ^  p3\\" ":<
2 2345678901234567890123456789012345678"""
#print(d)
s = '2>:3g" "-!v\  g30          <\n |!`"&":+1_:.:03p>03g+:"&"`|\n @               ^  p3\" ":<\n2 2345678901234567890123456789012345678'
r = """v@.<
 >1^
>?<^
 >2^"""
print(seive.split('\n') == s.split('\n'))
print(interpret(r))
