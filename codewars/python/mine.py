#!/usr/bin/python
def dfs(map, visited, s, e, d):
    r, c = s
    visited[r][c] = d 
    if s == e:
        return True

    dir = [[0, -1, 'left'], [0, 1, 'right'], [-1, 0, 'up'], [1, 0, 'down']]
    for r, c, d in dir:
        sr, sc = s[0] + r, s[1] + c
        if map[sr][sc] and not visited[sr][sc]:
            if dfs(map, visited, [sr, sc], e, d):
                return True

    return False


def print_path(x, y, path, direction, pret):
    if path[x][y] == 'done':
        return
    dx, dy = direction[path[x][y]]
    print_path(x + dx, y + dy, path, direction, pret)
    pret += [path[x][y]]

def solve(map, miner, exit):
    rows = len(map[0]) + 2
    cols = len(map) + 2
    newmap = [[False for i in range(cols)] for j in range(rows)]
    for i in range(len(map)):
        for j in range(len(map[0])):
            newmap[j+1][i+1] = map[i][j]

    visited = [[False for i in range(cols)] for j in range(rows)]
    for i in range(cols):
        visited[0][i] = True
        visited[rows-1][i] = True
    for i in range(rows):
        visited[i][0] = True
        visited[i][cols-1] = True
    direction = {'right': [0, -1], 'left': [0, 1], 'up': [1, 0], 'down': [-1, 0]}
    pret = []
    sx, sy = miner['y'] + 1, miner['x'] + 1
    ex, ey = exit['y'] + 1, exit['x'] + 1
    if dfs(newmap, visited, [sx, sy], [ex, ey], 'done'):
        print_path(ex, ey, visited, direction, pret)
    return pret

#map= [[True, False, True, True], [True, False, True, False], [True, False, True, True], [True, True, True, True]]
map = [[True, False],
       [True, True]]
print(solve(map, {'x': 0, 'y': 0}, {'x': 0, 'y': 1}))
