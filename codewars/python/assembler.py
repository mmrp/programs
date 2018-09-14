#!/usr/bin/env python
"""
We want to create a simple interpreter of assembler which will support the following instructions:

mov x y - copies y (either a constant value or the content of a register) into register x
inc x - increases the content of register x by one
dec x - decreases the content of register x by one
jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward), but only if x (a constant or a register) is not zero
Register names are alphabetical (letters only). Constants are always integers (positive or negative).

Note: the jnz instruction moves relative to itself. For example, an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.

The function will take an input list with the sequence of the program instructions and will return a dictionary with the contents of the registers.

Also, every inc/dec/jnz on a register will always be followed by a mov on the register first, so you don't need to worry about uninitialized registers.

mov x, y - copy y (either an integer or the value of a register) into register x.
inc x - increase the content of register x by one.
dec x - decrease the content of register x by one.
add x, y - add the content of the register x with y (either an integer or the value of a register) and stores the result in x (i.e. register[x] += y).
sub x, y - subtract y (either an integer or the value of a register) from the register x and stores the result in x (i.e. register[x] -= y).
mul x, y - same mith multiply (i.e. register[x] *= y).
div x, y - same with integer division (i.e. register[x] /= y).
label: - define a label position (label = identifier + ":", an identifier being a string that does not match any other command). Jump commands and call are aimed to these labels positions in the program.
jmp lbl - jumps to to the label lbl.
cmp x, y - compares x (either an integer or the value of a register) and y (either an integer or the value of a register). The result is used in the conditional jumps (jne, je, jge, jg, jle and jl)
jne lbl - jump to the label lbl if the values of the previous cmp command were not equal.
je lbl - jump to the label lbl if the values of the previous cmp command were equal.
jge lbl - jump to the label lbl if x was greater or equal than y in the previous cmp command.
jg lbl - jump to the label lbl if x was greater than y in the previous cmp command.
jle lbl - jump to the label lbl if x was less or equal than y in the previous cmp command.
jl lbl - jump to the label lbl if x was less than y in the previous cmp command.
call lbl - call to the subroutine identified by lbl. When a ret is found in a subroutine, the instruction pointer should return to the instruction next to this call command.
ret - when a ret is found in a subroutine, the instruction pointer should return to the instruction that called the current function.
msg 'Register: ', x - this instruction stores the output of the program. It may contain text strings (delimited by single quotes) and registers. The number of arguments isn't limited and will vary, depending on the program.
end - this instruction indicates that the program ends correctly, so the stored output is returned (if the program terminates without this instruction it should return the default output: see below).
; comment - comments should not be taken in consideration during the execution of the program.
"""
from collections import defaultdict
import re
import string
class Interpreter():
    def __init__(self):
        self.regs = defaultdict(int)
        self.valid_cmds = set(('mov', 'dec', 'inc', 'sub', 'add', 'mul', 'dec', 'je', \
                               'jne', 'jmp', 'jl', 'jle', 'jg', 'jge', 'call', 'msg', \
                                'ret', 'end', 'cmp', 'div'))
        self.labels = {}
        print(self.regs)
        self.ip   = 0
        self.cmpvalue = None
        self.retaddr = []
        self.output = ''
        self.instructions = []


    @staticmethod
    def isreg(x):
        return x in string.ascii_letters

    def fetch_value(self, v):
        print('fetch', v)
        if Interpreter.isreg(v):
            v = self.regs[v]
        else:
            v = int(v)
        return v

    def mov(self, x, y):
        self.regs[x] = self.fetch_value(y)
        return True

    def inc(self, x):
        self.regs[x] += 1
        return True

    def dec(self, x):
        self.regs[x] -= 1
        return True

    def add(self, x, y):
        self.regs[x] += self.fetch_value(y)
        return True

    def mul(self, x, y):
        self.regs[x] *= self.fetch_value(y)
        return True

    def div(self, x, y):
        self.regs[x] //= self.fetch_value(y)
        return True

    def sub(self, x, y):
        self.regs[x] -= self.fetch_value(y)
        return True

    def jmp(self, label):
        self.ip = self.labels[label]
        return False

    def jnz(self, x, y):
        if self.regs[x] != 0:
            self.ip += int(y)
            return False
        return True

    def cmp(self, x, y):
        x = self.fetch_value(x)
        y = self.fetch_value(y)
        self.cmpvalue = x - y
        return True

    def jne(self, lbl):
        if self.cmpvalue != 0:
            self.ip = self.labels[lbl]
            return False
        return True

    def je(self, lbl):
        if self.cmpvalue == 0:
            self.ip = self.labels[lbl]
            return False
        return True

    def jg(self, lbl):
        if self.cmpvalue > 0:
            self.ip = self.labels[lbl]
            return False
        return True

    def jge(self, lbl):
        if self.cmpvalue >= 0:
            self.ip = self.labels[lbl]
            return False
        return True

    def jl(self, lbl):
        if self.cmpvalue < 0:
            self.ip = self.labels[lbl]
            return False
        return True

    def jle(self, lbl):
        if self.cmpvalue <= 0:
            self.ip = self.labels[lbl]
            return False
        return True

    def call(self, lbl):
        print('in call', self.labels[lbl])
        self.retaddr.append(self.ip+1)
        self.ip = self.labels[lbl]
        return False

    def msg(self, inp):
        out = ''
        print(re.findall(r'\'[^\']*\'|[a-zA-Z]', inp))
        for e in re.findall(r'\'[^\']*\'|[a-zA-Z]', inp):
            if e[0] == '\'' and e[-1] =='\'':
                out += str(e[1:-1])
            else:
                out += str(self.fetch_value(e.strip()))
        self.output = out + self.output
        print('msg', self.output)
        return True

    def ret(self):
        self.ip = self.retaddr.pop()
        return False

    def process(self, instructions):
        ip = 0
        for intr in instructions.splitlines():
            res = re.split(r'[;]+', intr)
            if res[0] is '': continue
            cmd = re.split(r'[ ,]+', res[0].strip())
            if cmd[0] not in self.valid_cmds: #should be a label
                self.labels[cmd[0].split(':')[0]] = ip
            else:
                if cmd[0] == 'msg':
                    self.instructions.append(['msg', re.sub(r'^msg', '', res[0].strip()).strip()])
                else:
                    self.instructions.append(cmd)
                ip += 1
        print(self.labels)
        print(self.instructions)
        self.ip = 0
        while self.ip < len(self.instructions):
            cmd = self.instructions[self.ip]  #remove the comments
            intr = cmd[0]
            args = cmd[1:]
            print("current", intr, args, self.ip)
            input()
            if intr == 'end':
                break
            inc_ip = getattr(self, intr)(*args)
            if inc_ip: self.ip += 1
            #print(intr, args, self.ip, self.regs)
#           raw_input()
        print(self.regs)
        return -1 if intr != 'end' else self.output


if '__main__' == __name__:
    program = '''
; My first program
mov  a, 5
inc  a
call function
msg  '(5+1)/2 = ', a    ; output message
end

function:
    div  a, 2
    ret
'''
    program_fibonacci = '''
mov   a, 8            ; value
mov   b, 0            ; next
mov   c, 0            ; counter
mov   d, 0            ; first
mov   e, 1            ; second
call  proc_fib
call  print
end

proc_fib:
    cmp   c, 2
    jl    func_0
    mov   b, d
    add   b, e
    mov   d, e
    mov   e, b
    inc   c
    cmp   c, a
    jle   proc_fib
    ret

func_0:
    mov   b, c
    inc   c
    jmp   proc_fib

print:
    msg   'Term ', a, ' of Fibonacci series is: ', b        ; output text
    ret
'''
    program_fail = '''
call  func1
call  print
end

func1:
    call  func2
    ret

func2:
    ret

print:
    msg 'This program should return -1'
'''
    program_factorial = '''
mov   a, 10
mov   b, a
mov   c, a
call  proc_fact
call  print
end

proc_fact:
    dec   b
    mul   c, b
    cmp   b, 1
    jne   proc_fact
    ret

print:
    msg   a, '! = ', c ; output text
    ret
'''

    program_mod = '''
mov   a, 11           ; value1
mov   b, 3            ; value2
call  mod_func
msg   'mod(', a, ', ', b, ') = ', d        ; output
end

; Mod function
mod_func:
    mov   c, a        ; temp1
    div   c, b
    mul   c, b
    mov   d, a        ; temp2
    sub   d, c
    ret
'''
    inp = Interpreter()
    print(inp.process(program))
