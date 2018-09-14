def has_exit(maze):
    c = 0
    for p, v in enumerate(maze):
        if 'k' in v:
            c += 1
            kpos = (p, v.index('k'))
    if c != 1:
        raise Exception()
    if (len(maze) == 1 and len(maze[0]) == 1):
        return True
    
    x, y = kpos
    dir = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    visited = set()
    L = len(maze)
    W = len(maze[0])
    visited.add((x,y))
    
    def dfs(maze, x, y):
        print(x, y)
        if x == 0 or y == 0 or x == L-1 or y == W-1:
            if maze[x][y] == ' ': 
                return True
                
        for dx, dy in dir:
            fx, fy = (x + dx, y + dy)
            if fx < 0 or fy < 0 or fx >= L or fy >= W or \
                      (fx, fy) in visited or \
                      maze[fx][fy] == '#':
                continue
            visited.add((fx, fy))
            if dfs(maze, fx, fy):
                return True
        return False
