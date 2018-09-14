#!/usr/bin/python

import itertools
gbl_expr = {}
def get_possible_numbers(total):
    expr = {}
    subset = set([])
    nums = map(str, range(1, 101))
    for n1,n2 in itertools.product(nums, nums):
        for oper in "+-*/":
            res = n1 + oper + n2
            if eval(res) == total:
                expr[res] = True
            subset.add(n1)
    return (expr, list(subset))

gbl_expr[24] = get_possible_numbers(24)
#poss_nums = gbl_expr[24][1]
#for n in poss_nums:
#    gbl_expr[n] = get_possible_numbers(n)
#    print('done', n)

print(gbl_expr)#, poss_nums)
