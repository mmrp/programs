#!/usr/bin/python

import sys
import itertools
class skyscapper(object):
    def __init__(self, clues, size):
        self.board = [[0] * size for _ in range(size)]
        self.perm_all   = {}
        self.row_perm = {}
        self.col_perm = {}
        self.generate_all_permutations(size)
        self.row_clues = [(clues[4*size-1-i], clues[size+i]) for i in range(size)] #top and bottom
        self.col_clues = [(clues[0+i], clues[3*size-1-i]) for i in range(size)] #left and right
        self.solve()

    def solve(self):
        for rc in self.row_clues: self.row_perm[rc] = copy.deepcopy(self.perm_all[rc])
        for cc in self.col_clues: self.col_perm[cc] = copy.deepcopy(self.perm_all[cc])

    def get_map(self, perm, n, a1, a2):
        s = [set([]) for _ in range(n)]
        if not(a1) and not(a2):
            return [set(range(1,n+1)) for _ in range(n)]

        for e in perm:
            f, b = e
            if (not(a1) and b == a2) or (f == a1 and not(a2)) or (f == a1 and b == a2):
                for g in perm[e]:
                    for p, v in enumerate(g):
                        s[p].add(v)
       
        return s if all(s) else []

    def get_mapping(self):
        for rc in self.row_clues:
            rmap = self.get_map(self.row_perm, self.size, *rc)
        for cc in self.col_clues:
            cmap = self.get_map(self.col_perm, self.size, *cc)
        for i in range(size):
            for j in range(size):
                res = rmap(slef.row_clues[i]) & cmap(slef.col_clues[j])
                if len(res) == 1:
                    self.board[i][j] = res[0]
                


    def generate_all_permutations(self, size):
        def greater(s):
            g = s[0]
            count = 1
            for e in s:
                if e > g:
                    count += 1
                    g = e
            return count

        self.perm_all[(0,0)] = []
        for e in list(itertools.permutations(range(1, size+1))):
            f, b = greater(e), greater(e[::-1])
            if (f,b) not in self.perm_all:
                self.perm_all[(f,b)] = []
            self.perm_all[(f,b)].append(e)
            self.perm_all[(0,0)].append(e)

        for i in range(1, size+1):
            res = []
            for j in range(1, size+1):
                if (i, j) in self.perm_all:
                    for e in self.perm_all[(i, j)]:
                        res.append(e)
            if res:
                self.perm_all[(i,0)] = res
    
        for i in range(1, size+1):
            res = []
            for j in range(1, size+1):
                if (j, i) in self.perm_all:
                    for e in self.perm_all[(j, i)]:
                        res.append(e)
            if res:
                self.perm_all[(0,i)] = res
    

    def matching_permutation(self, pos, arr):
        res = []
        for v in self.perm[pos]:
            for p in zip(arr, v):
                if p[0] and p[0] != p[1]:
                    break
            else:
                res.append(v)
        return res
            
            
s = skyscapper([], 6)
print(s.matching_permutation((4,1), [0,0,0,0,5,6]))
#perm_all[(4,1)] = get_perm((4,1), [0,0,0,0, 5, 0])
#print(perm_all[(4,1)])
