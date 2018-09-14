def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]def construct_graph(grid):
    w = len(grid)
    l = len(grid[0])
    graph = [[] for i in range(l * w)]
    off = -w
    for i in range(l):
        off += w
        for j in range(w):
            if not grid[j][i].passable:
                continue
            c = off + j
            for dw, dl, p in [(1, 0, w), (0, 1, 1)]: #check only for down and right
                if j == (w-1) and p == 1: # skip right assignment for last column
                    continue

                if i == (l-1) and p == w: # skip bottom assignment for last row
                    continue

                if not grid[j + dl][i + dw].passable:
                    continue

                graph[c].append(c + p)
                graph[c+p].append(c)
    return graph

#def find_shortest_path(grid, start_node, end_node):
#   #print_grid(grid, start_node, end_node)
#   print construct_graph(grid) 
#   return
    
    
def lt(a, b):
    return a[0] < b[0]

def gt(a, b):
    return a[0] > b[0]

def up(a, k, pos):
    while k > 1 and gt(a[k/2], a[k]):
        pos[a[k][1]]   = k/2
        pos[a[k/2][1]] = k
        a[k/2], a[k]   = a[k], a[k/2]
        k = k / 2


def heap_push(a, v, pos):
    a.append(v)
    up(a, len(a) - 1, pos)

def down(a, p, pos):
    n = len(a) - 1
    while 2 * p <=  n:    #left_child_index < max_node_index
        l = 2 * p
        if l < n and gt(a[l], a[l+1]): # l < n, says right exists
            l += 1

        if gt(a[p], a[l]):
            pos[a[p][1]] = l
            pos[a[l][1]] = p
            a[p], a[l] = a[l], a[p]
            p = l
        else:
            break


def heap_pop(a, pos):
    pos[a[-1][1]]  = 1
    a[-1], a[1] = a[1], a[-1]
    v = a.pop()
    down(a, 1, pos)
    return v


def find_shortest_path(grid, start_node, end_node):
    #print_grid(grid, start_node, end_node)
    g = construct_graph(grid)
    print g, start_node, end_node
    n = len(g)
    gl = len(grid)
    gw = len(grid[0])
    s = start_node.position.x * gw + start_node.position.y
    e = end_node.position.x * gw + end_node.position.y
    
    print s, e, n, gl, gw
    dist = [0]
    pos  = [i+1 for i in range(n)]
    for i in range(n):
        if i == s:
            heap_push(dist, (0, i), pos)
        else:
            heap_push(dist, (n, i), pos)
            
    prev = [-1 for i in range(n+1)]
    Q    = {i: 0 for i in range(n+1)}


    print Q, pos
    print dist    
    while len(Q) > 1:
        d, v = heap_pop(dist, pos)
        print d, v
        del Q[v]
        for nbr in g[v]:
            print nbr
            if nbr not in Q:
                continue
            print "dist: ", pos[nbr], dist[pos[nbr]]
            if d + 1 < dist[pos[nbr]][0]:
                dist[pos[nbr]] = (d + 1, nbr)
                up(dist, pos[nbr], pos)
                prev[nbr] = v
    print prev
    path = [e]
    c = e
    while prev[c] != s:
        c = prev[c]
        path.append(c)
    path.append(s)
    return path[::-1]
