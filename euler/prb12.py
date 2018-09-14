

import math;
def prime_factor(n):

	count = 1;	
	tcount = 1;
	j = n;
	for i in range(2, math.sqrt(n)):
		tcount = 0;
		while (j > 1):
			if j % i == 0:
				j = j/i;
				tcount += 1;		
			else:
				break;
		count = count * (tcount+1);
	return count;


factors = 1;
i = 10;
while (factors < 500):
	factors = prime_factor((i*(i+1))/2);
	print (i*(i+1))/2, factors;
	if (factors > 500):
		break;
	i += 1;
	
