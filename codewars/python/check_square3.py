#!/usr/bin/python

import sys
import itertools
import copy
class skyscrapper(object):
    def __init__(self, clues):
        print(len(clues))
        self.size = len(clues)/4
        size = self.size
        self.board = [[0] * size for _ in range(size)]
        self.perm_all   = {}
        self.row_clues = [(clues[4*size-1-i], clues[size+i]) for i in range(size)] #top and bottom
        self.col_clues = [(clues[0+i], clues[3*size-1-i]) for i in range(size)] #left and right
        skyscrapper.generate_all_permutations(self.perm_all, size)
        self.row_perm = [copy.deepcopy(self.perm_all[rc]) for rc in self.row_clues]
        self.col_perm = [copy.deepcopy(self.perm_all[cc]) for cc in self.col_clues]
        self.solve()
 

    @staticmethod
    def generate_all_permutations(perm_all, size):
        def greater(s):
            g, cc = s[0], 1
            for e in s:
                if e > g:
                    cc += 1
                    g = e
            return cc

        perm_all[(0,0)] = []
        for e in list(itertools.permutations(range(1, size+1))):
            f, b = greater(e), greater(e[::-1])
            if (f,b) not in perm_all:
                perm_all[(f,b)] = []
            perm_all[(f,b)].append(e)
            perm_all[(0,0)].append(e)

        for i in range(1, size+1):
            res = []
            for j in range(1, size+1):
                if (i, j) in perm_all:
                    for e in perm_all[(i, j)]:
                        res.append(e)
            if res:
                perm_all[(i,0)] = res
    
        for i in range(1, size+1):
            res = []
            for j in range(1, size+1):
                if (j, i) in perm_all:
                    for e in perm_all[(j, i)]:
                        res.append(e)
            if res:
                perm_all[(0,i)] = res

    @staticmethod
    def print_d(s, arr):
        print(s)
        for e in sorted(arr.keys()):
            print(e, arr[e])
    @staticmethod
    def print_l(s, arr):
        print(s)
        for i, e in enumerate(arr):
            print(e)
            
    def solve(self):
        total_count = self.size**2 
        found = 0
        skyscrapper.print_l('row_perm', self.row_perm)
        skyscrapper.print_l('col_perm', self.col_perm)
        while found < total_count:
            rmap = [self.get_map(self.row_perm[_r], self.size) for _r in range(self.size)]
            cmap = [self.get_map(self.col_perm[_c], self.size) for _c in range(self.size)]
            skyscrapper.print_l('rmap', rmap)
            skyscrapper.print_l('cmap', cmap)
            raw_input()
#            return
            for _row in range(self.size):
                for _col in range(self.size):
                    if self.board[_row][_col]: 
                        continue
                    
                    res = rmap[_row][_col] & cmap[_col][_row]
                    print('res', _row+1, _col+1, res)
                    if len(res) == 1:
                        print('found', _row+1, _col+1, res)
                        self.board[_row][_col] = list(res)[0]
                        self.row_perm[_row] = self.trim_permutation(self.row_perm[_row], self.board[_row])
                        self.col_perm[_col] = self.trim_permutation(self.col_perm[_col], [self.board[r][_col] for r in range(self.size)])
                        skyscrapper.print_l('after trimming row_perm', self.row_perm)
                        skyscrapper.print_l('after trimming col_perm', self.col_perm)
                        self.row_perm = self.remove_permutations(self.row_perm, _col, _row, list(res)[0])
                        self.col_perm = self.remove_permutations(self.col_perm, _row, _col, list(res)[0])

                        skyscrapper.print_l('after removing row_perm', self.row_perm)
                        skyscrapper.print_l('after removing col_perm', self.col_perm)
                        raw_input()
                        #print(self.row_perm)
                        #print(self.col_perm)
                        found += 1
         
    def get_map(self, perm, n):
        s = [set([]) for _ in range(n)]
        for g in perm:
            for p, v in enumerate(g):
                s[p].add(v)
        return s 

               
    def remove_permutations(self, perm, check_idx, ignore_entry, v): 
        for entry in range(self.size):
            if entry == ignore_entry: continue
            res = []
            for p, g in enumerate(perm[entry]):
                if g[check_idx] == v: continue
                res.append(g)

            if res: perm[entry] = res
        return perm
                

    #return the part of permutation which has matching entries 
    def trim_permutation(self, perm, entry):
        res = []
        for v in perm:
            for p in zip(entry, v):
                if p[0] and p[0] != p[1]:
                    break
            else:
                res.append(v)
        return res
            
            
#s = skyscrapper([2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 2, 3, 3, 2, 1, 3])
#s = skyscrapper([ 3, 2, 2, 3, 2, 1, 1, 2, 3, 3, 2, 2, 5, 1, 2, 2, 4, 3, 3, 2, 1, 2, 2, 4 ])
s = skyscrapper([ 3, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0])
#s = skyscrapper([ 2,2,0,2, 0,0,1,0, 0,0,0,0,1,0,0,0])
s.print_l('board', s.board)
#print(s.matching_permutation((4,1), [0,0,0,0,5,6]))
#perm_all[(4,1)] = get_perm((4,1), [0,0,0,0, 5, 0])
#print(perm_all[(4,1)])
