#!/usr/bin/python

import itertools
nums = list(itertools.product(map(str, range(1, 14)), repeat = 4))
opers = list(itertools.product('+-/*', repeat = 3))
for n,o in itertools.product(nums, opers):
    e1 = '(' + n[0] + o[0] + n[1] + ')' + o[1] + '(' + n[2] + o[2] + n[3] + ')'
    e2 = '(' + '(' + n[0] + o[0] + n[1] + ')' + o[1] + n[2] + ')' + o[2] + '(' + n[3] + ')'
    e3 = '(' + '(' + n[0] + ')' + o[0] + '(' + n[1] +  o[1] + n[2] + ')' + ')' + o[2] + '(' + n[3] + ')'
    e4 = '(' + n[0] + ')' + o[0] + '(' + n[1] +  o[1] + '(' + n[2] + o[2] + n[3] + ')' + ')' 
    e5 = '(' + n[0] + ')' + o[0] + '(' + '('  + n[1] +  o[1] + n[2] + ')' + o[2] + n[3] + ')'  
    try:
        if eval(e1) == 30:
            print(e1)
    except:
        pass
    #print(e1, e2, e3, e4, e5)
    #raw_input()
