


fact=range(0,10);
fact[0] = 1;
for i in range(1, 10):
	fact[i] = fact[i-1] * i;
fact[0] = 0;

gsum  = 0;
i = 3;
while i < 100000:
	j = i;
	sum = 0;
	while j:
		sum += fact[j%10];
		j = j / 10;	
	if i == sum:
		gsum += sum;	
	i += 1;

print gsum;
