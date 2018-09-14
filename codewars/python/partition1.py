def prod(n):
    ret = [{1.}]
    for i in range(1, n+1):
        ret.append({(i - x) * j for x, s in enumerate(ret) for j in s})
    return ret[-1]

print(prod(5))
