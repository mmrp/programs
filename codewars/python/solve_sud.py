#!/usr/bin/python
import copy
import math
def solve(board, board_c, board_b, rows, cols, boxes, R, S):
    if max((len(r) for r in rows)) == 0:
        return True

    rl, cr = min((len(r), i) for i, r in enumerate(rows)  if len(r) > 0)
    cl, cc = min((len(c), i) for i, c in enumerate(cols)  if len(c) > 0)
    bl, cb = min((len(b), i) for i, b in enumerate(boxes) if len(b) > 0)

    if rl <= cl and rl <= bl:
        cc = board[cr].index(0)
        cb = S * (cr / S) + cc / S #S * (cr / S) + cc / S    #box number
        bp  = S * (cr % S) + cc % S
    elif cl <= rl and cl <= bl:
        cr = board_c[cc].index(0)
        cb = S * (cr / S) + cc / S #S * (cr / S) + cc / S    #box number
        bp = S * (cr % S) + cc % S
    else:
        bp = board_b[cb].index(0)
        cr = S * (cb / S) + bp / S
        cc = S * (cb % S) + bp % S

    for e in (rows[cr] & cols[cc] & boxes[cb]):
        board[cr][cc] = e
        board_c[cc][cr] = e
        board_b[cb][bp] = e
        nb = copy.deepcopy(boxes)
        nr = copy.deepcopy(rows)
        nc = copy.deepcopy(cols)
        nb[cb].remove(e)
        nr[cr].remove(e)
        nc[cc].remove(e)
        if solve(board, board_c, board_b, nr, nc, nb, R, S):
            return True
        board[cr][cc]   = 0
        board_c[cc][cr] = 0
        board_b[cb][bp]  = 0
    return False



from sudoku import validSolution
def sudoku(board):
    print_board(board)
    r = len(board)
    c = len(board[0])
    s = int(math.sqrt(r))
    n = set([i for i in range(r + 1)])
    z = set([0])
    board_c = [[board[i][j] for i in range(c)] for j in range(r)]
    board_b = [[board[a+i][b+j] for i in range(s) for j in range(s)] for a in range(0, r, s) for b in range(0, r, s)]
    rows  = [n - set(e) - z for e in board]
    cols  = [n - set(e) - z for e in board_c]
    boxes = [n - set(e) - z for e in board_b]
    #print rows
    #print cols
    #print boxes
    import time
    t1 = time.time()
    r = solve(board, board_c, board_b, rows, cols, boxes, r, s)
    if validSolution(board):
        print "Valid"
        print_board(board)
    else:
        print "Invalid solution"
    t2 = time.time()
    print(t2-t1)

def print_board1(board):
    for r in board:
        for c in r:
            print c,
        print


def print_board(board):
    r = len(board)
    s = int(math.sqrt(r))
    vlist = [i for i in range(0, r+1, s)]
    line = ' ' + '+'.join(['-' * (2*s) for i in range(s)])
    for i in range(r):
        if i in vlist:
            print line
        print ''.join(('|' if j in vlist else '') + str(board[i][j]) + ' ' for j in range(r)) + '|'

    print line

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

puzzle1=[[8,5,0,0,0,2,4,0,0],
         [7,2,0,0,0,0,0,0,9],
         [0,0,4,0,0,0,0,0,0],
         [0,0,0,1,0,7,0,0,2],
         [3,0,5,0,0,0,9,0,0],
         [0,4,0,0,0,0,0,0,0],
         [0,0,0,0,8,0,0,7,0],
         [0,1,7,0,0,0,0,0,0],
         [0,0,0,0,3,6,0,4,0]]

puzzle2=[[9, 0, 0, 0, 8, 0, 0, 0, 1],
 [0, 0, 0, 4, 0, 6, 0, 0, 0],
 [0, 0, 5, 0, 7, 0, 3, 0, 0],
 [0, 6, 0, 0, 0, 0, 0, 4, 0],
 [4, 0, 1, 0, 6, 0, 5, 0, 8],
 [0, 9, 0, 0, 0, 0, 0, 2, 0],
 [0, 0, 7, 0, 3, 0, 2, 0, 0],
 [0, 0, 0, 7, 0, 5, 0, 0, 0],
 [1, 0, 0, 0, 4, 0, 0, 0, 7]]
#[[9, 2, 6, 5, 8, 3, 4, 7, 1], [7, 1, 3, 4, 2, 6, 9, 8, 5], [8, 4, 5, 9, 7, 1, 3, 6, 2], [3, 6, 2, 8, 5, 7, 1, 4, 9], [4, 7, 1, 2, 6, 9, 5, 3, 8], [5, 9, 8, 3, 1, 4, 7, 2, 6], [6, 5, 7, 1, 3, 8, 2, 9, 4], [2, 8, 4, 7, 9, 5, 6, 1, 3], [1, 3, 9, 6, 4, 2, 8, 5, 7]]
sudoku(puzzle)
sudoku(puzzle1)
sudoku(puzzle2)
#sudoku(puzzle2)
