
def gcd(a,b):
	while (a > 0):
		if (b > a):
			a,b = b,a;
		a = a - b;
	return b;


print gcd(15499, 94744);
#
sn = 15499;
sd = 94744;
for d in range(0 , sd):
	f = 0;
	for s in range(1, d):
		if (gcd(s, d) == 1):
			f = f + 1;		
	
	print f, (d-1);
	if (f * sd < (d-1) * sn): # f/(d-1) < sn/sd
		break;
		

