#!/usr/bin/python

import string
def get_digits(s, c):
    while c < len(s) and s[c] in string.digits:
        c += 1
    return c
#transform the formula, such that every atom has a count
def transform(s):
    s = "(" + s + ")1"
    i = 0
    news = ""
    while i < len(s):
        if s[i] in "})]":
            if s[i+1] in "123456789":
                j = get_digits(s, i+2)
                news += s[i] + s[i+1:j]#[::-1]
                i = j 
            else:
                news += s[i] + "1" 
                i += 1
        elif s[i] in string.uppercase:
            if s[i+1] in string.lowercase:
                if s[i+2] in "123456789":
                    j = get_digits(s, i+3)
                    news += s[i:i+2] + s[i+2:j]#[::-1]
                    i = j
                else:
                    news += s[i] + s[i+1] + "1"
                    i += 2
            elif s[i+1] in "123456789":
                j = get_digits(s, i+2)
                news += s[i] + s[i+1:j]#[::-1]
                i = j
            else:
                news += s[i] + "1"
                i += 1
        else:
            news += s[i]
            i += 1
    return news

#multiply
def process(s):
    stk = []
    stk.append("1")
    stk.append(")")
    i = 2
    news = ""
    while stk:
        c = stk[-2]
        if s[i] in string.digits:
            j = get_digits(s, i)
            d = str(int(c) * int(s[i:j][::-1]))
            if not s[j] in "})]":
                news += d[::-1]
            i = j
        elif s[i] in "}])":
            stk.append(d)
            stk.append(s[i])
            i += 1
        elif s[i] in "{[(":
            stk.pop()
            stk.pop()
            i += 1
        else:
            news += s[i]
            i += 1
    print(news)
    return news[::-1]
#sum all 
def calculate(s):
    atoms = {}
    i = 0
    while i < len(s):
        if s[i] in string.uppercase:
            if s[i+1] in string.lowercase:
                p = i+2
            else:
                p = i+1
            a = s[i:p]
            if not a in atoms:
                atoms[a] = 0
            j = get_digits(s, p)
            atoms[a] += int(s[p:j])
            i = j

    return(atoms)

inp = 'K4[ON[SO3]2]2' #'Mg(OH)2'
news = transform(inp) #"Mg3H2O2{(NPO2H4)3(SN2O)23}5")
print(news)
news1 = process(news[::-1])
print(news1)
print(calculate(news1))

