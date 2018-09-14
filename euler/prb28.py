i=3;
d = 2;
sum = 1;
while i < (1001 * 1001 +1):
	sum = sum + 4 * i + 6 * d;
	l = i + 3 * d;
	d = d + 2;
	i = l + d;
print sum;
