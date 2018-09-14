n = int(input().strip())
a = list(map(int, input().strip.split(' ')))
a.sort()
l = len(a)
print(sum(a)/l)
median = a[l/2]
if l % 2 == 0:
    median = (a[l/2] + a[l/2-1])/2
print(median)
print(max(a, key = lambda x: a.count(x)))

