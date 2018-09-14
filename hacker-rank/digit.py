def super(n):
    while len(n) >= 2:
        n = str(sum(list(map(int, str(n)))))
    return int(n)

n, k = input().strip().split(" ")
n = sum(list(map(int, n))) * int(k)
print(super(str(n)))
