import math
class Sudoku(object):
    #your code here
    def __init__(self, grid):
        self.grid = grid
        
    def is_valid(self):
        n  = len(self.grid)         
        sq = int(math.sqrt(n))

        if sq**2 != n:
            return False
           
        print(n, sq) 
        if not all([len(self.grid) == n]):
            return False

        try:
            if not all([len(self.grid[i]) == n for i in range(n)]):
                return False

            setn = set([i for i in range(1, n+1)])
            cols = zip(*self.grid)
            
            squares = []
            for i in range(n):
                p, q  = sq * (i / sq), sq * (i % sq)
                squares.append([self.grid[i][j] for i in range(p, p + sq) for j in range(q, q + sq)])
            if all([self.grid[i][j] >= 1 and self.grid[i][j] <= n for i in range(n) for j in range(n)] +
                   [set(self.grid[i]) == setn for i in range(n)] +
                   [set(cols[i]) == setn for i in  range(n)] +
                   [set(squares[i]) == setn for i in range(n)]):
                  return True
        except:
            return False
        return False

goodSudoku1 = Sudoku([
  [7,8,4, 1,5,9, 3,2,6],
  [5,3,9, 6,7,2, 8,4,1],
  [6,1,2, 4,3,8, 7,5,9],

  [9,2,8, 7,1,5, 4,6,3],
  [3,5,7, 8,4,6, 1,9,2],
  [4,6,1, 9,2,3, 5,8,7],
  
  [8,7,6, 3,9,4, 2,1,5],
  [2,4,3, 5,6,1, 9,7,8],
  [1,9,5, 2,8,7, 6,3,4]
])

print(goodSudoku1.is_valid())
g = Sudoku([True])
print(g.is_valid())
