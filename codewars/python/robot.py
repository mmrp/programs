#!/usr/bin/python

from collections import deque
import math

    
    
def path(s):
    n = len(s)
    w = int(math.sqrt(n))
    g = [[s[i*w+j] for j in range(w)] for i in range(w)]
    start = s.index('S')
    end   = s.index('T')
    ex, ey = (end/w, end %w)
    visited = deque()
    visited.append((start/w, start % w))
    dist = {(start/w, start % w): 0}
    while visited:
        x, y = visited.popleft()
        if x == ex and y == ey:
            return dist[(x, y)]
        n = dist[(x, y)]
        if x+1 < w and g[x+1][y] != '#' and (x+1,y) not in visited:
            visited.append((x+1, y))
            dist[(x+1, y)] = n + 1
        if y-1 >= 0 and g[x][y-1] != '#' and (x,y-1) not in visited:
            visited.append((x, y-1))
            dist[(x, y-1)] = n + 1
        if y+1 < w and g[x][y+1] != '#' and (x,y+1) not in visited:
            visited.append((x, y+1))
            dist[(x, y+1)] = n + 1
    return -1
            
    print(g)

print(path("S.......T"))
print(path("S#.##...T"))
