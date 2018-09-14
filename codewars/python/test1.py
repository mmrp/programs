def sum_pairs(ints, s):
    p = 0
    cur = [len(ints), len(ints)]
    while p < cur[1]:
        v = cur[p]
        if  s-v in ints[p+1:cur[1]]:
            ep = ints[p+1:cur[1]].index(s-v) + p + 1
            if ep < cur[1]:
                cur[0], cur[1] = p, ep
        p += 1
    if cur[0] == len(ints):
        return None
    return [ints[cur[0]], ints[cur[1]]]


a = [i for i in range(100000)]


print sum_pairs(a, 100001)
print sum_pairs([1, 4, 8, 7, 3, 15], 8)
