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
        self.solve(0, self.row_perm, self.col_perm)
 

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
    def prune(self, nrow_perm, ncol_perm, _row, _col, v): 
        nrow_perm[_row] = self.trim_permutation(nrow_perm[_row], self.board[_row])
        ncol_perm[_col] = self.trim_permutation(ncol_perm[_col], [self.board[r][_col] for r in range(self.size)])
#        skyscrapper.print_l('after trimming row_perm', nrow_perm)
#        skyscrapper.print_l('after trimming col_perm', ncol_perm)
        nrow_perm = self.remove_permutations(nrow_perm, _col, _row, v)
        ncol_perm = self.remove_permutations(ncol_perm, _row, _col, v)
#        skyscrapper.print_l('after removing row_perm', nrow_perm)
#        skyscrapper.print_l('after removing col_perm', ncol_perm)
        for e in nrow_perm:
            if not e:
                return False
        for e in ncol_perm:
            if not e:
                return False
        return True


    def solve(self, found, row_perm, col_perm):
        if found == self.size**2: return True
        rmap = [self.get_map(row_perm[_r], self.size) for _r in range(self.size)]
        cmap = [self.get_map(col_perm[_c], self.size) for _c in range(self.size)]
       # skyscrapper.print_l('rmap', rmap)
       # skyscrapper.print_l('cmap', cmap)
       # raw_input()
        #print(self.board)
        allres = [(len(rmap[_row][_col] & cmap[_col][_row]), _row, _col) for _row in range(self.size) for _col in range(self.size) if self.board[_row][_col] == 0]
        #print(allres, min(allres))
        l, _row, _col = min(allres)
        res = rmap[_row][_col] & cmap[_col][_row]
        #print('res', _row+1, _col+1, res)
        for v in list(res): 
            nrow_perm = copy.deepcopy(row_perm)
            ncol_perm = copy.deepcopy(col_perm)
            if not self.prune(nrow_perm, ncol_perm, _row, _col, v):
          #      print ('failed to use', v)
                continue
            #print('setting value ', v)
            self.board[_row][_col] = v
            if self.solve(found+1, nrow_perm, ncol_perm):
                return True
            #print('failed to use 2', v)
            self.board[_row][_col] = 0
            #raw_input()
            #print(self.row_perm)
            #print(self.col_perm)
        return False
     
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
s = skyscrapper([ 3, 2, 2, 3, 2, 1, 1, 2, 3, 3, 2, 2, 5, 1, 2, 2, 4, 3, 3, 2, 1, 2, 2, 4 ])
#s = skyscrapper([ 3, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0])
#s = skyscrapper([ 2,2,0,2, 0,0,1,0, 0,0,0,0,1,0,0,0])
s.print_l('board', s.board)
#print(s.matching_permutation((4,1), [0,0,0,0,5,6]))
#perm_all[(4,1)] = get_perm((4,1), [0,0,0,0, 5, 0])
#print(perm_all[(4,1)])

import time
for c in ([ 3, 2, 2, 3, 2, 1, 1, 2, 3, 3, 2, 2, 5, 1, 2, 2, 4, 3, 3, 2, 1, 2, 2, 4 ],
          [ 0, 3, 0, 5, 3, 4, 0, 0, 0, 0, 0, 1, 0, 3, 0, 3, 2, 3, 3, 2, 0, 3, 1, 0 ],
          [ 0, 0, 0, 2, 2, 0, 0, 0, 0, 6, 3, 0, 0, 4, 0, 0, 0, 0, 4, 4, 0, 3, 0, 0 ]):
    t1 = time.time()
    s = skyscrapper(c)
    print(s.print_l('', s.board))
    t2 = time.time()
    print(t2 - t1)
