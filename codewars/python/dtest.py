#michaelrccurtis
class Skyscrapers(object):
    def __init__(self, clues, size):
        self.grid    = [[range(1, size+1) for _ in range(size)] for _ in range(size)]
        self.tops    = [c if c > 0 else None for c in clues[0:size]]
        self.rights  = [c if c > 0 else None for c in clues[size:2*size]]
        self.bottoms = [c if c > 0 else None for c in clues[2*size:3*size]][::-1]
        self.lefts   = [c if c > 0 else None for c in clues[3*size:4*size]][::-1]
        self.completed = [[False for _ in range(size)] for _ in range(size)]
        self.to_check  = []
        self.size      = size
        self.gen_perms()
        tick = 0
#        print(self.grid)
        for row in range(self.size):
            for col in range(self.size):
                self.to_check.append((row, col))
        while len(self.to_check) > 0:
            cell = self.to_check.pop(0)
            self.check_cell(cell[0], cell[1])

    def check(self, row, col):
        if (row, col) not in self.to_check:
            self.to_check.append((row, col))

    def gen_perms(self):
        top_perms      = [gen_perms(range(1, self.size+1), 0, c) for c in self.tops]
        bottom_perms   = [gen_perms(range(1, self.size+1), 0, c) for c in self.bottoms]
        self.col_perms = [[perm for perm in top_perms[i] if (perm[::-1] in bottom_perms[i])] for i in range(self.size)]
        left_perms     = [gen_perms(range(1, self.size+1), 0, c) for c in self.lefts]
        right_perms    = [gen_perms(range(1, self.size+1), 0, c) for c in self.rights]
        self.row_perms = [[perm for perm in left_perms[i] if (perm[::-1] in right_perms[i])] for i in range(self.size)]
        print('-------------row_perms-----------', len(self.row_perms))
        for e in self.row_perms:
            print(len(e))

    def check_cell(self, row, col):
        poss = []
        for num in self.grid[row][col]:
            if num not in [perm[col] for perm in self.row_perms[row]]:
                continue
            if num not in [perm[row] for perm in self.col_perms[col]]:
                continue
            if num in [vals[0] for vals in [self.grid[row][c] for c in range(self.size) if c != col] if len(vals) == 1]:
                continue
            if num in [vals[0] for vals in [self.grid[r][col] for r in range(self.size) if r!= row]  if len(vals) == 1]:
                continue
            poss.append(num)
        if len(poss) < len(self.grid[row][col]):
            print 'updated', row+1, col+1, poss
            self.grid[row][col] = poss
            self.row_perms[row] = [perm for perm in self.row_perms[row] if all([perm[_col] in self.grid[row][_col] for _col in range(self.size)])]
            self.col_perms[col] = [perm for perm in self.col_perms[col] if all([perm[_row] in self.grid[_row][col] for _row in range(self.size)])]
#            print(self.row_perms[row])
            for x in range(self.size):
                if x != row:
                    self.check(x, col)
                if x != col:
                    self.check(row, x)


    def check_row(self, row):
        for col in range(self.size):
            if self.completed[row][col]:
                continue
            self.grid[row][col] = list(set([perm[col] for perm in self.row_perms[row]]))
            if len(self.grid[row][col]) == 1:
                self.completed[row][col] = True
        self.row_perms[row] = [perm for perm in self.row_perms[row] if all([perm[col] in self.grid[row][col] for col in range(self.size)])]

    def check_col(self, col):
        for row in range(self.size):
            if self.completed[row][col]:
                continue
            self.grid[row][col] = list(set([perm[row] for perm in self.col_perms[col]]))
            if len(self.grid[row][col]) == 1:
                self.completed[row][col] = True
        self.col_perms[col] = [perm for perm in self.col_perms[col] if all([perm[row] in self.grid[row][col] for row in range(self.size)])] 

def gen_perms(nums, high, constraint):
    if (constraint == 0 or constraint is None) and len(nums) == 0:
        return [[]]
    if constraint > len(nums):
        return None
    perms = []
    for num in nums:
        new_high = high if num < high else num
        if constraint is not None:
            ncon = constraint if num < high else constraint-1
        else:
            ncon = None
        nnums = list(nums)
        nnums.remove(num)
        num_perms = gen_perms(nnums, new_high, ncon)
        if num_perms is not None:
            perms += [[num] + p for p in num_perms]
    return perms

def solve_puzzle(clues):
    sky = Skyscrapers(clues, 7)
    return tuple([tuple([x[0] for x in row]) for row in sky.grid])


import time
for c in ([7,0,0,0,2,2,3,0,0,3,0,0,0,0,3,0,3,0,0,5,0,0,0,0,0,5,0,4],
          [6,4,0,2,0,0,3,0,3,3,3,0,0,4,0,5,0,5,0,2,0,0,0,0,4,0,0,3]):
#          [ 3, 2, 2, 3, 2, 1, 1, 2, 3, 3, 2, 2, 5, 1, 2, 2, 4, 3, 3, 2, 1, 2, 2, 4 ],
#          [ 0, 3, 0, 5, 3, 4, 0, 0, 0, 0, 0, 1, 0, 3, 0, 3, 2, 3, 3, 2, 0, 3, 1, 0 ],
#          [ 0, 0, 0, 2, 2, 0, 0, 0, 0, 6, 3, 0, 0, 4, 0, 0, 0, 0, 4, 4, 0, 3, 0, 0 ]):

#    c = [0, 0, 1, 3, 2, 0, 3, 0, 0, 0, 0, 3, 0, 2, 1, 3] 
    #c = [2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 2, 3, 3, 2, 1, 3]
    #c = [ 3, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0]
    t1 = time.time()
    print(solve_puzzle(c))
    t2 = time.time()
    print(t2 - t1)

