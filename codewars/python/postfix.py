#!/usr/bin/python3



def postfix(str):
    oper = {'.': ['left', 0], '(':['left', 1], 
            '+': ['left', 2], '-': ['left', 2], 
            '*': ['left',3], '/':['left', 3], 
            '^':['right', 4]
           }

    output = []
    stack =  ['.']
    for s in str:
        if s == '(':
            stack.append(s)
        elif s == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif s in oper:
            assoc, prec = oper[s]
            if prec == oper[stack[-1]][1]:
                if assoc == 'left':
                    output.append(stack.pop())
                stack.append(s)
            elif prec > oper[stack[-1]][1]:
                stack.append(s)
            else:
                while prec < oper[stack[-1]][1]:
                    output.append(stack.pop())
                
                if prec == oper[stack[-1]][1]:
                    if assoc == 'left':
                        output.append(stack.pop())
                    stack.append(s)
                elif prec > oper[stack[-1]][1]:
                    stack.append(s)     
        else:
            output.append(s)

    while stack[-1] != '.':
        output.append(stack.pop())

    return ''.join(output)

print(postfix(raw_input()))
