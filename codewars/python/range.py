def solution(args):
    args = args + [max(args) + 2]
    s, e = 0, 0
    range = []
    while e <= len(args)-2:
        s = e
        while args[e] + 1 == args[e+1]:
            e += 1
        if e - s + 1 >= 3:
            range.append(str(args[s]) + "-" + str(args[e]))
        else:
            range += [str(i) for i in args[s:e+1]]    
        e += 1
    return ",".join(range)

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
