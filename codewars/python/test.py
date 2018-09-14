#!/usr/bin/python
import re
from collections import Counter

def valid(field):
    C = Counter()
    n = len(field)
    m = len(field[0])
    field = [[0] * m] + field + [[0] * m]
    for i in range(n+2):
        field[i] = [0] + field[i] + [0]
    for i in range(1,n+1):
        for j in range(1, m+1):
            rc = field[i][j-1] + field[i][j+1]
            cc = field[i-1][j] + field[i+1][j]
            dc = field[i-1][j-1] + field[i+1][j+1] + field[i+1][j-1] + field[i-1][j+1]
            if field[i][j] == 1:
                if (rc >= 1 and cc >=1) or (rc >=1 and dc >=1) or (dc >= 1 and cc >=1): 
                    return False
                elif rc == 0 and cc == 0 and dc == 0: 
                    C['1'] += 1
            
    for r in field:
        for e in re.findall(r'11+', ''.join(map(str, r))):
            C[e] += 1
            
    for r in zip(*field):
        for e in re.findall(r'11+', ''.join(map(str, r))):
            C[e] += 1
    if C['1'] == 4 and C['11'] == 3 and C['111'] == 2 and C['1111'] == 1:
        return True;
    return False


battleField = [ [1, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0], 
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 0], 
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
                [0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

"""[[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""
print(valid(battleField))
