import math
class Sudoku(object):
    #your code here
    def __init__(self, grid):
        self.grid = grid
        
    def valid_len(arr, n):
        return all([len(arr[i]) == n for i in len(arr)] + [len(arr) == n])
            
    def is_valid(self):
        n  = len(self.grid)       
        sq = int(math.sqrt(n))

        if sq**2 != n:
            return False
                
        print(n, sq) 
        print(self.grid)
        try:
            if not all([len(self.grid) == n]):
                return False
    
            if not all([len(self.grid[i]) == n for i in range(n)]):
                return False
    
            setn = set([i for i in range(1, n+1)])
            cols = zip(*self.grid)
                
            squares = []
            for i in range(n):
                p, q  = sq * (i / sq), sq * (i % sq) 
                squares.append([self.grid[i][j] for i in range(p, p + sq) for j in range(q, q + sq)])
            print('check', [isinstance(self.grid[i][j], int) for i in range(n) for j in range(n)])
            if all([not isinstance(self.grid[i][j], bool) for i in range(n) for j in range(n)] + 
                   [set(self.grid[i]) == setn for i in range(n)] +
                   [set(cols[i]) == setn for i in  range(n)] +
                   [set(squares[i]) == setn for i in range(n)]):
                  return True
        except:
            return False
        return False

a = [[True]]
s = Sudoku(a)
print(s.is_valid())
