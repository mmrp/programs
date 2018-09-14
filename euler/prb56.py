

def get_sum(n):
	s=0;
	while n:
		s += n%10;
		n = n/10;	
	return s;

sum=0;
tsum=0;
for i in range(1,100):
	for j in range(1,100):
		tsum = get_sum(i**j);
		if tsum > sum:
			sum = tsum;


print sum;
