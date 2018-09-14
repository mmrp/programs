import copy
def print_arr(a):
    for i in range(len(a)): print(a[i])

def get_generation(cells1, generations):
#    print(cells1, generations)
    cells = copy.deepcopy(cells1)
    print_arr(cells)
    for g in range(generations):
        r = len(cells)
        c = len(cells[0])
    
        temp = [[0] * (c+2) for _ in range(r + 2)]  
        temp_a = [[0] * (c+2) for _ in range(r + 2)]  
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if cells[i-1][j-1] == 1:
                    temp_a[i][j] = 1
                    temp[i-1][j-1] += 1
                    temp[i-1][j]   += 1
                    temp[i-1][j+1] += 1
                    temp[i][j-1]   += 1
                    temp[i][j+1]   += 1
                    temp[i+1][j-1] += 1
                    temp[i+1][j]   += 1
                    temp[i+1][j+1] += 1
        for i in range(r + 2):
            for j in range(c + 2):
                neighbors, alive = temp[i][j], temp_a[i][j]
                if alive:
                    if neighbors < 2 or neighbors > 3:
                        alive = 0 
                else:
                    if neighbors == 3:
                        alive = 1
                temp_a[i][j] = alive

        #print_arr(temp_a)
        # find first row, last row
        frow = -1
        for i in range(r+2):
            for j in range(c + 2):
                if temp_a[i][j]:
                    frow = i
                    break
            if frow != -1:
                break

        lrow = -1
        for i in range(r+1, -1, -1):
            for j in range(c + 2):
                if temp_a[i][j]:
                    lrow = i
                    break
            if lrow != -1:
                break

        fcol = -1
        for j in range(c + 2):
            for i in range(r+2): #, -1, -1):
                if temp_a[i][j]:
                    fcol = j
                    break
            if fcol != -1: 
                break

        lcol = -1
        for j in range(c + 1, -1, -1):
            for i in range(r+1, -1, -1):
                if temp_a[i][j]:
                    lcol = j
                    break
            if lcol != -1:
                break
 
        # find first col, last col
        #print(frow, fcol, lrow, lcol)
        cells = [[temp_a[i][j] for j in range(fcol, lcol+1)] for i in range(frow, lrow+1)]
        print("temp_a", print_arr(temp_a))
        print("temp", print_arr(temp))
        print("cells", print_arr(cells))
    #print htmlize(cells1)
    #print(cells)
    return cells #[cells[i][1:-1] for i in range(1, r)]

start = [[1,0,0],
         [0,1,1],
         [1,1,0]]
end   = [[0,1,0],
         [0,0,1],
         [1,1,1]]
         
resp = get_generation(start, 2)
print(resp)
